
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def inspect_drive(url):
    """Inspect a Drive URL"""
    print(f"🔍 Inspecting: {url}")
    
    with sync_playwright() as p:
        # HEADLESS=False to help with Google UI interactions and auth
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        try:
            page = context.new_page()
            page.goto(url, wait_until="networkidle", timeout=60000)
            time.sleep(5) 
            
            print(f"  Title: {page.title()}")
            
            # Take screenshot
            params = {"path": "drive_inspection.png"}
            page.screenshot(**params)
            print("  📸 Saved screenshot to drive_inspection.png")
            
            # Try to list items
            # Google Drive list items often have role="row" or specific class
            items = page.query_selector_all('div[role="row"]')
            print(f"  Found {len(items)} items (rows).")
            
            for item in items:
                print(f"   - {item.inner_text().splitlines()[0]}")

            return True
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    
    inspect_drive(args.url)
