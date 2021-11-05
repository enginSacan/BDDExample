from selenium import webdriver
from app.Application import Application


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()
