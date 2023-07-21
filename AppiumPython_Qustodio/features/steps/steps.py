import os
import sys

from appium import webdriver
from behave import given, when, then, step
from time import sleep

PAGE_NAVIGATION_TIMER = 3
IDLE_TIMER = 2


@given('the app is launched')
def step_impl(context):
    try:
        context.HomePage.skip_on_board_page()
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@when(u'user performs "{Swipe_Direction}" swipe')
def step_impl(context, Swipe_Direction):
    context.HomePage.perform_swipe(Swipe_Direction)
    sleep(IDLE_TIMER)


@when(u'{searchedterm} is entered')
def step_impl(context, searchedterm):
    context.HomePage.input_searched_term(searchedterm)
    sleep(IDLE_TIMER)
    context.reddit_home_page.send_enter_key()
    sleep(PAGE_NAVIGATION_TIMER)


@then(u'should be able to see the next "{Screen_Name}" screen')
def step_impl(context, Screen_Name):
    assert context.HomePage.check_next_screen_is_displayed(Screen_Name) is True
    sleep(IDLE_TIMER)


@then(u'should be able to see the "{searchedterm}" results')
def step_impl(context, searchedterm):
    assert context.HomPage.check_searched_result_is_displayed(searchedterm) is True
    sleep(IDLE_TIMER)


@when(u'user performs a tap on "{ButtonName}" button')
def step_impl(context, ButtonName):
    context.HomePage.tap_on_the_item(ButtonName)
    sleep(PAGE_NAVIGATION_TIMER)


@when(u'user enter details on sign up screen "{username}", "{email}" and "{password}"')
def step_impl(context, username, email, password):
    context.HomePage.input_username_email_password(username, email, password)


@when(u'user performs a tap on submit button')
def step_impl(context, ButtonName = "Submit"):
    context.HomePage.tap_on_the_item(ButtonName)
    sleep(PAGE_NAVIGATION_TIMER)

@when(u'user taps on policy agreement')
def step_impl(context, ButtonName = "PolicyCheck"):
    context.HomePage.tap_on_the_item(ButtonName)
    sleep(PAGE_NAVIGATION_TIMER)


@then(u'user should be able to see welcome screen')
def step_impl(context):
    context.HomePage.check_next_screen_is_displayed('WelcomeScreen')


@then(u'user enter details on sign up screen "<username>" "<password>"')
def step_impl(context, username, password):
    context.HomePage.input_searched_term(username, password)
