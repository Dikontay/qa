from config import initialize_driver
from waits import set_implicit_wait, wait_for_search_button, fluent_wait_for_results
from actions import hover_over_repository
from dropdowns import interact_with_dropdown
from selenium.webdriver.common.by import By
import logging

def main():
    driver = initialize_driver()
    try:
        # Open GitHub
        driver.get("https://github.com")
        logging.info("Opened GitHub homepage.")

        # Set implicit wait
        set_implicit_wait(driver)

        
       

        # Explicit wait for the search button
        wait_for_search_button(driver)
     
        

        # Fluent wait for results
        fluent_wait_for_results(driver)

        # Hover over repository'
        hover_over_repository(driver)

    except Exception as e:
        logging.critical(f"Critical error occurred: {e}")
    finally:
        driver.quit()
        logging.info("Closed the browser and ended the script.")

if __name__ == "__main__":
    main()
