from scapy.all import sniff

def packet_sniffer(interface):
    """Sniffs network packets on the specified interface."""
    print(f"Starting packet sniffing on interface: {interface}")

    def process_packet(packet):
        print(packet.summary())

    sniff(iface=interface, prn=process_packet, store=False)