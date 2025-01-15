import time
from playwright.sync_api import sync_playwright

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto('https://globalstudio.fuse.ai/login')
        page.fill('input[type="text"]', 'testuser@email.com')
        page.fill('input[type="password"]', 'testuser')

        page.click('button[type="submit"]')

        page.wait_for_load_state('load')

        # Verify that the URL after login is correct
        if page.url == 'https://globalstudio.fuse.ai/':
            print("Login Success")
        else:
            print("Your username is invalid!")
        
        time.sleep(5)

        browser.close()

test_login()

