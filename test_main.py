import time
import pytest
import logging
from config import initialize_driver
from waits import set_implicit_wait, wait_for_search_button, fluent_wait_for_results
from actions import hover_over_repository
from selenium.common.exceptions import TimeoutException

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.fixture(scope="module")
def driver():
    # Initialize the driver
    driver = initialize_driver()
    driver.get("https://github.com")
    logging.info("Opened GitHub homepage.")
    yield driver
    driver.quit()
    logging.info("Closed the browser.")

def test_implicit_wait(driver):
    logging.info("Starting test: test_implicit_wait")
    try:
        set_implicit_wait(driver)
        time.sleep(2)
        logging.info("Implicit wait set successfully.")
    except Exception as e:
        logging.error(f"Implicit wait failed: {e}")
        pytest.fail(f"Implicit wait test failed: {e}")
        

def test_explicit_wait(driver):
    logging.info("Starting test: test_explicit_wait")
    try:
        wait_for_search_button(driver)
        time.sleep(2)
        logging.info("Search button found using explicit wait.")
    except TimeoutException:
        logging.error("Search button not found in time.")
        pytest.fail("Explicit wait test failed: Search button not found.")

def test_fluent_wait(driver):
    logging.info("Starting test: test_fluent_wait")
    try:
        fluent_wait_for_results(driver)
        time.sleep(2)
        logging.info("Results appeared using fluent wait.")
    except TimeoutException:
        logging.error("Results did not appear in time.")
        pytest.fail("Fluent wait test failed: Results not found.")

def test_hover_action(driver):
    logging.info("Starting test: test_hover_action")
    try:
        hover_over_repository(driver)
        time.sleep(2)
        logging.info("Hovered over repository successfully.")
    except Exception as e:
        logging.error(f"Hover action failed: {e}")
        pytest.fail(f"Hover action test failed: {e}")
