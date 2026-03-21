
import sys
import json
import time
from pathlib import Path
from patchright.sync_api import sync_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from browser_utils import BrowserFactory

def discover_notebooks():
    """Scrape the dashboard for notebooks"""
    print("🔍 Discovering notebooks from dashboard...")
    
    with sync_playwright() as p:
        # Launch using our authenticated context factory
        # HEADLESS=False to help with Google UI interactions
        context = BrowserFactory.launch_persistent_context(p, headless=False)
        
        try:
            page = context.new_page()
            page.goto("https://notebooklm.google.com/", wait_until="domcontentloaded")
            
            # Wait for meaningful content (notebook cards)
            # We wait for at least one link with /notebook/ in it
            try:
                page.wait_for_selector('a[href*="/notebook/"]', timeout=10000)
            except:
                print("⚠️ No notebooks found immediately. Waiting a bit longer...")
                time.sleep(5)
                
            # Extract all notebook links
            notebooks = []
            links = page.query_selector_all('a[href*="/notebook/"]')
            
            for link in links:
                href = link.get_attribute("href")
                # Sometimes title is in a child div, or the link text itself
                # Let's try to get a reasonable name
                title = link.inner_text().split('\n')[0].strip()
                if not title:
                    title = "Untitled Notebook"
                    
                # Ensure full URL
                if href.startswith("/"):
                    href = "https://notebooklm.google.com" + href
                    
                # Simple dedup based on URL
                if not any(n['url'] == href for n in notebooks):
                    notebooks.append({
                        "title": title,
                        "url": href
                    })
            
            return notebooks
            
        finally:
            context.close()

if __name__ == "__main__":
    try:
        notebooks = discover_notebooks()
        if notebooks:
            print(f"\n✅ Found {len(notebooks)} notebooks:")
            for nb in notebooks:
                print(f"- {nb['title']}")
                print(f"  Url: {nb['url']}")
        else:
            print("❌ No notebooks found. You might need to create one first.")
    except Exception as e:
        print(f"❌ Error: {e}")
