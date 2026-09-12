import multiprocessing

NUMBER_OF_BOTS = 30 
KAHOOT_ID = 729004

def scraper(bot_number):
    from playwright.sync_api import sync_playwright
    import time
    print(rf"Running Bot Number {bot_number}")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome")
        page = browser.new_page()
        page.goto("https://kahoot.it/")

        textbox = page.get_by_role("textbox")
        textbox.fill(f"{KAHOOT_ID}")
        page.get_by_role("button", name="Join").click()
        time.sleep(2)

        username = page.get_by_role("textbox")
        username.fill(f"scraper{bot_number}")
        page.get_by_role("button", name="OK, go!").click()

        print(f"Bot Number {bot_number} joined")

        time.sleep(30)

        browser.close()

def main():
    processes = []

    for i in range(NUMBER_OF_BOTS):
        p = multiprocessing.Process(target=scraper, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

if __name__ == "__main__":
    main()