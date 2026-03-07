# 📈 10-K Financial Analyzer

> A Python tool that retrieves and parses key financial figures directly from SEC 10-K filings — just enter a company name and ask your question.

---

## 📌 Overview

Instead of manually digging through hundreds of pages of SEC filings, this tool automates the entire process. Enter a company name, ask a financial question, and get the exact figure pulled straight from the official regulatory document.

---

## ✨ Features

- 🔍 **Company Resolution** — Converts a plain company name into its stock ticker (via yfinance) and SEC Central Index Key (via SEC's ticker database)
- 📂 **SEC EDGAR Integration** — Fetches the most recent 10-K filing directly from `data.sec.gov`
- 🧹 **Smart Parsing** — Uses BeautifulSoup to navigate complex HTML tables and locate specific financial line items
- 💰 **Clean Output** — Automatically strips formatting characters (`$`, `,`, brackets) and returns a clean numeric value

---

## 🔧 Tech Stack

| Tool | Role |
|------|------|
| Python | Core language |
| `requests` | SEC EDGAR API communication |
| `BeautifulSoup (bs4)` | HTML parsing of 10-K documents |
| `yfinance` | Company name → ticker resolution |

---

## 🚀 Usage

```bash
pip install requests yfinance beautifulsoup4
python financial_analyzer.py
```

```
Name of Company you're targeting: Microsoft

Enter Your Financial Question: Net Income

> $101,832 million dollars
```

### Supported Questions

| Question | Data Extracted |
|----------|---------------|
| `revenue` | Total Revenue |
| `cost of revenues` | Cost of Revenue |
| `operating expenses` | Total Operating Expenses |
| `net income` | Net Income |
| `cash provided by operating activities` | Operating Cash Flow |
| `cash used in investing activities` | Investing Cash Flow |

---

## ⚙️ How It Works

1. Resolves the company name to a **ticker symbol** and **CIK** (SEC identifier)
2. Calls the `data.sec.gov` submissions API to find the latest **10-K filing URL**
3. Downloads the full HTML content of the filing
4. Scans for keyword matches (e.g. "Net Income", "Revenue") in the document
5. Finds the corresponding table row and extracts the **first clean numeric value**

---

## 📁 Files

| File | Description |
|------|-------------|
| `financial_analyzer.py` | Main script |

---

## 🔮 Future Improvements

- Web interface for interactive queries
- Visualization dashboard for financial trends
- Expanded support for additional filing types (10-Q, 8-K)

---

*Built with Python + SEC EDGAR. No paid APIs, no subscriptions — all data is publicly available.*
