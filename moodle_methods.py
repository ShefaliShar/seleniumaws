import sys
from selenium import webdriver  # import selenium to the file
import moodle_locators as locators  # all variable take from moodle_locators file
from selenium.webdriver.chrome.service import Service
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # => add this for dropdown list
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# This method solves the "DeprecateWarning" error that occurs in Selenium 4 and above.
# 1. Comment out, or remove the previous method which was: driver = webdriver.Chrome('chromedriver.exe path')

# s = Service(executable_path='C://Users//GAURAV//PycharmProjects//pythonProject//chromedriver.exe')
# driver = webdriver.Chrome(service=s)

# create a variable , specify path to chromedriver.exe
# driver = webdriver.Chrome('C://Users//GAURAV//PycharmProjects//pythonProject//chromedriver.exe')


def setUp():
    print(f'Launch {locators.app} Application')
    print('********************-----------***************************')
    # make browser full screen
    driver.maximize_window()

    # Give browser up to 30 second to respond
    driver.implicitly_wait(30)

    # Navigate to Moodle website
    driver.get(locators.moodle_url)

    # check that Moodle URl and homepage title
    if driver.current_url == locators.moodle_url and driver.title == locators.moodle_home_page_title:
        print('Yay!!', locators.app, 'Launched Successfully')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)

    else:
        print('Moodle did not launch.Check your code application')
        print(f'Current URL: {driver.current_url}\n Page tile: {driver.title}')
        tearDown()


def tearDown():
    if driver is not None:
        print('-----------------------------------****-----------------------')
        print('The test Completed at:', datetime.datetime.now())
        sleep(2)
        driver.close()
        driver.quit()

# login to Moodle
# def log_in():
#     if driver.current_url == locators.moodle_url:
#         driver.find_element(By.LINK_TEXT, 'Log in').click()
#         if driver.current_url == locators.moodle_login_page_url:   # check we are on login page
#             print(f'{locators.app} Login Page is displayed!')
#             print('----------------------------****************------------------------------')
#             sleep(0.25)
#             driver.find_element(By.ID, 'username').send_keys(locators.admin_username)
#             sleep(0.25)
#             driver.find_element(By.ID, 'password').send_keys(locators.admin_password)
#             sleep(0.25)
#             driver.find_element(By.ID, 'loginbtn').click()  # method1 using ID
#             # ------------------locators XPATH practice ------------------------------------------------
#             # driver.find_element(By.XPATH, '//button[contains().,"Log in"]').click()  # method2 using XPATH with the TEXT
#             # driver.find_element(By.XPATH, '//button[contains(@id, "loginbtn")]').click()  # method 3 using XPATH with specific ID
#             # driver.find_element(By.XPATH, '//button[@id="loginbtn"]').click()  # method4 by XPATH without contains
#             # driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()  # method5 by XPATH without button * means any element
#             # driver.find_element(By.CSS_SELECTOR, 'button[id="loginbtn"]').click() # method1 CSS_SELECTOR
#             # driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()  # method2 CSS_SELECTOR
#             # ------------------------------------------------------------------------------------------------------------
#             # validate we are on dashboard
#             if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
#                 assert driver.current_url == locators.moodle_dashboard_url  # assert will silently check if it is true
#                 assert driver.title == locators.moodle_dashboard_page_title
#                 print(f'Login Successful!! {locators.app} Dashboard is Displayed - Page title:', driver.title)
#             else:
#                 print('We are not at the Dashboard Page. Please check your Code!! ')


def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_page_url:   # check we are on login page
            print(f'{locators.app} Login Page is displayed!')
            print('----------------------------****************------------------------------')
            sleep(0.25)
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID, 'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()  # method1 using ID
            # ------------------locators XPATH practice ------------------------------------------------
            # driver.find_element(By.XPATH, '//button[contains().,"Log in"]').click()  # method2 using XPATH with the TEXT
            # driver.find_element(By.XPATH, '//button[contains(@id, "loginbtn")]').click()  # method 3 using XPATH with specific ID
            # driver.find_element(By.XPATH, '//button[@id="loginbtn"]').click()  # method4 by XPATH without contains
            # driver.find_element(By.XPATH, '//*[@id="loginbtn"]').click()  # method5 by XPATH without button * means any element
            # driver.find_element(By.CSS_SELECTOR, 'button[id="loginbtn"]').click() # method1 CSS_SELECTOR
            # driver.find_element(By.CSS_SELECTOR, 'button#loginbtn').click()  # method2 CSS_SELECTOR
            # ------------------------------------------------------------------------------------------------------------
            # validate we are on dashboard
            if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
                assert driver.current_url == locators.moodle_dashboard_url  # assert will silently check if it is true
                assert driver.title == locators.moodle_dashboard_page_title
                print(f'Login Successful!! {locators.app} Dashboard is Displayed - Page title:', driver.title)
            else:
                print('We are not at the Dashboard Page. Please check your Code!! ')


def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(.,"Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print('----------------------------*********------------------------------------')
        print(f'Logout Successful! at {datetime.datetime.now()}')


def create_new_user():
    # navigate to Site Administration
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # Validate we are at add a new user page
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    assert driver.title == locators.moodle_add_new_user_page_title
    print(f'----Navigate to Add a New User Page-- Page Title: *** {locators.moodle_add_new_user_page_title} ****')
    sleep(0.25)
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    # select an action from drop down list
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    sleep(0.25)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(locators.country)
    sleep(0.25)
    Select(driver.find_element(By.ID, 'id_timezone')).select_by_visible_text('America/Vancouver')
    sleep(0.25)
    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)
    sleep(0.25)
    # upload picture
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()  # click an arrow
    sleep(0.25)
    # navigate to image
    # --------------------------------------------------------------------------
    # driver.find_element(By.LINK_TEXT, 'Server files').click()
    # driver.find_element(By.LINK_TEXT, 'sl_Frozen').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'sl_How to build a snowman').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'Course image').click()
    # sleep(0.25)
    # driver.find_element(By.LINK_TEXT, 'gieEd4R5T.png').click()
    # sleep(0.25)
    # --------------------------------------------------------------------------
    # replace previous code for selecting an image with loop below
    img_path = ['Server files', 'sl_Frozen', 'sl_How to build a snowman', 'Course image', 'gieEd4R5T.png']
    for p in img_path:
        driver.find_element(By.LINK_TEXT, p).click()
        sleep(0.25)

    # Select Radio button
    # driver.find_element(By.XPATH, '//input[@value="4"]').click()  # option1
    driver.find_element(By.XPATH, '//label[contains(.,"Create an alias/shortcut to the file")]').click()  # option2
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Select this file")]').click()
    sleep(0.25)
    # Picture description
    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.pic_desc)
    # populate additional names
    driver.find_element(By.LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.last_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.middle_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.first_name)
    sleep(0.25)
    # populate interests
    driver.find_element(By.LINK_TEXT, 'Interests').click()

    for tag in locators.list_of_interests:
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag) -method1
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + Keys.ENTER) -method2
        driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(tag + "\n")  # method3
        sleep(0.25)
        # driver.find_element(By.XPATH, '//input[contains(@id, "form_autocomplete_input")]').send_keys(Keys.ENTER) -method1
        sleep(0.25)

    # populate optional
    driver.find_element(By.LINK_TEXT, 'Optional').click()
    for i in range(len(locators.list_opt)):
        opt, ids, val = locators.list_opt[i], locators.list_ids[i], locators.list_val[i]
        # print(f'Populate {opt}')
        driver.find_element(By.ID, ids).send_keys(val)
        sleep(0.25)
    # --------------------Press Submit Button-------------------------

    driver.find_element(By.ID, 'id_submitbutton').click()
    sleep(0.25)
    print(f'-------New USer "{locators.new_username}/{locators.new_password}, {locators.email}" is added---------')

###########################################################################################################

def search_user():
    # check we are on the users main page
    if driver.current_url == locators.moodle_user_main_page and driver.title == locators.moodle_user_main_page_title:
        assert driver.find_element(By.LINK_TEXT, 'Browse list of users').is_displayed()
        print(f'\'Browse list of user page\' is displayed !!')
        sleep(0.25)
        # check we can search user by email
        print(f'-----------------Search for user by email address: {locators.email}-----')
        driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
        sleep(0.25)
        if driver.find_element(By.XPATH, f'//td[contains(.,"{locators.email}")]'):
            print(f'-------User : {locators.email} is found!--------\n')
            logger('created')


def check_new_user_can_login():
    if driver.title == locators.moodle_dashboard_page_title and driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(.,"{locators.full_name}")]').is_displayed():
            print(f'-------- User with full name : {locators.full_name} is displayed ----\n')
            # logger('created')


def delete_user():
    driver.find_element(By.XPATH, '//span[contains(.,"Site administration")]').click()
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.25)

    search_user()
    driver.find_element(By.XPATH, '//*[contains(@title,"Delete")]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//button[contains(.,"Delete")]').click()
    sleep(0.25)
    print(f'**************New user deleted. Username: {locators.new_username} and Email: {locators.email}*************')
    logger('deleted')


# logger
def logger(action):
    # create variable to store the file content
    old_instance = sys.stdout
    log_file = open('message.log', 'a')  # open log file and append a record
    sys.stdout = log_file
    print(f'{locators.email}\t'
          f'{locators.new_username}\t'
          f'{locators.new_password}\t'
          f'{datetime.datetime.now()}\t'
          f'{action}')
    sys.stdout = old_instance
    log_file.close()


# ------ Create new user -----
# setUp()
# print('here we are going to add new test user')
# log_in(locators.admin_username, locators.admin_password)  # Login as admin
# create_new_user()
# search_user()
# log_out()
# ------ Login as new user-----------
# log_in(locators.new_username, locators.new_password)
# check_new_user_can_login()
# logger('created')
# log_out()
# --------Delete the new user--------------------
# log_in(locators.admin_username, locators.admin_password)
# delete_user()
# log_out()
# ------------------------------------------------------------
# tearDown()
