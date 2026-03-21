
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def debug_dashboard():
    """Debug dashboard content"""
    print("🔍 Debugging dashboard...")
    
    with sync_playwright() as p:
        context = BrowserFactory.launch_persistent_context(p, headless=True)
        try:
            page = context.new_page()
            page.goto("https://notebooklm.google.com/notebook/ddd47ed3-7953-4a7d-8619-1e48e3dbab7a", wait_until="domcontentloaded")
            time.sleep(8) # Wait longer for notebook to load
            
            # Scroll to bottom to load all
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)
            
            print(f"PAGE TITLE: {page.title()}")
            print(f"URL: {page.url}")
            
            # Dump all buttons
            print("\nBUTTONS:")
            buttons = page.get_by_role("button").all()
            for b in buttons:
                try:
                    txt = b.inner_text().replace('\n', ' ')[:50]
                    aria = b.get_attribute("aria-label") or ""
                    print(f" - Text: '{txt}' | Aria: '{aria}'")
                except: pass
                
            # Dump inputs
            print("\nINPUTS & TEXTAREAS:")
            inputs = page.query_selector_all("input, textarea")
            for i in inputs:
                try:
                    tag = i.evaluate("el => el.tagName")
                    cls = i.get_attribute("class") or ""
                    placeholder = i.get_attribute("placeholder") or ""
                    aria = i.get_attribute("aria-label") or ""
                    print(f" - Tag: {tag} | Class: '{cls}' | Placeholder: '{placeholder}' | Aria: '{aria}'")
                except: pass
            
            print("\nBODY TEXT SAMPLE:")
            print(page.inner_text("body")[:2000]) # First 2000 chars
            
            # Try to find elements with "Christmas" or "Vanoce"
            print("\nSEARCHING FOR KEYWORDS:")
            for keyword in ["Christmas", "Vanoce", "Vánoce", "Xmas"]:
                count = page.get_by_text(keyword).count()
                if count > 0:
                    print(f"FOUND '{keyword}': {count} times")
                
        finally:
            context.close()

if __name__ == "__main__":
    debug_dashboard()
