
import sys
import time
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def upload_text_source(notebook_url, title, content):
    """Add a text source to an existing notebook"""
    print(f"✨ Adding text source '{title}' to notebook...")
    
    with sync_playwright() as p:
        # HEADLESS=False to help with Google UI interactions
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        try:
            page = context.new_page()
            page.goto(notebook_url, wait_until="domcontentloaded")
            time.sleep(5) 
            
            # 0. Check if modal is ALREADY open (Any dialog)
            print("  CHECKING: Is modal already open?")
            dialog = page.query_selector('div[role="dialog"]') or \
                     page.query_selector('.dialog-container') or \
                     page.query_selector('mat-dialog-container')
                     
            if dialog and dialog.is_visible():
                print("  ✅ Modal (dialog) appears to be already open.")
                text_btn = True # Fake it to skip button search
            else:
                # 1. Open "Add source" menu if needed
                print("  SEARCHING: Source options...")
            
            # Try multiple variations
            selectors = [
                'div:has-text("Copied text")',
                'div:has-text("Paste text")',
                'button:has-text("Copied text")',
                'span:has-text("Copied text")',
                'div[aria-label="Copied text"]',
                'div[role="button"]:has-text("text")'
            ]
            
            text_btn = None
            for sel in selectors:
                text_btn = page.query_selector(sel)
                if text_btn: break

            if not text_btn:
                # Try clicking "Add source" plus button first
                print("  ...clicking Add Source button...")
                add_btn = page.query_selector('button[aria-label="Add source"]') or page.query_selector('span:has-text("Add source")')
                if add_btn:
                    add_btn.click()
                    time.sleep(3) # Increase wait
                    
                    # Search again
                    for sel in selectors:
                       text_btn = page.query_selector(sel)
                       if text_btn: break
            
            if text_btn:
                print(f"  CLICK: {text_btn.inner_text()}")

                text_btn.click()
                
                print("  ...waiting for modal...")
                # Wait for the modal/input area
                time.sleep(2) # Animation wait
                
                # Title input often has placeholder "Title" or is the first input
                # Try multiple strategies
                title_selectors = [
                    'input[placeholder="Title"]',
                    'input[aria-label="Title"]',
                    'input[data-placeholder="Title"]',
                    'input[type="text"]' # Fallback to any text input
                ]
                
                title_input = None
                for sel in title_selectors:
                    try:
                        title_input = page.wait_for_selector(sel, timeout=3000)
                        if title_input:
                            print(f"    Found title input: {sel}")
                            break
                    except:
                        continue
                
                if not title_input:
                    # Final Hail Mary: Get all inputs and pick the first visible one
                    inputs = page.query_selector_all('input')
                    for inp in inputs:
                        if inp.is_visible():
                            title_input = inp
                            print("    Found generic visible input")
                            break
                
                if title_input:
                    print(f"  ...filling Title: {title}")
                    title_input.fill(title)
                else:
                    print("❌ Could not find ANY title input")
                
                # Content textarea often has placeholder "Paste text" or similar
                # Or it is a contenteditable div
                print(f"  ...filling Content ({len(content)} chars)...")
                
                # Strategy: Try contenteditable div FIRST (common in Google apps)
                print(f"  ...filling Content ({len(content)} chars)...")
                
                content_filled = False
                
                # 1. Try contenteditable
                content_div = page.query_selector('div[contenteditable="true"]')
                if content_div and content_div.is_visible():
                    print("    Found contenteditable div")
                    # contenteditable doesn't support fill(), need click + type or evaluate
                    content_div.click()
                    # For large content, type is slow. Use clipboard or innerText
                    # But innerText might not trigger angular change detection
                    # Let's try filling via keyboard
                    content_div.fill(content) 
                    content_filled = True
                
                # 2. Try TextArea (enabled only)
                if not content_filled:
                    textareas = page.query_selector_all('textarea')
                    for ta in textareas:
                        if ta.is_visible() and ta.is_enabled():
                            print("    Found enabled textarea")
                            ta.fill(content)
                            content_filled = True
                            break
                            
                # 3. Fallback: Tab from title
                if not content_filled and title_input:
                    print("    Fallback: Tabbing from title")
                    title_input.focus()
                    title_input.press("Tab")
                    # Check if we moved?
                    time.sleep(0.5)
                    page.keyboard.insert_text(content)
                    content_filled = True
                
                time.sleep(1)
                
                # Click Insert/Add
                print("  ...submitting...")
                insert_btn = page.query_selector('button:has-text("Insert")') or \
                             page.query_selector('button:has-text("Add")')
                
                if insert_btn:
                    insert_btn.click()
                    print("  CLICK: Insert")
                    
                    # Wait for processing
                    print("  WAITING: Source processing...")
                    time.sleep(5)
                    print("✅ Source addition flow completed")
                    return True
                else:
                    print("❌ Insert button not found")
                    return False

            else:
                print("❌ 'Copied text' source option not found")
                return False
                
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--content-file", required=True, help="Path to file containing content")
    args = parser.parse_args()
    
    try:
        with open(args.content_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if upload_text_source(args.url, args.title, content):
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"Error reading file or uploading: {e}")
        sys.exit(1)
