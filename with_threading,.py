import requests
import threading

with open("./subdomainlist.txt") as subdomain_file:
    subdomain_text = subdomain_file.read()

subdomains = subdomain_text.split()

same_subdomains = []
existing_subdomains = []

for subdomain in subdomains:
    if subdomain in existing_subdomains:
        same_subdomains.append(subdomain)
    else:
        existing_subdomains.append(subdomain)

print("Example target: example.com")
target = input("enter your target site: ")
subdomains_list = []

"""
def find_subdomain(url, sub_url):
    url = f"http://{sub_url}.{url}"
    try:
        rsp = requests.get(url)
        if rsp:
            subdomains_list.append(url)
    except requests.exceptions.ConnectionError:
        pass
"""

"""
for x in existing_subdomains:
    find_subdomain(target, sub_url=x)

# find_subdomain(target, "mail")

print(subdomains_list)
"""


def create_urls(url, sub_url, array_list):
    url = f"http://{sub_url}.{url}"
    array_list.append(url)


urls = []
array_list1 = []

for x in existing_subdomains:
    create_urls(target, x, array_list1)


def find_subdomain1(url):
    try:
        rsp = requests.get(url)
        print(url)
    except requests.exceptions.ConnectionError:
        pass


threads = []

for url in array_list1:
    thread = threading.Thread(target=find_subdomain1, args=(url,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All process completed!")
