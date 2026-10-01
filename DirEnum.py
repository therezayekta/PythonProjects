import requests
import sys
import time


def print_banner():
    print("=" * 45)
    print("         DIRECTORY ENUMERATOR")
    print("=" * 45)


def load_wordlist(path):
    try:
        with open(path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Wordlist not found: {path}")
        sys.exit(1)


def enumerate_dirs(target, paths):
    found = []
    forbidden = []
    failed = []

    for path in paths:
        url = f"{target.rstrip('/')}/{path}"
        try:
            res = requests.get(url, timeout=3)
            if res.status_code == 200:
                print(f"  [+] Found     {url}")
                found.append(url)
            elif res.status_code == 403:
                print(f"  [!] Forbidden {url}")
                forbidden.append(url)
        except requests.exceptions.RequestException:
            failed.append(url)

    return found, forbidden, failed


def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <url> <wordlist>")
        sys.exit(1)

    target = sys.argv[1]
    wordlist_path = sys.argv[2]

    print_banner()
    print(f"\n  Target   : {target}")
    print(f"  Wordlist : {wordlist_path}\n")
    print("-" * 45)

    paths = load_wordlist(wordlist_path)
    start = time.perf_counter()
    found, forbidden, failed = enumerate_dirs(target, paths)
    elapsed = time.perf_counter() - start

    print("-" * 45)
    print(f"\n  Found     : {len(found)}")
    print(f"  Forbidden : {len(forbidden)}")
    print(f"  Failed    : {len(failed)}")
    print(f"  Time      : {elapsed:.2f}s")


if __name__ == "__main__":
    main()
