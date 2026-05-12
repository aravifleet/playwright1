# ABA IndieCommerce Configuration Check

This project automates the basic configuration check for the IndieCommerce site using Playwright.

## Prerequisites

- Python 3.10+
- Playwright

## Installation

1. **Set up a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install playwright
   playwright install
   ```

## Project Structure

- `basic_configurationcheck/`: Contains the automation scripts.
  - `configuration.py`: The main script to run the automation.
  - `configuration_utils.py`: Contains configuration variables (URL, credentials) and browser selection logic.
- `sample_images/`: Contains images (logos, favicons) used during the configuration process.

## How to Run

To run the configuration check, follow these steps:

1. Navigate to the root of the project.
2. Run the script using Python:

   ```bash
   python ABA_INDIECOMMERCE/basic_configurationcheck/configuration.py
   ```

3. When prompted, enter the browser type you wish to use (`firefox`, `edge`, or `chrome`).

### Note on File Paths
The script expects to be run from the project root so that it can correctly locate the images in `ABA_INDIECOMMERCE/sample_images`.

## Automation Steps

1. Launches the selected browser.
2. Navigates to the configured URL.
3. Logs in with the provided credentials.
4. Navigates to **IndieCommerce Settings > Design**.
5. Adds a new design with a custom title.
6. Uploads a logo and favicon from the `sample_images` folder.
7. Saves the design and activates it.
8. Logs out and closes the browser.
