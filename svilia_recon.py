import socket
import sys

def banner():
    print("""
    #########################################
    #           SVILIA HACK TEAM            #
    #        Recon & Port Scanner v1.0      #
    #########################################
    """)

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

if __name__ == "__main__":
    banner()
    if len(sys.argv) == 2:
        target = sys.argv[1]
        print(f"[*] Scanning Target: {target}")
        # En yaygın kullanılan portlar
        common_ports = [21, 22, 80, 443, 8080, 3306]
        for port in common_ports:
            scan_port(target, port)
    else:
        print("Usage: python3 svilia_recon.py <target_ip>")
