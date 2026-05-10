
from playwright.sync_api import sync_playwright
from cline_util import GREETING, GOOGLE_URL, BROWSERS

def run():
    browser_name_input = input("Enter browser (chrome, firefox, webkit, edge): ").lower()
    headless_input = input("Run in headless mode? (yes/no): ").lower()

    browser_type = BROWSERS.get(browser_name_input)
    if not browser_type:
        print("Invalid browser. Defaulting to chromium.")
        browser_type = "chromium"

    headless_mode = True if headless_input == "yes" else False

    with sync_playwright() as p:
        if browser_type == "chromium":
            browser = p.chromium.launch(headless=headless_mode)
        elif browser_type == "firefox":
            browser = p.firefox.launch(headless=headless_mode)
        elif browser_type == "webkit":
            browser = p.webkit.launch(headless=headless_mode)
        else:
            print("Unknown browser type. Defaulting to chromium.")
            browser = p.chromium.launch(headless=headless_mode)

        page = browser.new_page()
        page.goto(GOOGLE_URL)
        print(page.title())
        browser.close()

if __name__ == "__main__":
    print(GREETING)
    run()
