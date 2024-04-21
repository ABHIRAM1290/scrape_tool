import csv
import requests
from bs4 import BeautifulSoup

def scrape_yellowpages(base_url):
    with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Location', 'City', 'P.O. Box', 'Phone', 'Mobile', 'Company Page Link', 'Logo URL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        page_num = 1
        while True:
            url = f"{base_url}?page={page_num}"
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to fetch page {page_num}. Status code: {response.status_code}")
                break

            soup = BeautifulSoup(response.content, 'html.parser')

            businesses = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
            if not businesses:
                print("No more businesses found.")
                break

            for business in businesses:
                name = business.find('h5', class_='item-title').text.strip()
                location = business.find('p', class_='address').text.strip()
                city = business.find('span', class_='city').text.strip()
                pobox = business.find('span', class_='pobox').text.strip()
                phone = business.find('span', class_='phone').text.strip()
                mobile = business.find('span', class_='mobile').text.strip()
                company_page_link = business.find('a', class_='view-more').get('href')
                logo_url = business.find('img', class_='img-responsive').get('src')

                writer.writerow({
                    'Name': name,
                    'Location': location,
                    'City': city,
                    'P.O. Box': pobox,
                    'Phone': phone,
                    'Mobile': mobile,
                    'Company Page Link': company_page_link,
                    'Logo URL': logo_url
                })

            page_num += 1

# Example usage:
base_url = "https://www.yellowpages-uae.com/uae/restaurant"
scrape_yellowpages(base_url)
