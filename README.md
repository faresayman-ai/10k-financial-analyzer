## 10-K Financial Analyzer 📈

This Python-based tool automates the retrieval and parsing of financial data from SEC 10-K filings. By entering a company name and a specific financial metric, users can extract key figures directly from official regulatory documents without manual searching.

## Features

* Converts a plain-text company name into its official Stock Symbol using yfinance and its SEC Central Index Key (CIK) via the SEC's ticker database.
* Fetches the most recent filings directly from the SEC EDGAR servers.
* Uses BeautifulSoup to navigate complex HTML tables within 10-K documents to locate specific financial line items.
* Automatically strips formatting characters (like $, ,, or brackets) to provide a clean numerical value.

## How It Works ?

* The script searches for the company's ticker and CIK to ensure it targets the correct legal entity.
* It accesses the data.sec.gov submissions API to find the URL for the most recent 10-K (Annual Report).
* The tool downloads the full HTML content of the filing and scans for keywords like "Net Income" or "Revenue".
* Once the relevant table row is found, it identifies the first numeric value and formats it for the user.

## Tech

* Language: Python
* requests library : For API communication with the SEC.
* BeautifulSoup (bs4): For parsing 10-K HTML structure.
* yfinance library: For resolving company names to tickers.

## Usage Example

$ python financial_analyzer.py 

Name of Company you're targeting: Microsoft

Enter Your Financial Question: Net Income ?

> $101,832 million dollars


## Future Improvements

* Web interface for interactive queries
* Visualization dashboard for financial trends
* Expanded support for additional filing types
