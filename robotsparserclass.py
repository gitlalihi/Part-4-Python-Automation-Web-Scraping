import urllib.robotparser

# a Few Functions of urllib.robotsparser class
r = urllib.robotparser.RobotFileParser()

r.set_url("https://httpbin.org/robots.txt")

r.read() # reads robots.txt and feeds it tp parser

print(r.can_fetch("*", "https://httpbin.org/")) # returns trueor false

#print(r.can_fetch("*","https://httpbin.org/get"))

#req_rate = r.request_rate("*")

#print(req_rate)

# Get the crawl delay for the user-agent "*"
crawl_delay = r.crawl_delay("*")

if crawl_delay is not None:
    print("Crawl delay:", crawl_delay)
else:
    print("No crawl delay specified for the user-agent.")