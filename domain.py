'''
Write a function that when given a URL as a string, parses out just the domain 
name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''
import re


def domain_name(url):
    regex = re.compile(r'(\w+)?[:\.](//)?(www.)?([\w-]+)')
    find = regex.search(url)
    for element in list(find.groups()):
        return element if element not in ['https', 'www', 'http']\
             else find.group(4)


def domain_name2(url):
    url = url.replace("http://", "").replace("https://", "")\
        .replace("www.", "")
    end = url.find(".")
    return url[0:end]


def domain_name3(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

lista = [
    'https://it.cornell.edu/dns/examples-domain-names',
    "http://github.com/carbonfive/raygun",
    'https://www.google.com/search?q=format+of+a+domain+name&rlz=1C1CHBD_esVE924VE924&oq=format+os+a+domain&aqs=chrome.1.69i57j0i19j0i19i22i30l2j0i19i22i30i395l6.7318j1j7&sourceid=chrome&ie=UTF-8',
    'www.xakep.ru',
    'http://www.codewars.com/kata/',
    'https://hyphen-site.org',
    'icann.org'
]

for element in lista:
    print(domain_name3(element))
