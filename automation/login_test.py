import requests

def test_login(url, users, passwords):
    for user in users:
        for pwd in passwords:
            payload = {"username": user, "password": pwd}
            r = requests.post(url, json=payload)
            print(f"Tentando {user}:{pwd} -> Status {r.status_code}")

if __name__ == "__main__":
    url = input("URL de login da API: ")
    users = ["admin", "root", "test"]
    passwords = ["123", "admin", "password", "root"]
    test_login(url, users, passwords)
