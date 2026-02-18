# -*- coding: utf-8 -*-
import requests
import yfinance as yf
from bs4 import BeautifulSoup

def get_symbol_by_name(name):
    try:
        result = yf.Search(name, max_results=1)
        if result.quotes:
            return result.quotes[0]['symbol']
        else:
            return None
    except Exception:
        return None

def get_cik_from_name(name):
    try:
        url = "https://www.sec.gov/files/company_tickers.json"
        data = requests.get(url, headers={'User-Agent':'Your_Name@gmail.com'}).json()
        for company in data.values():
            if name.lower() in company['title'].lower():
                return str(company['cik_str']).zfill(10)
        return None
    except requests.exceptions.RequestException:
        return None

def get_recent_filings(cik):
    try:
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        response = requests.get(url, headers={'User-Agent':'Your_Name@gmail.com'})
        data = response.json()
        if "filings" not in data or "recent" not in data["filings"]:
            return None
        else:
            filings = data["filings"]["recent"]
        return filings
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to retrieve the last 10-K data: {e}")
        return None

def get_10_k(url):
    try:
        response = requests.get(url, headers={'User-Agent':'Your_Name@gmail.com'})
        return response.text
    except requests.exceptions.RequestException:
        return None

def get_total_value(text_elements):
    if not text_elements:
        print("Data not found in the document.")
        return

    for text_element in text_elements:
        row = text_element.find_parent('tr')
        if not row:
            continue
        cells = row.find_all('td')
        for cell in cells:
            value = cell.get_text(strip=True).replace(',', '').replace('$','').replace('(','').replace(')','')
            if value.replace('.', '', 1).replace('-','',1).isdigit():
              formatted_value = f"{float(value):,.0f}"
              print(f"${formatted_value} million dollars")
              return

def Finanicial_Question(soup):
    Question = input('Enter Your Financial Question: ').lower()


    revenue_texts = soup.find_all(string=lambda s: s and 'revenue' in s.lower())
    cost_texts = soup.find_all(string=lambda s: s and 'cost of revenue' in s.lower())
    expenses_texts = soup.find_all(string=lambda s: s and 'operating expense' in s.lower())
    net_income_texts = soup.find_all(string=lambda s: s and 'net income' in s.lower())
    cash_operating_texts = soup.find_all(string=lambda s: s and 'cash provided by operating activities' in s.lower())
    cash_investing_texts = soup.find_all(string=lambda s: s and 'cash used in investing activities' in s.lower())

    if 'revenue' in Question:
        get_total_value(revenue_texts)
    elif 'cost of revenues' in Question:
        get_total_value(cost_texts)
    elif 'operating expenses' in Question:
        get_total_value(expenses_texts)
    elif 'net income' in Question:
        get_total_value(net_income_texts)
    elif 'cash provided by operating activities' in Question:
        get_total_value(cash_operating_texts)
    elif 'cash used in investing activities' in Question:
        get_total_value(cash_investing_texts)
    else:
        print('Invalid Question')


def main():
    Company_name = input("Name of Company you're targeting: ")
    tinker = get_symbol_by_name(Company_name)

    if tinker is None:
        print("Symbol not found.")
        return
    cik = get_cik_from_name(Company_name)
    if cik is None:
        print("CIK not found.")
        return

    now = get_recent_filings(cik)
    if not now:
        print("No recent filings found.")
        return

    for f, acc, pr2 in zip(now["form"], now["accessionNumber"], now["primaryDocument"]):
        if f == "10-K":
            acc_node = acc.replace("-", "")
            url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc_node}/{pr2}"

            html_content = get_10_k(url)
            if not html_content:
                print("Failed to retrieve 10-K document.")
                return
            soup = BeautifulSoup(html_content, 'html.parser')

            Finanicial_Question(soup)
            break

if __name__ == "__main__":
    main()
