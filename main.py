import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import argparse
import json

def get_value(course_name, course_num):
    
    Chrome_options = webdriver.ChromeOptions()
    Chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=Chrome_options)

    browser.get("https://classes.uwaterloo.ca/under.html")

    options = browser.find_element(By.NAME, value="subject")

    search_string = "//option[@value='" + course_name + "']"
    option = options.find_element(By.XPATH, search_string)
    option.click()

    text_box = browser.find_element(By.NAME, value="cournum")
    text_box.send_keys(course_num)

    submit_button = browser.find_element(By.XPATH, "//input[@value='Search']")
    submit_button.click()
    
    browser.implicitly_wait(2)
    value =  browser.find_element(locate_with(By.XPATH, "//table")).get_attribute('outerHTML')
    df  = pd.read_html(value)
    df = pd.DataFrame(df[-1])
    tot = df.loc[0, 'Enrl Tot']
    cap = df.loc[0, 'Enrl Cap']
    
    val = 0
    if tot < cap:
        val = 1
    
    browser.quit()
    return val

if __name__ == "__main__":
    
    # Command line arguments
    parser = argparse.ArgumentParser(description='Check for an open class')
    
    # Parameters are defined
    params_file = "params.json"
    with open(params_file) as paramfile:
        param = json.load(paramfile)
    
    url = param["DISCORD_WEBHOOK_URL"]
    course_name = param["course_name"]
    course_num = param["course_num"]
    
    while(True):
        out = get_value(course_name, course_num)
        if out == 1:
            payload = {'content': 'There is an empty space in the class of {} {}!'.format(course_name, course_num)}
            response = requests.post(url, json=payload)
            print(response)
            break
            