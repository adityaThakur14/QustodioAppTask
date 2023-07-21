import logging
import re
import sys
from time import sleep

from selenium.webdriver.common.by import By
from utils.base_page import BasePage

logger = logging.getLogger('behaving')


class HomePage(BasePage):
    # home page
    login_button_loc = (By.ID, "com.qustodio.qustodioapp:id/loginText")
    sign_up_button_loc = (By.ID, "com.qustodio.qustodioapp:id/signupButton")
    submit_button_loc = (By.ID, "com.qustodio.qustodioapp:id/button")
    greeting_message_loc = (By.ID, "com.qustodio.qustodioapp:id/title")
    policy_agreement_loc = (By.ID, "com.qustodio.qustodioapp:id/privacyPolicyCheck")

    # Alert message modal

    alert_msg_yes_button_loc = (By.ID, "Pages:id/button1")
    alert_msg_no_button_loc = (By.ID, "Pages:id/button2")

    # Searched result list
    search_screen_onboarding = (By.ID, "com.qustodio.qustodioapp:id/image")
    search_screen_welcomescreen = (By.ID, "com.qustodio.qustodioapp:id/titleText")
    search_username_loc = (By.ID, "com.qustodio.qustodioapp:id/idUserNameInputEditText")
    search_email_loc = (By.ID, "com.qustodio.qustodioapp:id/idUserEmailInputEditText")
    search_password_loc = (By.ID, "com.qustodio.qustodioapp:id/idUserPasswordInputEditText")
    search_results_loc = (By.CLASS_NAME, "Pages.widget.RelativeLayout")



    def skip_on_board_page(self):

        if self.is_element_found(*self.greeting_message_loc) == True:
            pass
        else:
            self.fail("STDOUT: Can't find on board page. \n")
        return

    def input_username_email_password(self, username, email, password):
        if self.is_element_found(*self.search_username_loc) == True:
            self.send_keys(username, *self.search_username_loc)
            self.send_keys(email, *self.search_email_loc)
            self.send_keys(password, *self.search_password_loc)
        else:
            self.fail("STDOUT: Can't find search field. \n")
        return

    def input_searched_term(self, searched_term):
        if self.is_element_found(*self.search_field_loc) == True:
            self.send_keys(searched_term, *self.search_field_loc)
        else:
            self.fail("STDOUT: Can't find search field. \n")
        return

    def perform_swipe(self, swipe_direction):
        if swipe_direction == "Left":
            self.right_to_left_swipe()
        return

    def check_next_screen_is_displayed(self, screen_name):
        if screen_name == "Onboarding":
            if self.is_element_found(*self.search_screen_onboarding) == True:
                return True
        elif screen_name == "WelcomeScreen":
            if self.is_element_found(*self.search_screen_welcomescreen) == True:
                return True
        else:
            return False

    def check_searched_result_is_displayed(self, searched_term):
        names_array = self.fetch_elements_name(*self.search_results_name_loc)
        if names_array == None:
            self.fail("STDOUT: Can't find searched result: %s. \n" % searched_term)
            return False
        for i in range(names_array.__len__()):
            result_name = names_array[i]
            if searched_term == result_name[2:]:
                return True
        self.fail("STDOUT: Can't find searched result: %s. \n" % searched_term)
        return False


    def tap_on_the_item(self,itemname):
        if itemname == 'GetStarted':
            self.find_element(*self.sign_up_button_loc).click()
        elif itemname == 'Submit':
            self.find_element(*self.submit_button_loc).click()
        elif itemname == 'PolicyCheck':
            self.find_element(*self.policy_agreement_loc).click()
        else:
            return False



