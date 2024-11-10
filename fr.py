#!/usr/bin/env python3
import argparse
from ressorce_discovery.utilities import banner, load_worldlist
from ressorce_discovery.request_performer import launch_threads

def main():
    banner()
    parser = argparse.ArgumentParser(description="forzebruta, a url fuzzer with advance features.")
    parser.add_argument('-u', '--url', required=True, help="Target URL with 'FUZZ' placeholder")
    parser.add_argument('-t', '--threat', type=int, default=10, help="Number of threads")
    parser.add_argument('-c', '--hidecode', nargs='+', default=[], help="Status code to hide from output")
    parser.add_argument('-w', '--wordlist', nargs='*', default=["admin", "login", "test"], help="Wordlist for fuzzing")
    parser.add_argument('-o', '--output', help="File to save results")
    parser.add_argument('--proxy', help="Proxy URL (e.g., http://127.0.0.1:8080)")
    parser.add_argument('--delay', type=float, default=0, help="Delay between requests in seconds")
    parser.add_argument('--headers', nargs='+', help="Custom headers (e.g., 'User-Agent: custom')")
    parser.add_argument('--retry', type=int, default=1, help="Retry attempts for failed requests")

    args = parser.parse_args()
    words = args.wordlist if args.wordlist else load_worldlist("default_wordlist.txt")

    launch_threads(words, args.url, args.threads, args.hidecode, args.output, args.proxy, args.headers, args.delay, args.retry)

if __name__ == "__main__":
    main()

