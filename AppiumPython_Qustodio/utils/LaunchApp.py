from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import os
from Pages.HomePage import HomePage

CWD = os.getcwd()
SCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"

__driver_configs = {}


def start_driver(context):
    try:
        desired_capabilities = {
            "deviceName": "emulator-5554",
            "automationName": "uiautomator2",
            "platformName": "Android",
            "app": os.path.join(CWD, "apk/Kids_App_Qustodio_180.65.1.2.apk"),
            "appPackage": "com.qustodio.qustodioapp",
            "appActivity": "com.qustodio.qustodioapp.ui.splash.SplashScreenActivity"
        }

        context.driver = webdriver.Remote('http://127.0.0.1:4723', desired_capabilities)
        context.HomePage = HomePage(context.driver)
    except Exception as e:
        print("Exception in Launching app: ", e)

def cleanup_driver(context):
    context.driver.quit()



