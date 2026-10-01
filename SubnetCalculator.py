import ipaddress
import sys


def print_banner():
    print("=" * 40)
    print("        SUBNET CALCULATOR")
    print("=" * 40)


def main():
    print_banner()

    user_in = input("\n  Network (e.g. 192.168.1.0/24): ").strip()

    try:
        network = ipaddress.ip_network(user_in, strict=False)
    except ValueError:
        print(f"[!] '{user_in}' is not a valid IP network.")
        sys.exit(1)

    hosts = list(network.hosts())
    first_host = hosts[0] if hosts else "N/A"
    last_host = hosts[-1] if hosts else "N/A"

    print(f"\n  Network   : {network.network_address}")
    print(f"  Broadcast : {network.broadcast_address}")
    print(f"  Mask      : {network.netmask}")
    print(f"  Prefix    : /{network.prefixlen}")
    print(f"  First IP  : {first_host}")
    print(f"  Last IP   : {last_host}")
    print(f"  Hosts     : {network.num_addresses - 2:,}")


if __name__ == "__main__":
    main()
