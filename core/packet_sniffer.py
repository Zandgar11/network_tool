rom scapy.all import sniff

def sniff_packets():
    """
    Fonction principale pour capturer des paquets réseau.
    """
    print("[INFO] Démarrage de la capture de paquets...")

    def process_packet(packet):
        print(f"[PACKET] {packet.summary()}")

    # Capture les paquets (par défaut, l'interface est auto-sélectionnée)
    sniff(prn=process_packet, store=False)
