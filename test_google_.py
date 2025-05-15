
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_should_Navigate_to_Google_and_verify_valid_title():

    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")
    assert driver.title == "Google"

    driver.quit()

def test_Perform_a_search_with_a_keyword_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")

    search_text_box = driver.find_element(By.NAME, "q")
    search_text_box.send_keys("selenium")
    search_text_box.send_keys(Keys.ENTER)

    WebDriverWait(driver, 40).until(EC.title_contains("selenium"))
    assert "selenium" in driver.title.lower()

    driver.quit()

def test_Open_the_first_link_in_selenium_page_and_verify_that_the_URL_is_of_seleniumdev():

    driver = webdriver.Chrome()
    driver.get("https://www.google.co.in/")


    search_text_box = driver.find_element(By.NAME, "q")
    search_text_box.send_keys("selenium")
    search_text_box.send_keys(Keys.ENTER)

    WebDriverWait(driver, 30).until(EC.title_contains("selenium"))
    assert "selenium" in driver.title.lower()


    first_result = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div#search h3"))
    )
    first_result.click()

    WebDriverWait(driver, 30).until(EC.url_contains("selenium.dev"))
    assert "selenium.dev" in driver.current_url ==("https://www.selenium.dev/")
    
    driver.quit()































