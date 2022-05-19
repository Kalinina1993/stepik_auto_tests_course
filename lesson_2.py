""" ЧЕКБОКС, РАДИОБАТОН, МЕТОД GET_ATTRIBUTE"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import math
import time
from selenium.webdriver.support.ui import Select
import os

s = Service("/home/natasha/PycharmProjects/Stepik_Python/Automation_testing/chromedriver")
driver = webdriver.Chrome(service=s)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get("http://suninjuly.github.io/math.html")
    driver.find_element(By.ID, "answer").send_keys(calc(driver.find_element(By.ID, "input_value").text))

    driver.find_element(By.ID, "robotCheckbox").click()

    driver.find_element(By.ID, "robotsRule").click()

    driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(5)


finally:
    driver.quit()

try:
    driver.get(" http://suninjuly.github.io/get_attribute.html")
    driver.find_element(By.ID, "answer").send_keys(calc(driver.find_element(By.ID, "treasure").get_attribute("valuex")))

    driver.find_element(By.ID, "robotCheckbox").click()

    driver.find_element(By.ID, "robotsRule").click()

    driver.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button").click()
    time.sleep(5)


finally:
    driver.quit()

"""SELECT, ВЫПАДАЮЩИЕ СПИСКИ, SCROLL, ЗАГРУЗКА ФАЙЛОВ"""


try:
    driver.get("http://suninjuly.github.io/selects1.html")
    z = str(int(driver.find_element(By.ID, "num1").text) + int(driver.find_element(By.ID, "num2").text))
    Select(driver.find_element(By.TAG_NAME, "select")).select_by_visible_text(z)
    driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(5)

finally:
    driver.quit()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    driver.get("http://SunInJuly.github.io/execute_script.html")
    driver.find_element(By.ID, "answer").send_keys(calc(driver.find_element(By.ID, "input_value").text))
    driver.execute_script("window.scrollBy(0, 100);")
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(5)
finally:
    driver.quit()


try:
    driver.get("http://suninjuly.github.io/file_input.html")
    driver.find_element(By.NAME, "firstname").send_keys("Ross")
    driver.find_element(By.NAME, "lastname").send_keys("Galler")
    driver.find_element(By.NAME, "email").send_keys("Ilovedinousavrs@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(current_dir, "file1.txt")
    driver.find_element(By.ID, "file").send_keys(file)
    driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(5)
finally:
    driver.quit()

