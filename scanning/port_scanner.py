import socket

def scan(target):
    print(f"Escaneando {target}...\n")
    for port in range(1, 1025):
        s = socket.socket()
        s.settimeout(0.3)
        try:
            s.connect((target, port))
            print(f"[+] Porta aberta: {port}")
        except:
            pass

if __name__ == "__main__":
    alvo = input("Digite o host (ex: scanme.nmap.org): ")
    scan(alvo)
