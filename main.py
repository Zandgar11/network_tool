import os
import sys

def main():
    print("=== Network Multi-Tool ===")
    print("1. Scanner réseau")
    print("2. Sniffer de paquets")
    print("3. Requête WHOIS")
    print("4. Traceroute")
    print("5. Ping")
    print("0. Quitter")

    while True:
        try:
            choice = int(input("Choisissez une option : "))
            
            if choice == 1:
                from core.packet_sniffer import sniff_packets
                target = input("Entrez l'adresse IP ou la plage (ex: 192.168.1.0/24) : ")
                sniff_packets(target)

            elif choice == 2:
                from core.packet_sniffer import sniff_packets
                sniff_packets()

            elif choice == 3:
                from core.whois_lookup import whois_lookup
                target = input("Entrez le domaine ou l'adresse IP pour la recherche WHOIS : ")
                whois_lookup(target)

            elif choice == 4:
                from core.traceroute import traceroute
                target = input("Entrez l'adresse IP ou le domaine à tracer : ")
                traceroute(target)

            elif choice == 5:
                from core.ping_tool import ping
                target = input("Entrez l'adresse IP ou le domaine à pinger : ")
                ping(target)

            elif choice == 0:
                print("Au revoir !")
                sys.exit(0)

            else:
                print("Option invalide. Veuillez réessayer.")

        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
