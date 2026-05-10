# agent_utils.py - utility constants and helper functions for agent.py

DEFAULT_URL = "https://www.google.com"
DEFAULT_TIMEOUT_MS = 5000  # milliseconds
PROMPT = "Select browser (chrome/firefox) [chrome]: "
UNKNOWN_CHOICE_MSG = "Unknown choice '{choice}', defaulting to chrome."
HEADLESS = False


def select_browser():
    """Prompt the user to select a browser. Returns 'chromium' or 'firefox'."""
    try:
        choice = input(PROMPT).strip().lower()
    except Exception:
        choice = ""

    if choice in ("chrome", "chromium", ""):
        return "chromium"
    elif choice == "firefox":
        return "firefox"
    else:
        print(UNKNOWN_CHOICE_MSG.format(choice=choice))
        return "chromium"
