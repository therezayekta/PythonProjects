import requests
import sys

BASE_URL = "https://dummyjson.com"


def get_products(limit=10):
    res = requests.get(f"{BASE_URL}/products", params={"limit": limit}, timeout=5)
    res.raise_for_status()
    return res.json()


def get_product(product_id):
    res = requests.get(f"{BASE_URL}/products/{product_id}", timeout=5)
    res.raise_for_status()
    return res.json()


def print_banner():
    print("=" * 40)
    print("         API CLIENT — dummyjson")
    print("=" * 40)


def main():
    print_banner()

    try:
        data = get_products(limit=5)
        products = data["products"]

        print(f"\n{'ID':<6}{'TITLE':<30}{'PRICE':>8}")
        print("-" * 44)
        for p in products:
            print(f"{p['id']:<6}{p['title'][:28]:<30}{p['price']:>8.2f}")

        print(f"\nShowing {len(products)} of {data['total']} products")

    except requests.Timeout:
        print("[!] Request timed out.")
        sys.exit(1)
    except requests.HTTPError as e:
        print(f"[!] HTTP error: {e.response.status_code}")
        sys.exit(1)
    except requests.ConnectionError:
        print("[!] Could not connect. Check your internet.")
        sys.exit(1)


if __name__ == "__main__":
    main()
