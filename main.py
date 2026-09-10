import subprocess
import sys
import os

NUMBER_OF_BOTS = 40
KAHOOT_ID = 151364

def main():
    for i in range(999):
        try: 
            os.remove(f"scraper{i}.py")
        except FileNotFoundError:
            pass

    for i in range(NUMBER_OF_BOTS):
        with open(f"scraper{i}.py", "w") as f:
                f.write(
    rf'''
    from playwright.sync_api import sync_playwright
    import time
    BotNumber = {i}
    KAHOOT_ID = {KAHOOT_ID}
    print(rf"Running scraper{i}.py")
    with sync_playwright() as pw:
        browser = pw.chromium.launch(channel="chrome")
        page = browser.new_page()
        page.goto("https://kahoot.it/")

        textbox = page.get_by_role("textbox")
        textbox.fill(f"{KAHOOT_ID}")
        page.get_by_role("button", name="Join").click()
        time.sleep(2)

        username = page.get_by_role("textbox")
        username.fill(f"scraper{i}")
        page.get_by_role("button", name="OK, go!").click()

        print(f"BotNumber{i} joined")

        time.sleep(30)

        browser.close()''')

    for i in range(NUMBER_OF_BOTS):
        subprocess.Popen([f"{sys.executable}", f"scraper{i}.py"])

if __name__ == "__main__":
    main()