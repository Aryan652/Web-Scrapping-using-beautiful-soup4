# Web-Scrapping-using-beautiful-soup4
In this repository i scrapped a certain website using python web scrapping library named as bs4
# *Ocado Scraper*
This script is a web scraper for the Ocado website, which extracts product information and stores it in an Excel file.

## **Usage**
Install the required libraries by running:
1. Copy code
`pip install beautifulsoup4 pandas requests`
2. Update the url variable with the desired Ocado category URL.
3. Run the script.

The script will print the name and URL of each product in the category, and then scrape the product details and save them in an Excel file.

## **Data Structure**
The scraped data is stored in an Excel file with the following structure:


* Each product has its own sheet.
* The sheet name is the product name.
* The table columns are:
	* `Name`: The name of the product.
	* `Unit Price`: The price per unit of the product.
	* `Weight`: The weight of the product.
	* `Units`: The number of units in the product.
	* `Description`: A description of the product.
   
## **Functions**
* `req(url)`: Sends a GET request to the given URL and returns the response text.
* `pharse(text)`: Parses the given HTML text using BeautifulSoup.
* `soup(content, pharse, id='default value', func='default value')`: Searches for elements in the parsed HTML content based on the given parameters.
* `scrap(url, elem='default value', id='default value', func='default value')`: Scrapes the given URL and searches for elements based on the given parameters.
* `decode(content)`: Decodes the given HTML content and returns the decoded string.
  
# **Note**
The script is designed to scrape product information from the Ocado website. However, the structure of the website may change, which could break the script. If you encounter any issues, please update the script accordingly.



