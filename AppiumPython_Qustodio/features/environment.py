import hashlib
import os
import sys

from appium import webdriver
import time
from utils.LaunchApp import *


IDLE_TIMER = 3

global gCWD, gSCREEN_SHOTS_PATH
gCWD = os.getcwd()
gSCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"


# Hooks
def before_all(context):
    context.config.setup_logging()
    start_driver(context)


def after_all(context):
    # TODO
    # uninstall the app on cloude device
    # context.driver.remove_app(context.config.userdata.get("app_uri"));
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    # start_activity()
    # Android ONLY
    # get_current_activity()
    pass


def after_scenario(context, scenario):
    # TODO
    pass


def after_feature(context, feature):
    cleanup_driver(context)


def before_step(context, step):
    pass


def after_step(context, step):
    if step.status == "failed":
        ts = time.time()
        st = time.ctime(ts)
        #screenshot_file = gSCREEN_SHOTS_PATH + step.name + "_" + st + ".png"
        time.sleep(IDLE_TIMER)
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
