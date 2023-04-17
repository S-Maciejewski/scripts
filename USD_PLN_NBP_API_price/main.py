import csv
import requests
from datetime import datetime

INPUT_FILE = 'dates.csv'
OUTPUT_FILE = 'dates_prices.csv'


def get_usd_pln_rate(date):
    url = f'http://api.nbp.pl/api/exchangerates/rates/a/usd/{date}/?format=json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'][0]['mid']
    else:
        print(f'Error fetching rate for {date}')
        return None

def main():
    with open(INPUT_FILE, 'r') as infile, open(OUTPUT_FILE, 'w', newline='') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        csv_writer.writerow(['date', 'price'])

        for row in csv_reader:
            date_str = row[0]
            try:
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                price = get_usd_pln_rate(date)
                if price is not None:
                    csv_writer.writerow([date_str, price])
                    
            except ValueError:
                print(f'Invalid date format: {date_str}')

if __name__ == '__main__':
    main()
    print(f'{OUTPUT_FILE} generated')