# scrape_tool
 python script to scrape all the details in the given url-
csv: This module provides classes for reading and writing tabular data in CSV format.
requests: This library is used for making HTTP requests.
BeautifulSoup: This library is used for parsing HTML and extracting data from it.
Function Definition:
scrape_yellowpages(base_url): This function takes the base URL of the Yellow Pages directory as input.
Opening CSV File for Writing:
with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile: This line opens a CSV file named "results.csv" in write mode. The newline='' parameter is used to prevent extra blank lines being inserted between rows, and encoding='utf-8' ensures proper handling of special characters.
Writing Header Row:
fieldnames = [...]: This list contains the names of the columns for the CSV file.
writer = csv.DictWriter(csvfile, fieldnames=fieldnames): This creates a DictWriter object, which allows writing rows to the CSV file based on dictionaries where the keys correspond to column names.
writer.writeheader(): This method writes the header row containing column names to the CSV file.
Scraping Loop:
while True:: This loop will continue indefinitely until it's explicitly broken.
url = f"{base_url}?page={page_num}": This constructs the URL for each page by appending the page number to the base URL.
response = requests.get(url): This sends an HTTP GET request to the URL and stores the response.
soup = BeautifulSoup(response.content, 'html.parser'): This creates a BeautifulSoup object from the HTML content of the response.
Extracting Business Information:
businesses = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4'): This finds all the HTML elements that represent individual businesses on the page.
Inside the loop over businesses, the script extracts various pieces of information for each business such as name, location, city, etc., using BeautifulSoup's find and find_all methods.
The extracted information is then written to the CSV file using writer.writerow() with the appropriate column names.
Pagination Handling:
The loop increments the page_num variable to move to the next page of results until there are no more businesses found or an error occurs.
Example Usage:
The script sets base_url to the URL of the Yellow Pages directory for restaurants in the UAE.
It then calls the scrape_yellowpages() function with this base URL to start the scraping process.
