import socket

def resolve_hostname(hostname):
    """Resolves a hostname to an IP address."""
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return None

def is_valid_ip(ip):
    """Checks if the provided string is a valid IPv4 address."""
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False