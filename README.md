
# 🎮 Playwright Project: Web Scraper for Steam Specials

This project is a web scraper built using [Playwright](https://playwright.dev/python/) and [Selectolax](https://github.com/lexbor/selectolax) to extract promotional game data from the Steam Store or any similar site. It programmatically navigates the page, extracts the required HTML content, parses it, and saves structured data into a CSV file.

## 🚀 Features

- Automates browser interactions using Playwright.
- Extracts specific HTML sections using custom CSS selectors.
- Parses game information and processes raw attributes.
- Saves cleaned data as a structured CSV file.
- Modular and configurable setup.

## 🧠 Project Structure

```
playwright-project/
│
├── main.py                  # Main entry point for scraping logic
├── config/
│   └── tools.py             # Contains utility to load configuration for scraping
├── utiles/
│   ├── extract.py           # Extracts HTML content using Playwright
│   ├── parse.py             # Parses HTML nodes based on given schema
│   └── process.py           # Cleans and transforms parsed data
├── requirements.txt         # Python dependencies
└── 2025-06-22_extract.csv   # Sample output file
```

## ⚙️ Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AhmedElaarag50/playwright-project.git
    cd playwright-project
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Install Playwright browsers**:
    ```bash
    playwright install
    ```

## ▶️ Run the Project

```bash
python main.py
```

Make sure your `config/tools.py` defines the correct target URL and CSS selectors.

## 📂 Output

The extracted data will be saved to a file named like: `YYYY-MM-DD_extract.csv`.

## 📌 Technologies Used

- Python 3.10+
- Playwright (sync API)
- Selectolax (HTML parsing)
- CSV handling
- Custom configuration system

## 🧩 Customization

You can change:
- The target URL
- The container and item selectors (in the config)
- Output formatting

## 📃 License

This project is licensed under the MIT License.

---

> Developed with ❤️ by Ahmed Salim ([@AhmedElaarag50](https://github.com/AhmedElaarag50))
