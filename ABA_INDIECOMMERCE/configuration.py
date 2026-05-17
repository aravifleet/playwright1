from playwright.sync_api import sync_playwright
import time
import json
import configuration_utils

def website_accessiblecheck():
    print("Select the browser you want to use")
    print("1. Chromium | 2. Firefox | 3. Edge")
    choice = input("Enter the number 1/2/3 or type 0 to exit: ").strip()
    
    with sync_playwright() as p:
        browser = None
        
        if choice == '1':
            browser = configuration_utils.launch_chrome(p)
        elif choice == '2':
            browser = configuration_utils.launch_firefox(p)
        elif choice == '3':
            browser = configuration_utils.launch_edge(p)
        elif choice == '0':
            print("Exiting the configuration.")
            return
        
        if browser is None:
            print("Invalid choice. Please select a valid browser.")
            return
        
        page = browser.new_page()
        page.goto(configuration_utils.url)
        print("Page Title:", page.title())
        page.locator("//a[@title='Log in']").click()
        page.locator("id=edit-name").fill(configuration_utils.aba_email)
        page.locator("id=edit-name").press("Tab")
        page.locator("id=edit-pass").fill(configuration_utils.aba_password)
        page.locator("id=edit-pass").press("Tab")
        page.locator("id=edit-submit").press("Enter")
        page.locator("//span[text()='Dashboard']").click()
        page.goto(configuration_utils.url + configuration_utils.config_path)
        time.sleep(3)
        page.screenshot(path=configuration_utils.path, full_page=True)
        page.locator("//span[text()='Logout']").click()
        
        time.sleep(3)
        browser.close()
        
        
        

if __name__ == "__main__":
    website_accessiblecheck()
    