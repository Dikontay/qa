from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

def hover_over_repository(driver):
    """Hover over the first repository in the search results."""
    try:
        # Locate the first repository item
        repo_item = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/main/react-app/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div[4]/div/div/div[1]/div/div[1]/h3/div/div[2]/a")
        actions = ActionChains(driver)
        actions.move_to_element(repo_item).perform()
        logging.info("Hovered over the first repository in the search results.")
    except Exception as e:
        logging.error(f"Error hovering over the repository: {e}")
        raise

def click_first_repository(driver):
    """Click on the first repository link in the search results."""
    try:
        # Use explicit wait to ensure the repository link is clickable
        repo_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'repo-list-item')][1]//a"))
        )
        repo_name = repo_link.text  # Save the repository name for logging
        repo_link.click()
        logging.info(f"Clicked on the repository: {repo_name}")
    except Exception as e:
        logging.error(f"Error clicking on the repository: {e}")
        raise