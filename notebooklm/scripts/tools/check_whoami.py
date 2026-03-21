
import sys
import time
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def check_whoami():
    print("🔍 Checking logged in account...")
    
    with sync_playwright() as p:
        context = BrowserFactory.launch_persistent_context(p, headless=False) # Visible
        try:
            page = context.new_page()
            page.goto("https://myaccount.google.com/", wait_until="domcontentloaded")
            time.sleep(3)
            
            # Try to find email in the page
            # Usually in the header or "Welcome, Name"
            
            # 1. Page title often has "Google Account"
            print(f"Title: {page.title()}")
            
            # 2. Look for email in the top right user button aria-label
            user_btn = page.query_selector('a[aria-label*="@"]') or \
                       page.query_selector('div[aria-label*="@"]')
            
            if user_btn:
                label = user_btn.get_attribute("aria-label")
                print(f"✅ Found User Button: {label}")
                # label usually "Google Account: Name  (email@gmail.com)"
            else:
                # deeper search
                body_text = page.inner_text("body")
                if "@gmail.com" in body_text:
                    # simplistic find
                    import re
                    emails = re.findall(r'[\w\.-]+@gmail\.com', body_text)
                    if emails:
                        print(f"✅ Found emails on page: {list(set(emails))}")
                    else:
                         print("❓ Could not pinpoint email.")
                else:
                    print("❌ Not logged in?")
            
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            context.close()

if __name__ == "__main__":
    check_whoami()
