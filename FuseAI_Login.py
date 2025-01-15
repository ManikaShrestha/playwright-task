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

         try:
            page.locator('xpath=//h4[contains(text(),"Studio Projects")]').wait_for(timeout=5000)
            print("Login Success")
        except Exception as e:
            print("Your username is invalid!", str(e))
            
        time.sleep(5)
        browser.close()

        browser.close()

test_login()

