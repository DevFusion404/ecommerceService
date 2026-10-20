"""
Network Client - Socket and port connectivity helper.
"""

def parse_port(port_text):
    try:
        port_num = int(port_text)
        return port_num
    except:
        return 8080

if __name__ == "__main__":
    print("Port:", parse_port("9090"))
