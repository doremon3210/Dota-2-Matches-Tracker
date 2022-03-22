from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time
import requests


def matchResult():
    url = "https://www.dotabuff.com/matches/" + matchID

    # The headers allow the program to trick the host from detecting
    page = requests.get(url, headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find('div', class_='match-result').get_text()
    print(result)
# End of the function

def trackLog():
    # Initialize the URL
    url = "https://www.trackdota.com/matches/" + matchID

    # These 2 lines help in hiding the browser 
    options = ChromeOptions()
    options.headless = True

    # Initialize an instance of Chrome
    driver = Chrome('./chromedriver', options=options)

    # Load the web
    driver.get(url) 

    # This function to ensure that the program can scrape the website.
    # Consider in increasing the number of sleep if needed
    time.sleep(0.5)

    # Get the HTML source
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Get the Actitivy Logs
    activity_logs = soup.find('div', class_='tmyjrn-0 iqfSVJ')

    # Print out each log from latest to newest
    for log in activity_logs.find_all(class_='h1n53p-0 iDAExv')[::-1]:
        print(log.find('div').get_text() + " " + log.find('span').get_text())

    # Close the browser
    driver.quit()
# End of the function

print("Enter the match ID: ")
matchID = input()

print("Do you want to know the result? (Enter 1 or 0)")
print("1: Yes")
print("0: No")
choice = int(input())

if (choice == 1):
    matchResult()

print()
print("Do you want to see the Activity Log? (Enter 1 or 0)")
print("1: Yes")
print("0: No")
choice = int(input())
if (choice == 1):
    trackLog()

print()
print("Closing the program...")
print()