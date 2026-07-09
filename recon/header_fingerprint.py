import requests

def fingerprint(url):
    try:
        r = requests.get(url, timeout=5)
        print(f"[+] URL: {url}")
        print("[+] Server:", r.headers.get("Server"))
        print("[+] X-Powered-By:", r.headers.get("X-Powered-By"))
        print("[+] Cookies:", r.cookies.get_dict())
        print("[+] Status Code:", r.status_code)
    except Exception as e:
        print("[-] Erro:", e)

if __name__ == "__main__":
    target = input("Digite a URL alvo (ex: https://example.com): ")
    fingerprint(target)
