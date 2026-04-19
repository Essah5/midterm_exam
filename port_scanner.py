import socket
import time

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "scanme.nmap.org"]

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scanner:
            scanner.settimeout(1)
            result = scanner.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        raise ValueError("Hostname could not be resolved.")
    except Exception as e:
        raise RuntimeError(f"Scan error: {e}")

def main():
    try:
        host = input("Enter host: ").strip()

        if host not in ALLOWED_HOSTS:
            print("Error: Only 127.0.0.1, localhost, or scanme.nmap.org allowed.")
            return

        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))

        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("Error: Invalid port range.")
            return

        print(f"\nScanning {host}...\n")

        for port in range(start_port, end_port + 1):
            is_open = scan_port(host, port)
            status = "OPEN" if is_open else "CLOSED"
            print(f"Port {port}: {status}")
            time.sleep(0.1)

        print("\nScan complete.")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()