# agent.py - minimal Playwright script to open google.com (synchronous API)
# Notes:
# - Install Playwright and browsers before running this script (see Playwright docs).
# - This script opens a Chromium browser instance (headless=False) and navigates to Google.

from playwright.sync_api import sync_playwright
from agent_utils import DEFAULT_URL, DEFAULT_TIMEOUT_MS, HEADLESS, select_browser

# Browser selection
BROWSER = select_browser()


def run():
    try:
        with sync_playwright() as p:
            if BROWSER == "firefox":
                browser = p.firefox.launch(headless=HEADLESS)
            else:
                browser = p.chromium.launch(headless=HEADLESS)
            page = browser.new_page()
            page.goto(DEFAULT_URL)
            print(f"Opened {DEFAULT_URL}")
            # Keep the browser open briefly so you can see the page
            page.wait_for_timeout(DEFAULT_TIMEOUT_MS)
            browser.close()
    except Exception as e:
        print(f"Error running Playwright: {e}")


if __name__ == "__main__":
    run()
