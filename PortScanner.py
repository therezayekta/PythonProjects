import errno
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor


def print_banner():
    print("=" * 45)
    print("           PORT SCANNER")
    print("=" * 45)


def get_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def check_port(host, port, timeout=1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        code = s.connect_ex((host, port))
        return code


def get_state(code):
    if code == 0:
        return "open"
    elif code == errno.ECONNREFUSED:
        return "closed"
    else:
        return "filtered"


def scan_port(host, port):
    return port, check_port(host, port)


def parse_ports(text):
    ports = []
    for part in text.split(","):
        if "-" in part:
            start, end = part.split("-")
            start, end = int(start), int(end)
            if start > end or not (1 <= start <= 65535) or not (1 <= end <= 65535):
                raise ValueError
            ports.extend(range(start, end + 1))
        else:
            p = int(part)
            if not (1 <= p <= 65535):
                raise ValueError
            ports.append(p)
    return sorted(set(ports))


def resolve_host(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        print(f"[!] Could not resolve host: {host}")
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <host> [ports]")
        print(f"Example: python {sys.argv[0]} 127.0.0.1 22,80,1000-2000")
        sys.exit(1)

    host = sys.argv[1]
    port_text = sys.argv[2] if len(sys.argv) > 2 else "1-1024"

    try:
        ports = parse_ports(port_text)
    except ValueError:
        print("[!] Invalid ports. Use: 80 or 22,80 or 1-1024")
        sys.exit(1)

    ip = resolve_host(host)

    print_banner()
    print(f"\n  Target : {host} ({ip})")
    print(f"  Ports  : {len(ports)}")
    print(f"  Threads: 100\n")
    print("-" * 45)

    open_ports = []
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scan_port, host, port) for port in ports]
        for future in futures:
            port, code = future.result()
            if code == 0:
                open_ports.append(port)

    elapsed = time.perf_counter() - start

    if open_ports:
        print(f"\n  {'PORT':<8}{'SERVICE':<14}STATE")
        print("  " + "-" * 30)
        for port in sorted(open_ports):
            service = get_service(port)
            print(f"  {port:<8}{service:<14}open")
    else:
        print("\n  No open ports found.")

    print(f"\n  Scanned {len(ports)} ports in {elapsed:.2f}s")


if __name__ == "__main__":
    main()
