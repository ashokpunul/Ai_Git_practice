from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto(
            "https://www.cricbuzz.com/",
            wait_until="domcontentloaded",
            timeout=30000
        )

        print("Page title:", page.title())
        print("Current URL:", page.url)

        page.wait_for_timeout(5000)

        print("Page loaded successfully")

        selector = "a[href*='/live-cricket-scores/']"
        score_cards = page.locator(selector)
        count = score_cards.count()

        print("Live score cards found:", count)

        if count > 0:
            for index in range(count):
                score_text = score_cards.nth(index).inner_text().strip()
                if score_text:
                    print(score_text)
        else:
            print("No live score cards were found on the page.")

        page.screenshot(path="cricbuzz.png", full_page=True)

    except Exception as e:
        print("ERROR:", type(e).__name__)
        print(e)

    finally:
        browser.close()