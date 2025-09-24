import requests
import threading
from queue import Queue
import time

NUM_THREADS = 50
WORDLIST_FILE = "subdomainlist.txt"

q = Queue()
found_subdomains = []
print_lock = threading.Lock()

def save_results_to_file(subdomains_list, target_domain):
    filename = f"{target_domain}_subdomains.txt"
    with open(filename, "w") as f:
        for subdomain in subdomains_list:
            f.write(f"{subdomain}\n")
    
    with print_lock:
        print(f"\n[*] Results have been saved to the file: {filename}")


def scan_url(url):
    try:
        requests.get(url, timeout=5)
    except requests.ConnectionError:
        pass
    else:
        with print_lock:
            print(f"[+] Found Subdomain: {url}")
        found_subdomains.append(url)

def worker():
    while True:
        try:
            url = q.get_nowait()
            scan_url(url)
        except:
            break

def main():
    print("--- Subdomain Scanner ---")
    target_domain = input("Enter the target domain (e.g., google.com): ")

    try:
        with open(WORDLIST_FILE, "r") as f:
            unique_subdomains = list(set(f.read().splitlines()))
    except FileNotFoundError:
        print(f"[-] Error: Wordlist file '{WORDLIST_FILE}' not found.")
        return

    print(f"\n[*] Scanning {target_domain} with {len(unique_subdomains)} subdomains using {NUM_THREADS} threads...")

    for subdomain in unique_subdomains:
        url = f"http://{subdomain}.{target_domain}"
        q.put(url)

    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    
    print("\n--- Scan Complete ---")
    if found_subdomains:
        sorted_results = sorted(found_subdomains)
        print(f"[*] Found {len(sorted_results)} subdomains:")
        for sub in sorted_results:
            print(f"[+] {sub}")
        
        save_results_to_file(sorted_results, target_domain)
    else:
        print("[*] No subdomains were found.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"\n[*] Scan finished in {end_time - start_time:.2f} seconds.")