import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("selenium_github.log"),
        logging.StreamHandler()
    ]
)

def initialize_driver():
    """Initialize and return the WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    logging.info("Initialized WebDriver and maximized the window.")
    return driver
