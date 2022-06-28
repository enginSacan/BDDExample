from behave import given, when, then

__author__ = "Mehmet Engin Sacan"

"""
This file contains the step definition functions
"""


@given("Open page {url}")
def open_main_page(context, url):
    context.app.search_page.open_search_page(url)


@when("write {word} for search")
def search_page(context, word):
    context.app.search_page.search_word(word)


@when("go to site")
def go_to_site(context):
    context.app.search_page.go_to()
    context.app.company_page.check_company_page_loaded()


@when("check career link at the bottom")
def check_career(context):
    context.app.company_page.check_career_button()


@when("click {page} link")
def click_page(context, page):
    context.app.company_page.click_page(page)


@when("check the decription part in career page")
def description_check(context):
    return context.app.career_page.check_description()


@when("click {title} job")
def choose_job(context, title):
    context.app.career_page.choose_job(title)


@when("check error messages for application")
def error_message_check(context):
    context.app.job_page.check_error_messages()

@when("fill form with necessary fields and documents")
def fill_form(context):
    context.app.job_page.fill_all_form()
