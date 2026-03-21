
import sys
import os
import argparse
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def capture_local_html(html_path, output_dir):
    print(f"📸 Capturing Slides from: {html_path}")
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    (output_path / "screenshots").mkdir(exist_ok=True)
    
    # Convert local path to file URL
    file_url = Path(html_path).as_uri()
    
    with sync_playwright() as p:
        # Launch browser to render the local file
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        try:
            page = context.new_page()
            # Set viewport to match slide dimensions to ensure correct rendering (1280x720)
            page.set_viewport_size({"width": 1280, "height": 720})
            
            print(f"  Loading {file_url}...")
            page.goto(file_url, wait_until="domcontentloaded")
            
            # Additional wait for fonts/Tailwind scripts from CDN
            print("  Waiting 5s for resources...")
            page.wait_for_timeout(5000)
            
            # REMOVE ALL EXTERNAL STYLESHEETS/FONTS
            print("  Removing all external stylesheets to prevent timeout...")
            page.evaluate("""() => {
                document.querySelectorAll('link[rel="stylesheet"]').forEach(l => l.remove());
            }""")
            
            # Find all slide elements
            slides = page.query_selector_all(".ppt-slide")
            print(f"  Found {len(slides)} slides.")
            
            pdf_pages = []
            
            # Try full page screenshot
            print("  Capturing full page...")
            page.screenshot(path=str(output_path / "presentation_full.png"), full_page=True)
            print("  ✅ Saved presentation_full.png")
            
            """
            for i, slide in enumerate(slides, 1):
                image_path = output_path / "screenshots" / f"slide_{i:02d}.png"
                print(f"  Capturing Slide {i}...")
                
                # Scroll to element to ensure it's rendered (though screenshot handles this)
                slide.scroll_into_view_if_needed()
                
                # Take element screenshot
                slide.screenshot(path=str(image_path))
                print(f"  ✅ Saved {image_path.name}")
            """
            
            print("✅ Capture complete.")
            return True

        except Exception as e:
            print(f"❌ Error: {e}")
            return False
        finally:
            context.close()

if __name__ == "__main__":
    target_html = r"C:\Users\Rosta\Desktop\XMAS 2027\presentation.html"
    output_dir = r"C:\Users\Rosta\Desktop\XMAS 2027"
    
    capture_local_html(target_html, output_dir)
