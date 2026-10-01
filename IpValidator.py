import ipaddress
import sys


def print_banner():
    print("=" * 40)
    print("          IP VALIDATOR")
    print("=" * 40)


def validate_ip(ip):
    try:
        result = ipaddress.ip_address(ip)
        return result
    except ValueError:
        return None


def print_info(ip, result):
    print(f"\n  Input     : {ip}")
    print(f"  Version   : IPv{result.version}")
    print(f"  Type      : ", end="")

    if result.is_private:
        print("Private")
    elif result.is_loopback:
        print("Loopback")
    elif result.is_multicast:
        print("Multicast")
    else:
        print("Public")

    print(f"  Valid     : yes")


def main():
    print_banner()

    ip = input("\n  Enter IP: ").strip()

    result = validate_ip(ip)
    if result is None:
        print(f"\n  [!] '{ip}' is not a valid IP address.")
        sys.exit(1)

    if result.version != 4:
        print(f"\n  [!] '{ip}' is valid but not IPv4 (got IPv{result.version}).")
        sys.exit(1)

    print_info(ip, result)


if __name__ == "__main__":
    main()
