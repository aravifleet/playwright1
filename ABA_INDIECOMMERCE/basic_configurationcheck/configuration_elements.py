# Selectors for the IndieCommerce configuration automation

LOGIN_LINK = "//a[text()='Log in']"
USERNAME_INPUT = "//input[@name='name']"
PASSWORD_INPUT = "//input[@name='pass']"
LOGIN_BUTTON = "//input[@value='Login']"

SETTINGS_LINK = "//*[text()='IndieCommerce Settings']"
DESIGN_TAB = "//a[text()='Design']"
ADD_DESIGN_LINK = "//a[contains(., 'Add Design')]"

DESIGN_TITLE_INPUT = "//input[@name='title[0][value]']"
THEME_ROSE_RADIO = "//input[@value='Rose']"
LOGO_UPLOAD_INPUT = "//input[@id='edit-field-logo-0-upload']"
FAVICON_UPLOAD_INPUT = "//input[@value='Add a new file']"
SAVE_BUTTON = "//input[@value='Save']"

EDIT_DESIGN_LINK_PARTIAL = "//a[contains(text(), 'Edit DEMODESIGNS1')]"
CHECKBOX_INPUT = "//input[@type='checkbox']"

BACK_TO_ACCOUNT_LINK = "//*[contains(text(), 'Back to the site My Account')]"
LOGOUT_LINK = "//a[text()='Logout']"
