import os

def create_file(filepath, content=""):
    """Crée un fichier avec un contenu par défaut."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def create_project_structure():
    """Crée la structure du projet."""
    structure = {
        "core": ["scanner.py", "packet_sniffer.py", "whois_lookup.py", "traceroute.py", "ping_tool.py"],
        "utils": ["logger.py", "config.py", "helper.py"],
        "ui": ["cli.py", "gui.py"],
        "tests": ["test_scanner.py", "test_traceroute.py", "test_utils.py"],
    }

    base_files = {
        "main.py": """# -*- coding: utf-8 -*-\nfrom ui.cli import start_cli\n\ndef main():\n    print(\"=== Network Multi-Tool ===\")\n    print(\"1. Scanner réseau\")\n    print(\"2. Sniffer de paquets\")\n    print(\"3. Requête WHOIS\")\n    print(\"4. Traceroute\")\n    print(\"5. Ping\")\n    print(\"0. Quitter\")\n\n    choice = input(\"Choisissez une option : \")\n\n    if choice == \"1\":\n        from core.scanner import network_scan\n        network_scan()\n    elif choice == \"2\":\n        from core.packet_sniffer import sniff_packets\n        sniff_packets()\n    elif choice == \"3\":\n        from core.whois_lookup import whois_query\n        whois_query()\n    elif choice == \"4\":\n        from core.traceroute import perform_traceroute\n        perform_traceroute()\n    elif choice == \"5\":\n        from core.ping_tool import ping\n        ping()\n    elif choice == \"0\":\n        print(\"Au revoir !\")\n    else:\n        print(\"Choix invalide.\")\n        main()\n\nif __name__ == \"__main__\":\n    main()\n""",
        "ui/cli.py": """# -*- coding: utf-8 -*-\ndef start_cli():\n    print(\"Interface CLI lancée !\")\n""",
        "requirements.txt": "scapy\nrequests\ndnspython\npyqt5\ncolorama",
        "README.md": "# Network Multi-Tool\n\nUn outil polyvalent pour l'analyse réseau et les tests de connectivité.",
        "LICENSE": "MIT License\n\nCopyright (c) 2024",
    }

    # Créer les dossiers et fichiers
    for folder, files in structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            create_file(os.path.join(folder, file))

    for file, content in base_files.items():
        create_file(file, content)  

    print("Structure du projet créée avec succès !")

if __name__ == "__main__":
    create_project_structure()
