import requests

BURP_API = "http://localhost:1337/v0.1/scan"

def start_scan(target):
    payload = {
        "target": {
            "scope": {
                "include": [{"host": target}]
            }
        }
    }

    r = requests.post(BURP_API, json=payload)
    print("[+] Scan iniciado!")
    print(r.json())

if __name__ == "__main__":
    alvo = input("Host para escanear: ")
    start_scan(alvo)
