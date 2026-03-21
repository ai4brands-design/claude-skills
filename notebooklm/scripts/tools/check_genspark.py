
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def check_genspark(url):
    print(f"🔍 Checking GenSpark URL: {url}")
    
    with sync_playwright() as p:
        # Launch visible browser to see what happens
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        try:
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=60000)
            
            print("  Waiting for page load...")
            time.sleep(20) # Give it time to render React/Canvas apps (increased)
            
            title = page.title()
            print(f"  Page Title: {title}")
            
            # Take screenshot
            params = {"path": "genspark_check.png"}
            page.screenshot(**params)
            print("  📸 Saved screenshot to genspark_check.png")
            
            # Check for specific elements that indicate success
            body_text = page.inner_text("body")
            if "Login" in body_text or "Sign up" in body_text:
                print("  ⚠️ Potential Login Wall detected.")
            else:
                print("  ✅ Content seems accessible (no obvious login wall).")
                
            # Check for export dialog since it's in the URL
            dialog = page.query_selector('div[role="dialog"]')
            if dialog:
                print("  ℹ️ Dialog detected (likely export/download).")
            
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
    
    check_genspark(args.url)
