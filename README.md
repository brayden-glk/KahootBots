# Kahoot Bot Scraper

A Python automation script that launches multiple Chromium browser instances concurrently and automates the process of joining a Kahoot game.

The script uses **Playwright** for browser automation and Python's **multiprocessing** module to run multiple bots simultaneously.

> **Note:** This project is intended for learning and controlled testing/automation. Do not use it to disrupt real Kahoot games or interfere with other users.

## Features

* Launches multiple browser instances concurrently
* Automatically navigates to Kahoot
* Enters a specified Kahoot game PIN
* Generates a unique username for each bot
* Automatically joins the game
* Uses multiprocessing to run bots in parallel
* Automatically closes each browser after a specified period

## Requirements

* Python 3.8+
* Google Chrome
* Playwright

Install Playwright:

```bash
pip install playwright
```

Install the required Playwright browser dependencies:

```bash
playwright install
```

The script currently launches the installed Chrome browser using:

```python
pw.chromium.launch(channel="chrome")
```

## Configuration

At the top of the script, you can change the number of bots and Kahoot game ID:

```python
NUMBER_OF_BOTS = 30
KAHOOT_ID = 729004
```

### `NUMBER_OF_BOTS`

Controls how many separate processes/browser instances are launched.

```python
NUMBER_OF_BOTS = 3
```

### `KAHOOT_ID`

The game PIN that each bot attempts to join.

```python
KAHOOT_ID = 000000
```

## How It Works

The program starts in `main()`.

For each bot, a separate `multiprocessing.Process` is created:

```python
p = multiprocessing.Process(
    target=scraper,
    args=(i,)
)
```

Each process runs the `scraper()` function independently.

The function then:

1. Starts Playwright.
2. Launches Chrome.
3. Opens `kahoot.it`.
4. Enters the configured game PIN.
5. Clicks the **Join** button.
6. Enters a username such as `scraper0`, `scraper1`, etc.
7. Clicks **OK, go!**
8. Waits for 30 seconds.
9. Closes the browser.

After all processes have been started, `main()` waits for them to finish using:

```python
p.join()
```

## Running the Script

Save the script as something such as:

```text
kahoot_bots.py
```

Then run:

```bash
python kahoot_bots.py
```

You should see output similar to:

```text
Running Bot Number 0
Running Bot Number 1
Running Bot Number 2
...
Bot Number 0 joined
Bot Number 1 joined
Bot Number 2 joined
...
```

## Project Structure

A minimal project can look like:

```text
kahoot-bot/
├── kahoot_bots.py
├── README.md
└── requirements.txt
```

A `requirements.txt` file could contain:

```text
playwright
```

Then dependencies can be installed with:

```bash
pip install -r requirements.txt
playwright install
```

## Technical Notes

### Why multiprocessing?

Browser automation is relatively resource-intensive. Each bot needs its own Playwright browser context/process, so the script uses Python's `multiprocessing` module to run multiple bots concurrently.

### Why is Playwright imported inside `scraper()`?

```python
def scraper(bot_number):
    from playwright.sync_api import sync_playwright
```

The import occurs inside the child process rather than at module level. This can help avoid issues with multiprocessing and browser automation, particularly on platforms that use the `spawn` multiprocessing method.

### Browser resources

Running many Chrome instances simultaneously can consume significant CPU and RAM. Increasing:

```python
NUMBER_OF_BOTS = 30
```

substantially increases resource usage.

## Limitations

This script currently uses fixed delays:

```python
time.sleep(2)
time.sleep(30)
```

These assume that the page has finished loading within the specified time. A more robust implementation would use Playwright's built-in waiting mechanisms instead of relying primarily on fixed sleeps.

The script also assumes that Kahoot's current UI and accessibility labels remain unchanged.

## Disclaimer

This project is for educational purposes, particularly for learning:

* Python multiprocessing
* Browser automation
* Playwright
* Process management
* Concurrent execution

Only use it in environments where you have permission to automate and where automated participants are allowed.
