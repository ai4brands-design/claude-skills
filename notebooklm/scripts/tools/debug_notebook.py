
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def debug_notebook(url):
    """Debug notebook content"""
    print(f"🔍 Debugging notebook: {url}")
    
    with sync_playwright() as p:
        context = BrowserFactory.launch_persistent_context(p, headless=True)
        try:
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded")
            time.sleep(10) # Wait for full load
            
            print(f"PAGE TITLE: {page.title()}")
            print(f"URL: {page.url}")
            
            # Check for common inputs
            print("\nINPUTS/TEXTAREAS:")
            inputs = page.query_selector_all("textarea, input")
            for i in inputs:
                try:
                    p_text = i.get_attribute("placeholder") or ""
                    aria = i.get_attribute("aria-label") or ""
                    cls = i.get_attribute("class") or ""
                    print(f" - Tag: {i.evaluate('el => el.tagName')} | Class: '{cls}' | Placeholder: '{p_text}' | Aria: '{aria}'")
                except: pass

        finally:
            context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    debug_notebook(args.url)
