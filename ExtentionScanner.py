import sys
from pathlib import Path


def print_banner():
    print("=" * 40)
    print("         EXTENSION SCANNER")
    print("=" * 40)


def scan_directory(directory):
    counter = {}
    for item in directory.iterdir():
        if item.is_file():
            ext = item.suffix.lower() or "(no extension)"
            counter[ext] = counter.get(ext, 0) + 1
    return counter


def main():
    print_banner()

    path_input = input("\n  Directory: ").strip()
    directory = Path(path_input)

    if not directory.exists():
        print("[!] Path does not exist.")
        sys.exit(1)
    if not directory.is_dir():
        print("[!] That is not a directory.")
        sys.exit(1)

    counter = scan_directory(directory)

    if not counter:
        print("  No files found.")
        return

    total = sum(counter.values())
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    print(f"\n  {'EXTENSION':<20}{'COUNT':>6}{'':>4}{'%':>5}")
    print("  " + "-" * 35)
    for ext, count in sorted_counter:
        pct = (count / total) * 100
        print(f"  {ext:<20}{count:>6}    {pct:>4.1f}%")

    print(f"\n  Total files: {total}")


if __name__ == "__main__":
    main()
