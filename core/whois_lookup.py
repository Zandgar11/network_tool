import socket

def whois_lookup(target):
    """Performs a WHOIS lookup for the given target."""
    print(f"Performing WHOIS lookup for: {target}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect(("whois.verisign-grs.com", 43))
            sock.sendall((target + "\r\n").encode("utf-8"))
            response = b""
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response += data
            print(response.decode("utf-8"))
    except Exception as e:
        print(f"Error during WHOIS lookup: {e}")