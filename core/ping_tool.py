from scapy.all import IP, ICMP, sr1

def ping(target, count=4):
    """Sends ICMP echo requests to the target."""
    print(f"Pinging {target} with {count} packets:")
    for i in range(count):
        packet = IP(dst=target) / ICMP()
        reply = sr1(packet, verbose=0, timeout=1)
        if reply is None:
            print(f"Request {i + 1}: No response")
        else:
            print(f"Request {i + 1}: Reply from {reply.src} - Time={reply.time}")