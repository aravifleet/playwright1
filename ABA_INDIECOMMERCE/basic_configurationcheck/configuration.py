import re
from playwright.sync_api import Playwright, sync_playwright, expect
import configuration_utils
import configuration_elements
import os


base_path = "ABA_INDIECOMMERCE/sample_images"

logo_path = os.path.join(base_path, "ic-final-20logo.png")
favicon_path = os.path.join(base_path, "ic-favicon.png")


def run(playwright: Playwright) -> None:
    # --- Browser Selection Logic (KEEPING THIS) ---
    selected_browser = configuration_utils.browser_type
    
    if selected_browser == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif selected_browser == "edge":
        browser = playwright.chromium.launch(headless=False, channel="msedge")
    else:
        # Default to Chrome
        browser = playwright.chromium.launch(headless=False)
    
    context = browser.new_context()
    page = context.new_page()
    
    # --- Reverted to your Original Stable Logic ---
    page.goto(configuration_utils.url)
    page.locator(configuration_elements.LOGIN_LINK).click()
    page.locator(configuration_elements.USERNAME_INPUT).fill(configuration_utils.email)
    page.locator(configuration_elements.PASSWORD_INPUT).fill(configuration_utils.password)
    page.locator(configuration_elements.LOGIN_BUTTON).click()
    
    # Debug: Wait for load state and take a screenshot after login attempt
    page.wait_for_load_state("networkidle")
    page.screenshot(path="after_login.png")
    
    # Check for session limit form
    if page.locator("text=You have too many active sessions").is_visible():
        print("Session limit reached. Ending sessions...")
        page.screenshot(path="session_limit_debug.png")
        
        # Try to select all other sessions
        sessions = page.locator("input[type='checkbox'][name^='sessions']")
        if sessions.count() > 0:
            print(f"Checking {sessions.count()} session checkboxes")
            for i in range(sessions.count()):
                sessions.nth(i).check()
            
            disconnect_button = page.locator("input[value='Disconnect session'], button:has-text('Disconnect session')")
            if disconnect_button.is_visible():
                print("Clicking Disconnect session...")
                disconnect_button.click()
                page.wait_for_load_state("networkidle")
                page.screenshot(path="after_session_disconnect.png")
        else:
            # Maybe there is a 'Close all other sessions' or similar
            submit = page.locator("input[type='submit']")
            if submit.count() > 0:
                print("Clicking first submit button on session limit page...")
                submit.first.click()
                page.wait_for_load_state("networkidle")
                page.screenshot(path="after_session_disconnect.png")

    page.locator(configuration_elements.SETTINGS_LINK).first.click()
    page.locator(configuration_elements.SETTINGS_LINK).first.click()
    page.locator(configuration_elements.DESIGN_TAB).click()
    page.screenshot(path="before_add_design.png")
    page.locator(configuration_elements.ADD_DESIGN_LINK).click()
    page.locator(configuration_elements.DESIGN_TITLE_INPUT).fill("DEMODESIGNS123 - playwrightcoderunner")
    page.locator(configuration_elements.THEME_ROSE_RADIO).click()
    page.locator(configuration_elements.LOGO_UPLOAD_INPUT).set_input_files(logo_path)
    page.locator(configuration_elements.FAVICON_UPLOAD_INPUT).set_input_files(favicon_path)
    page.locator(configuration_elements.SAVE_BUTTON).click()
    page.locator(configuration_elements.EDIT_DESIGN_LINK_PARTIAL).first.click()
    page.locator(configuration_elements.CHECKBOX_INPUT).check()
    page.locator(configuration_elements.SAVE_BUTTON).click()
    page.locator(configuration_elements.BACK_TO_ACCOUNT_LINK).click()
    page.locator(configuration_elements.LOGOUT_LINK).click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)