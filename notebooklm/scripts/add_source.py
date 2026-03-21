
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def add_source(notebook_url, source_url):
    """Add a source to an existing notebook"""
    print(f"✨ Adding source to notebook: {notebook_url}")
    
    with sync_playwright() as p:
        context = BrowserFactory.launch_persistent_context(p, headless=True)
        try:
            page = context.new_page()
            page.goto(notebook_url, wait_until="domcontentloaded")
            time.sleep(5) 
            
            # Check if we need to open "Add source" menu
            # If empty, often source icons are visible.
            # Look for YouTube text or icon
            print("  SEARCHING: Source options...")
            
            # Try finding "YouTube" directly
            youtube_btn = page.query_selector('div:has-text("YouTube")') or page.query_selector('button:has-text("YouTube")')
            
            if not youtube_btn:
                # Try clicking "Add source" plus button first
                print("  ...clicking Add Source button...")
                add_btn = page.query_selector('button[aria-label="Add source"]') or page.query_selector('span:has-text("Add source")')
                if add_btn:
                    add_btn.click()
                    time.sleep(2)
                    youtube_btn = page.query_selector('div:has-text("YouTube")') or page.query_selector('button:has-text("YouTube")')

            if youtube_btn:
                print("  CLICK: YouTube")
                youtube_btn.click()
                
                print("  ...waiting for input...")
                input_box = page.wait_for_selector('input[type="text"]', timeout=5000)
                if input_box:
                    print(f"  ...filling URL: {source_url}")
                    input_box.fill(source_url)
                    time.sleep(1)
                    page.keyboard.press("Enter")
                    
                    print("  ...submitted...")
                    
                    # Wait for "Insert" button if it appears (common in new UI)
                    try:
                        insert_btn = page.wait_for_selector('button:has-text("Insert")', timeout=8000)
                        if insert_btn:
                            print("  CLICK: Insert")
                            insert_btn.click()
                    except:
                        print("  (No Insert button found, assuming auto-submit)")
                        
                    # Wait for processing
                    print("  WAITING: Source processing...")
                    time.sleep(10)
                    
                    print("✅ Source addition flow completed")
                    return True
                else:
                    print("❌ Input box not found")
            else:
                print("❌ YouTube source option not found")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--source", required=True)
    args = parser.parse_args()
    
    add_source(args.url, args.source)
