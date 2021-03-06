import sys
import requests
from bs4 import BeautifulSoup

# Terminal Colors
OK = '\033[92m'
FAIL = '\033[91m'
WARN = '\033[93m'
NC = '\033[0m'

# Check number of args
if len(sys.argv) != 2:
    print(FAIL + "[ERROR] Missing argument `username`\n")
    print(NC + "Usage: python3 dev-scraper.py `username`\n")
    sys.exit(1)

# Put username in the request url
user = sys.argv[1]
url = 'https://www.devpost.com/' + user
print(OK + "Getting Devpost info from " + url + "...\n" + NC)
data = requests.get(url=url)

# If request unsuccessful, exit
if data.status_code != 200:
    print(FAIL + "[ERROR] 404 Error, cannot find username {}".format(WARN + user))
    sys.exit(1)

# Create beautiful soup object
soup = BeautifulSoup(data.text, 'html.parser')

# Parse data from beautiful soup object
projects = soup.find('a', {'href': '/' + user}).find('span').text.strip()
hackathons = soup.find('a', {'href': '/' + user + '/challenges'}).find('span').text.strip()
followers = soup.find('a', {'href': '/' + user + '/followers'}).find('span').text.strip()
winner = soup.find_all('img', {'class': 'winner'})

print("Projects:\t{}\nHackathons:\t{}\nFollowers:\t{}\nWins:\t\t{}".format(projects, hackathons, followers, len(winner)))

