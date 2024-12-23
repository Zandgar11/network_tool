# -*- coding: utf-8 -*-
from ui.cli import start_cli

def main():
    print("=== Network Multi-Tool ===")
    print("1. Scanner réseau")
    print("2. Sniffer de paquets")
    print("3. Requête WHOIS")
    print("4. Traceroute")
    print("5. Ping")
    print("0. Quitter")

    choice = input("Choisissez une option : ")

    if choice == "1":
        from core.scanner import network_scan
        network_scan()
    elif choice == "2":
        from core.packet_sniffer import sniff_packets
        sniff_packets()
    elif choice == "3":
        from core.whois_lookup import whois_lookup
        whois_lookup()
    elif choice == "4":
        from core.traceroute import traceroute
        traceroute()
    elif choice == "5":
        from core.ping_tool import ping
        ping()
    elif choice == "0":
        print("Au revoir !")
    else:
        print("Choix invalide.")
        main()

if __name__ == "__main__":
    main()
