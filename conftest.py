from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('D:\\chromedriver.exe')
   pytest.driver.set_window_size(1600, 1200)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

