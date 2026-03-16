import requests
import os
from dotenv import load_dotenv
import csv
from datetime import datetime


load_dotenv()
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")

if not POLYGON_API_KEY:
    raise ValueError("POLYGON_API_KEY not found in environment variables. Please set it in a .env file or your environment.")

LIMIT = 10
DS = '2026-03-14'


def run_stock_job():
    DS = datetime.now().strftime('%Y-%m-%d')
    url = f'https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}'
    response = requests.get(url)
    tickers = []

    data = response.json()
    for ticker in data['results']:
        ticker['ds'] = DS
        tickers.append(ticker)

    while 'next_url' in data:
        print('requesting next page', data['next_url'])
        response = requests.get(data['next_url'] + f'&apiKey={POLYGON_API_KEY}')
        data = response.json()
        print(data)
        for ticker in data['results']:
            ticker['ds'] = DS
            tickers.append(ticker)

    example_ticker =  {'ticker': 'ZWS', 
        'name': 'Zurn Elkay Water Solutions Corporation', 
        'market': 'stocks', 
        'locale': 'us', 
        'primary_exchange': 'XNYS', 
        'type': 'CS', 
        'active': True, 
        'currency_name': 'usd', 
        'cik': '0001439288', 
        'composite_figi': 'BBG000H8R0N8', 	'share_class_figi': 'BBG001T36GB5', 	
        'last_updated_utc': '2025-09-11T06:11:10.586204443Z',
        'ds': '2025-09-25'
        }

    fieldnames = list(example_ticker.keys())

    # Load to CSV
    output_csv = 'tickers.csv'
    with open(output_csv, 'w', newline='', ) as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for ticker in tickers:
            row = {key: ticker.get(key, '') for key in fieldnames}
            writer.writerow(row)

if __name__ == '__main__':
    run_stock_job()