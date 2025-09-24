# Python Subdomain Scanner

A simple yet fast, multithreaded subdomain enumeration tool built with Python. This script scans a target domain for common subdomains using a provided wordlist.

<p>
  <img src="https://github.com/onurmertanarat/SubdomainLister/blob/master/assets/subdomain-lister-screenshot.PNG" alt="Screenshot of the tool in action" width="600">
</p>

---

## Features

* **Multithreaded Scanning:** Utilizes a worker/queue model with a fixed number of threads to perform high-speed, concurrent scans, making it significantly faster than sequential scanning.
* **Saves Results to File:** Automatically saves all found subdomains to a formatted text file named after the target domain (e.g., `google.com_subdomains.txt`) for persistence and later use.
* **Simple and Interactive:** Requires no complex command-line arguments. Just run the script and enter the target domain when prompted.
* **Efficient Wordlist Handling:** Automatically removes duplicate entries from the wordlist before scanning to avoid redundant checks.

---

## Technology Stack

* **Python 3**
* **Standard Libraries:** `threading`, `queue`, `time`
* **External Libraries:** `requests` (for HTTP requests), `termcolor` (for colored console output).

---

## Setup and Usage

### Prerequisites

* Python 3.6+
* pip

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/onurmertanarat/SubdomainLister.git](https://github.com/onurmertanarat/SubdomainLister.git)
    cd SubdomainLister
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # Create the environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

### Running the Tool

Simply run the script using Python:

```sh
python subdomain.py
```
The script will then prompt you to enter the target domain you wish to scan.

### Wordlist

The tool uses the subdomainlist.txt file by default. You can customize this file by adding or removing subdomain entries to tailor your scans.

---

## Contact

Onur Mert Anarat

[linkedin.com/in/onurmertanarat](https://www.linkedin.com/in/onurmertanarat)
