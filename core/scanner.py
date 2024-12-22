import socket
from utils.logger import log

# Function to perform a network scan
def network_scan():
    """
    Scans a given range of IP addresses for open ports.
    """
    print("=== Network Scanner ===")

    # Get target IP or domain from the user
    target = input("Enter the target IP or domain: ")

    # Validate the input
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target. Please enter a valid IP or domain.")
        return

    print(f"Scanning target: {target} ({target_ip})")

    # Define the port range to scan
    start_port = int(input("Enter the start port (e.g., 1): "))
    end_port = int(input("Enter the end port (e.g., 65535): "))

    print("Scanning...")

    try:
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Timeout for each connection attempt
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port} is open.")
                    log(f"Port {port} open on {target_ip}")
    except KeyboardInterrupt:
        print("Scan interrupted by user.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return

    print("Scan completed.")

if __name__ == "__main__":
    network_scan()