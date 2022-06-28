from selenium import webdriver
from app.Application import Application

__author__ = "Mehmet Engin Sacan"


"""
This file contains before and after actions for each scenario in the feature file.
"""


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
