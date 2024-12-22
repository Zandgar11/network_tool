# Network Multi-Tool

## Overview
The **Network Multi-Tool** is a Python-based software designed for network analysis, troubleshooting, and testing connectivity. It provides essential utilities such as scanning networks, performing WHOIS lookups, tracing routes, and more.

## Features
- **Network Scanner**: Detect devices and open ports on a network.
- **Packet Sniffer**: Capture and analyze network packets.
- **WHOIS Lookup**: Retrieve domain or IP ownership information.
- **Traceroute**: Track the path packets take to a destination.
- **Ping Tool**: Test connectivity and response times.

## Requirements
- Python 3.8 or higher
- Libraries: Install dependencies with:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/network-multi-tool.git
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Choose a utility from the interactive menu.

## Project Structure
- `core/`: Core functionality modules (e.g., scanner, traceroute).
- `utils/`: Helper functions and configuration.
- `ui/`: User interfaces (CLI and GUI).
- `tests/`: Unit tests for core modules and utilities.

## Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy Networking!