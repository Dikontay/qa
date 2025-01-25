package com.github.test;

import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import com.aventstack.extentreports.*;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;
import java.time.Duration;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeoutException;

import org.testng.annotations.BeforeTest;
import org.testng.annotations.Test;
import org.testng.annotations.AfterTest;

public class GitHubTests {
    WebDriver driver;
    ExtentReports extent;
    ExtentTest test;
    private static final Logger logger = LogManager.getLogger(GitHubTests.class);

    @BeforeTest
    public void setup() {
        ExtentSparkReporter spark = new ExtentSparkReporter("extent-report.html");
        extent = new ExtentReports();
        extent.attachReporter(spark);

        System.setProperty("webdriver.chrome.driver", "/opt/homebrew/bin/chromedriver");

        ChromeOptions options = new ChromeOptions();
        // options.addArguments("--headless"); // Run in headless mode (optional)
        // options.addArguments("--disable-dev-shm-usage");
        // options.addArguments("--no-sandbox");
        options.addArguments("--remote-allow-origins=*");

        driver = new ChromeDriver(options);
        driver.manage().window().maximize();
    }

    @Test
    public void searchGitHub() {
        test = extent.createTest("GitHub Search Test");
        test.log(Status.INFO, "Opening GitHub homepage");
        logger.info("Opening GitHub homepage");
        driver.get("https://github.com");

        WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20)); // Increase timeout if necessary
        try {
            WebElement searchButton = wait.until(ExpectedConditions.elementToBeClickable(By.cssSelector("[data-target='qbsearch-input.inputButton']")));
            searchButton.click();

            test.log(Status.INFO, "Search button clicked, opening search input");
            logger.info("Search button clicked, opening search input");

            WebElement searchBox = wait.until(ExpectedConditions.visibilityOfElementLocated(By.id("query-builder-test")));
            searchBox.sendKeys("Java");
            searchBox.submit();

            logger.info("Search executed successfully");
            test.log(Status.INFO, "Search executed successfully");

            if (driver.getTitle().contains("Search")) {
                test.pass("Page title verified");
            } else {
                test.fail("Page title verification failed");
            }

        } catch (NoSuchElementException e) {
            logger.error("Element not found: " + e.getMessage());
            test.fail("Element not found: " + e.getMessage());
        } catch (TimeoutException e) {
            logger.error("Timeout occurred while waiting for element: " + e.getMessage());
            test.fail("Timeout occurred while waiting for element: " + e.getMessage());
        } catch (Exception e) {
            logger.error("Unexpected error: " + e.getMessage());
            test.fail("Unexpected error: " + e.getMessage());
        }
    }

    @AfterTest
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
        extent.flush();
    }
}
