import hashlib
import sys

ALGORITHMS = ["md5", "sha1", "sha256", "sha512", "sha3_256"]


def print_banner():
    print("=" * 40)
    print("         HASH CALCULATOR")
    print("=" * 40)


def compute_hash(algorithm, text):
    hasher = hashlib.new(algorithm)
    hasher.update(text.encode())
    return hasher.hexdigest()


def main():
    print_banner()

    print(f"\n  Available algorithms:")
    for alg in ALGORITHMS:
        print(f"    - {alg}")

    algorithm = input("\n  Choose algorithm: ").strip().lower()
    if algorithm not in ALGORITHMS:
        print(f"[!] Invalid algorithm. Choose from: {', '.join(ALGORITHMS)}")
        sys.exit(1)

    text = input("  Enter text: ")
    if not text:
        print("[!] Text cannot be empty.")
        sys.exit(1)

    digest = compute_hash(algorithm, text)

    print(f"\n  Algorithm : {algorithm}")
    print(f"  Input     : {text}")
    print(f"  Hash      : {digest}")


if __name__ == "__main__":
    main()
