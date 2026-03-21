
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory, StealthUtils

def create_notebook(source_url: str = None):
    """Create a new notebook and optionally add a source"""
    print("✨ Creating new notebook...")
    
    with sync_playwright() as p:
        # HEADLESS=False to help with Google UI interactions
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        
        try:
            page = context.new_page()
            page.goto("https://notebooklm.google.com/", wait_until="domcontentloaded")
            time.sleep(5) # Allow scripts to hydrate
            
            # 1. Click "New Notebook"
            print("  SEARCHING: New Notebook button...")
            try:
                # Try multiple selectors
                selectors = [
                    'div.notebook-grid-item-new', 
                    'span:has-text("New Notebook")',
                    'div[role="button"]:has-text("New Notebook")',
                    'button[aria-label="Create new notebook"]'
                ]
                
                new_btn = None
                for selector in selectors:
                    print(f"    ...trying selector: {selector}")
                    try:
                        new_btn = page.wait_for_selector(selector, timeout=3000)
                        if new_btn:
                            print(f"    ✅ Found: {selector}")
                            break
                    except:
                        continue
                
                if new_btn:
                    print(f"  CLICK: {selector} (Standard Click)")
                    new_btn.hover()
                    time.sleep(1)
                    new_btn.click()
                    
                    # Check if URL changed
                    time.sleep(3)
                    if "/notebook/" in page.url and "creating" not in page.url:
                        print("  ✅ Click succcessful")
                    else:
                        print("  Basic click didn't navigate. Trying Keyboard...")
                        # Focus and Enter
                        new_btn.focus()
                        time.sleep(0.5)
                        page.keyboard.press("Enter")
                        
                else:
                    print("  ❌ Could not find New Notebook button with any selector")
                    # Fallback: Tab navigation
                    print("  Trying blind TAB navigation...")
                    page.keyboard.press("Tab")
                    page.keyboard.press("Tab")
                    page.keyboard.press("Tab") # Usually 3-5 tabs to get to grid
                    page.keyboard.press("Enter")
                    
            except Exception as e:
                print(f"  ❌ Failed to find/click New Notebook: {e}")
                
            # 2. Wait for notebook to load (and filter out transient URLs)
            print("  WAITING: Notebook creation (30s timeout)...")
            try:
                # Wait for URL that is NOT .../creating
                # regex: /notebook/[a-zA-Z0-9-]+
                page.wait_for_url(lambda url: "/notebook/" in url and "creating" not in url, timeout=30000)
                
                notebook_url = page.url
                print(f"  ✅ Created: {notebook_url}")
            except:
                print("  ❌ Timeout waiting for notebook URL creation")
                print(f"  Current URL: {page.url}")
                # Try to grab the first notebook if we are still on dashboard?
                # Maybe we created it but didn't navigate?
                return None

            # 3. Add Source if provided (Logic continues...)
            if source_url:
                print(f"  ADDING SOURCE: {source_url}")
                try:
                    # After creation, "Add source" modal/panel is usually open
                    time.sleep(3) # Let source options animate in
                    
                    # Look for YouTube option
                    # Try text first
                    youtube_option = page.query_selector('text="YouTube"')
                    if not youtube_option:
                         # Maybe inside a button or div with specific class
                         # Try generic "YouTube" mapping
                         youtube_option = page.query_selector('div:has-text("YouTube")')

                    if youtube_option:
                        print("  CLICK: YouTube source")
                        youtube_option.click()
                        
                        # Wait for input
                        print("  ...waiting for input...")
                        input_box = page.wait_for_selector('input[type="text"]', timeout=5000)
                        if input_box:
                            input_box.fill(source_url)
                            time.sleep(1)
                            page.keyboard.press("Enter")
                            
                            print("  ...submitted source...")
                            # Wait for "Insert" or "Add" if a second step is needed? 
                            # Usually hitting Enter starts fetching.
                            # Then there might be an "Insert" button to confirm after preview.
                            
                            try:
                                # Look for "Insert" or "Add" button that appears after fetch
                                insert_btn = page.wait_for_selector('button:has-text("Insert")', timeout=8000)
                                if insert_btn:
                                    print("  CLICK: Insert")
                                    insert_btn.click()
                                    time.sleep(5) # Wait for import
                            except:
                                print("  ⚠️ No 'Insert' button found, maybe auto-added?")
                                
                        else:
                             print("  ❌ Could not find source input box")
                    else:
                        print("  ❌ Could not find YouTube source option")

                except Exception as e:
                    print(f"  ❌ Failed verification of source addition: {e}")
            
            return notebook_url
            
        finally:
            context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", help="Source URL to add (e.g., YouTube)")
    args = parser.parse_args()
    
    try:
        url = create_notebook(args.source)
        if url:
            print(f"\nNEW_NOTEBOOK_URL={url}")
        else:
            sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
