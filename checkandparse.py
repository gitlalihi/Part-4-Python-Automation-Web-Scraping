#parsing and checking access rules using urilib.robotsparser
import  requests
from urllib import robotparser
from urllib.parse import urljoin, urlparse

def fetch_robots_txt(base_url):
    robots_url = urljoin(base_url, '/robots.txt')
    response = requests.get(robots_url)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to fetch robots.txt. Status code: {response.status_code}")
        return None

def parse_robots_txt(robots_content):
    r = robotparser.RobotFileParser()
    r.parse(robots_content.splitlines())
    return r

def can_fetch_url(r, user_agent, url):
    return r.can_fetch(user_agent, url)

def main():
    base_url = 'your target site'
    user_agent = 'your user-agent name'
    robots_content = fetch_robots_txt(base_url)
    if robots_content:
        # Step 2: Parse robots.txt
        rp = parse_robots_txt(robots_content)

        # Step 3: Check if the scrapper bot is allowed to access a specific URL
        sample_url = urljoin(base_url, 'target site/some/page')
        if can_fetch_url(rp, user_agent, sample_url):
             # lOGIC FOR SCRAPING here
             #.....

             #......
             print(f"Scraping allowed {sample_url}")
        else:
            print(f"Access to {sample_url} is not allowed by robots.txt")

if __name__ == "__main__":
    main()

