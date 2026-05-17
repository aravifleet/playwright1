url = "https://live-icsample1657400753.pantheonsite.io/"
path = "ABA_INDIECOMMERCE/configurationscreens/config.png"
aba_email = "aravi+abaadmin@fleetstudio.com"
aba_password = "Fleet@84"
config_path = "admin/config/development/configuration"

def launch_chrome(p): 
    return p.chromium.launch(headless=False)

def launch_firefox(p):
    return p.firefox.launch(headless=False)

def launch_edge(p):
    return p.chromium.launch(channel='msedge', headless=False)

