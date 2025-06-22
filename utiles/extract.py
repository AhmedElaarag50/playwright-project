from playwright.sync_api import sync_playwright
import time
def extract_html_from_url(url, element):
    with sync_playwright() as p:
        brouser = p.chromium.launch(headless=False)
        page = brouser.new_page()
        page.goto(url=url)
        page.wait_for_load_state("networkidle")
        prev_height = 0
        while True:
            current_height = page.evaluate('() => document.body.scrollHeight')
            page.evaluate("() => window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1)
            if current_height == prev_height:
                break
            prev_height = current_height
        page.wait_for_load_state('domcontentloaded')
        page.wait_for_selector(element)
        html = page.inner_html('body')
        return(html)