from scapy.all import IP, ICMP, sr1

def traceroute(target, max_hops=30):
    """Performs a traceroute to the target."""
    print(f"Starting traceroute to {target} (max hops: {max_hops})")
    for ttl in range(1, max_hops + 1):
        packet = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(packet, verbose=0, timeout=1)

        if reply is None:
            print(f"{ttl}: No response")
        elif reply.type == 0:
            print(f"{ttl}: {reply.src} (Reached target)")
            break
        else:
            print(f"{ttl}: {reply.src}")