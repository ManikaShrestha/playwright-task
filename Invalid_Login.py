import time
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://the-internet.herokuapp.com/login')
        page.fill('input[name="username"]', 'invaliduser')
        page.fill('input[name="password"]', 'invalidpassword')

        page.click('button[type="submit"]')

        page.wait_for_load_state('load')

        # Verify that the URL after login is correct
        if page.url == 'https://the-internet.herokuapp.com/secure':
            print("You logged into a secure area!")
        else:
            print("Your username is invalid!")
        
        time.sleep(5)

        browser.close()

test_login()

