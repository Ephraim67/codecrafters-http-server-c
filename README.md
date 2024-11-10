## Forzebruta
Forzebruta is a command-line tool for fuzzing URLs, useful for security testing and resource discovery. It supports multithreading, customizable headers, proxying, retry on failed requests, and status code filtering.

## Features
-  Multithreaded requests
- Custom wordlist for fuzzing
- Supports proxy and headers
- Hides specified HTTP status codes from output
- Saves results to a file
- Retry mechanism for failed requests

## Installation
1. Clone the repository:
   - git clone https://github.com/username/forzebruta.git
   - cd forzebruta

3. Install all required dependencies:
   - pip install -r requirements.txt

4. Make it executable:
   - chmod +x fr.py

## Usage
  ./fr.py -u **URL** -w **wordlist** -t **threads** -c **hidecode**

## Arguments
- -u, --url: Target URL with 'FUZZ' placeholder
- -t, --threads: Number of threads (default: 10)
- -c, --hidecode: Status codes to hide from output
- -w, --wordlist: Wordlist for fuzzing (default: wordlists/default_wordlist.txt)
- -o, --output: File to save results
- --proxy: Proxy URL (e.g., http://127.0.0.1:8080)
- --delay: Delay between requests in seconds (default: 0)
- --headers: Custom headers (e.g., 'User-Agent: custom')
- --retry: Retry attempts for failed requests (default: 1)


