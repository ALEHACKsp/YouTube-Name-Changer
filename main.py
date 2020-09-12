import os
import time

import requests
from selenium import webdriver, common

os.system('cls && title [YouTube Username Changer]')
CHANNEL_URL = input('[>] YouTube Channel URL: ')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 900)
driver.get('https://myaccount.google.com/u/0/name')

print('[!] Please log in...')
logged_in = False


def clear_first_name():
    # Clears the first name field
    driver.find_element_by_xpath(
        '/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div[2]/div[1]/div/div/label/input'
    ).clear()


while not logged_in:
    try:
        clear_first_name()
    except common.exceptions.NoSuchElementException:
        continue
    driver.set_window_position(-10000, 0)
    print('[!] Successfully logged in.\n')
    logged_in = True

while True:
    try:
        subscribers = requests.get(CHANNEL_URL).text.split(
            'subscriberCountText":{"runs":[{"text":"'
        )[1].split(' ')[0]
    except IndexError:
        subscribers = '0'

    if logged_in is None:
        clear_first_name()
    else:
        logged_in = None

    # Clears the surname field
    driver.find_element_by_xpath(
        '/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div[2]/div[2]/div/div/label/input'
    ).clear()

    # Edits first name
    driver.find_element_by_xpath(
        '/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div[2]/div[1]/div/div/label/input'
    ).send_keys('I have')

    # Edits surname
    driver.find_element_by_xpath(
        '/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div[2]/div[2]/div/div/label/input'
    ).send_keys(f'{subscribers} subscribers')

    # Updates profile settings
    driver.find_element_by_xpath(
        '/html/body/c-wiz/div/div[3]/c-wiz/div/div[2]/div/div[2]/div[4]/div[2]/div/div/button/div[2'
        ']'
    ).click()
    print(f'[!] Updated YouTube Channel name | Subscribers: {subscribers}')

    # For rate limit purposes waiting
    seconds = 60
    while seconds >= 0:
        os.system(f'title [YouTube Username Changer] - Seconds remaining: {seconds}')
        seconds -= 1
        time.sleep(1)
