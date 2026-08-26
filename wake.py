import os
from playwright.sync_api import sync_playwright

URL = os.environ["APP_URL"]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(URL, timeout=90000)
    page.wait_for_timeout(5000)

    btn = page.get_by_text("Yes, get this app back up!")
    if btn.count() > 0:
        print("앱이 자고 있어서 깨우는 중...")
        btn.first.click()
        page.wait_for_timeout(45000)
    else:
        print("앱이 이미 깨어 있음")

    page.wait_for_timeout(20000)
    page.screenshot(path="result.png")
    print("완료:", page.title())
    browser.close()
