import subprocess
import ipaddress

def whois_lookup(target):
    """
    Effectue une recherche WHOIS pour le domaine ou l'adresse IP spécifié.
    """
    try:
        # Vérifiez si l'adresse est locale
        try:
            ip = ipaddress.ip_address(target)
            if ip.is_private:
                print("[ERREUR] Les adresses IP privées ne peuvent pas être recherchées dans les bases WHOIS.")
                return
        except ValueError:
            pass  # Ce n'est pas une adresse IP, continuez avec un domaine

        # Exécutez la commande WHOIS
        print(f"[INFO] Recherche WHOIS pour : {target}")
        result = subprocess.run(["whois", target], capture_output=True, text=True)

        # Vérifiez si le résultat est vide ou contient une erreur
        if "No match for" in result.stdout or result.returncode != 0:
            print("[ERREUR] Aucune correspondance trouvée ou domaine non valide.")
        else:
            print(result.stdout)

    except Exception as e:
        print(f"[ERREUR] Une erreur est survenue lors de la recherche WHOIS : {e}")
