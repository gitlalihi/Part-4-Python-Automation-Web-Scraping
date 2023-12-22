# to parse and check whether the site can be scraped or not using only requests library 
# not getting correct results
import requests

def get_robots_txt(url):
    robots_url = f"{url.rstrip('/')}/robots.txt"
    response = requests.get(robots_url)
    return response.text

def parse_robots_txt(robots_content, user_agent):
    rules = []
    current_agent=None
    for line in robots_content.split('\n'):
        if line.startswith('User-agent:'):
            current_agent = line.split(': ')[1]
        elif line.startswith('Disallow:') and current_agent == user_agent:
            disallowed_path = line.split(': ')[1].strip()
            rules.append(disallowed_path)
    return rules

def is_allowed_path(path, disallowed_paths):
    for disallowed_path in disallowed_paths:
        if path.startswith(disallowed_path):
            return False
    return True

target_url = 'your target url/base ul'
user_agent = 'yor scrapper name'

# Step 1: Read the robots.txt file
robots_content = get_robots_txt(target_url)

# Step 2: Parse the robots.txt file
disallowed_paths = parse_robots_txt(robots_content, user_agent)

# Step 3: Check permissions before scraping
path_to_scrape = '/some/page'
if is_allowed_path(path_to_scrape, disallowed_paths):
    # Make a request and scrape the content
    # ...
    print("Scraping allowed")
else:
    print(f"Scraping {path_to_scrape} is disallowed by robots.txt")
