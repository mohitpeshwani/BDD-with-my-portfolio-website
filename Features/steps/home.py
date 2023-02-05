from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I go to the website')
def home_page(context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.driver.get("https://mohitpeshwani.github.io/crazyprogrammer/")


@when('Looking for the logo in the header')
def logo(context):
    context.driver.find_element(By.CSS_SELECTOR, "img[src='images/logo1.png'][width='150']").is_displayed()

@when('Menu bar in desktop mode')
def menu_bar(context):
    context.driver.find_element(By.ID,"main-nav").is_displayed()

@then("verifying wheather the buttons {items}")
def menu_items(context,items):
    if(items.lower()=="home"):
        context.driver.find_element(By.LINK_TEXT,"HOME").click()
        assert "#" in context.driver.current_url, " Home menu is\'t working fine"
    elif (items.lower() == "about"):
        context.driver.find_element(By.LINK_TEXT, "ABOUT").click()
        assert "#about" in context.driver.current_url, " Home menu is\'t working fine"
    elif (items.lower() == "blogs"):
        context.driver.find_element(By.LINK_TEXT, "BLOGS").click()
        assert "#blog" in context.driver.current_url, " Home menu is\'t working fine"
    elif (items.lower() == "services"):
        context.driver.find_element(By.LINK_TEXT,"SERVICES").is_displayed()
        assert "#" in context.driver.current_url, " Home menu is\'t working fine"
