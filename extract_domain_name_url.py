# Write a function that when given a URL as a string,
# parses out just the domain name and returns it as a string.
def domain_name(url):
    if "www" in url:
        url = url.split("www.")[1]
    if "http" in url:
        url = url.split("//")[1]
    if "https" in url:
        url = url.split("//")[1]
    if "://" in url:
        url = url.split("://")[1]
    if "/" in url:
        url = url.split("/")[0]
    if "." in url:
        url = url.split(".")[0]
    return url


print(domain_name("http://codewars.com"))
