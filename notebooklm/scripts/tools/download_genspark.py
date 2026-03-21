
import sys
import time
import argparse
import os
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def download_and_capture(url, output_dir):
    print(f"🚀 Starting GenSpark Capture: {url}")
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "screenshots").mkdir(exist_ok=True)
    
    with sync_playwright() as p:
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        try:
            page = context.new_page()
            page.goto(url, wait_until="networkidle", timeout=60000)
            
            print("  Waiting 20s for app to hydrate...")
            time.sleep(20)
            
            # 1. Attempt PDF Download
            print("  --- PDF EXPORT ---")
            
            # Check for generic dialog first (since URL has export_dialog=true)
            dialog = page.query_selector('div[role="dialog"]')
            if dialog and dialog.is_visible():
                print("  ✅ Export dialog found open.")
            else:
                print("  Export dialog not open. Searching for button...")
                try:
                    # Look for "Export" or "Download" or "Share"
                    export_btn = page.query_selector('button:has-text("Export")') or \
                                 page.query_selector('button:has-text("Download")') or \
                                 page.query_selector('button[aria-label="Export"]')
                    if export_btn:
                        print("  Clicking Export button...")
                        export_btn.click()
                        time.sleep(3)
                except Exception as e:
                    print(f"  Could not open export: {e}")

            # Now look for PDF option in dialog
            try:
                # This is a guess at selectors based on common patterns. 
                # Ideally we'd inspect the DOM, but we are blind.
                # Look for "PDF" text
                pdf_btn = page.query_selector('text="PDF"') or \
                          page.query_selector('div:has-text("PDF")') or \
                          page.query_selector('button:has-text("PDF")')
                
                if pdf_btn:
                    print("  Selected PDF format.")
                    pdf_btn.click()
                    time.sleep(1)
                    
                    # Look for "Download" or "Export" confirm button
                    confirm_btn = page.query_selector('div[role="dialog"] button:has-text("Download")') or \
                                  page.query_selector('div[role="dialog"] button:has-text("Export")')
                                  
                    if confirm_btn:
                        print("  Clicking Download confirm...")
                        # Setup download listener
                        with page.expect_download(timeout=60000) as download_info:
                            confirm_btn.click()
                        
                        download = download_info.value
                        download_path = output_path / "presentation.pdf"
                        download.save_as(download_path)
                        print(f"  ✅ PDF Downloaded: {download_path}")
                        
                        # Close dialog if still open
                        page.keyboard.press("Escape")
                        time.sleep(1)
            except Exception as e:
                print(f"  ❌ PDF Download failed: {e}")
                # Close dialog to proceed to screenshots
                page.keyboard.press("Escape")
                time.sleep(1)

            # 2. Capture Screenshots (Slides)
            print("  --- SCREENSHOT CAPTURE ---")
            
            # Find navigation (Next button)
            # Usually bottom right or right side. Arrow icon.
            # Using keyboard is safer if supported.
            
            # First, ensure focus is on body/slides
            page.click("body")
            
            for i in range(1, 15): # Assume max 15 slides
                screenshot_file = output_path / "screenshots" / f"slide_{i:02d}.png"
                page.screenshot(path=str(screenshot_file))
                print(f"  📸 Captured {screenshot_file.name}")
                
                # Check if we reached end? Hard to know visually.
                # Just press Right Arrow
                page.keyboard.press("ArrowRight")
                time.sleep(2) # Wait for transition
                
            print("✅ Capture sequence complete.")
            return True

        except Exception as e:
            print(f"❌ Critical Error: {e}")
            return False
        finally:
            context.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", default=r"C:\Users\Rosta\Desktop\XMAS 2027")
    args = parser.parse_args()
    
    download_and_capture(args.url, args.output)
