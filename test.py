import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


user_browser = input("Enter the browser you want to use (chromium,firefox,webkit,edge): ").strip().lower()

def run(playwright: Playwright) -> None:
    if user_browser == "chromium":
          browser = playwright.chromium.launch(headless=False)
    elif user_browser =="firefox":
          browser = playwright.firefox.launch(headless=False)
    elif user_browser == "edge":
          browser = playwright.chromium.launch(channel="msedge", headless=False)
    elif user_browser == "webkit":
          browser = playwright.webkit.launch(headless=False)
    else:
        print("Kindly enter the valid user browser name")
        return
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    page.locator("//*[@title='Search']").fill("TTD")
    page.locator("//*[@title='Search']").press("Enter")
    time.sleep(2)
    print("The program was executed successfully")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
