# 🛡️ Red Team — Comandos Essenciais de Reconhecimento e Enumeração

Este documento reúne os principais comandos utilizados em atividades de **Red Team**, **Pentest** e **Análise de Superfície de Ataque**, sempre em ambientes autorizados.  
O foco aqui é **reconhecimento, coleta de informações e análise**, sem qualquer instrução de exploração.

---

# 🌐 1. HTTP / Web — Inspeção e Coleta de Informações

## curl
Ferramenta para enviar requisições HTTP e inspecionar respostas do servidor.

### O que faz:
- Ver headers  
- Ver cookies  
- Testar endpoints  
- Enviar dados para APIs  

### Exemplos:
curl -I https://site.com  
curl -v https://site.com  
curl -X POST https://site.com/api -d "user=test"

---

## wget
Utilizado para baixar arquivos ou páginas.

### O que faz:
- Baixa arquivos  
- Baixa páginas  
- Baixa sites recursivamente  

### Exemplos:
wget https://site.com/robots.txt  
wget -r https://site.com

---

# 📁 2. Descoberta de Diretórios e Arquivos

## gobuster
Descobre diretórios e arquivos ocultos.

gobuster dir -u https://site.com -w wordlist.txt

## ffuf
Fuzzing rápido para diretórios e parâmetros.

ffuf -u https://site.com/FUZZ -w wordlist.txt

## dirsearch
Scanner de diretórios simples e eficiente.

dirsearch -u https://site.com

---

# 🔎 3. Fingerprinting de Tecnologias

## whatweb
Identifica tecnologias usadas no site.

whatweb https://site.com

## wappalyzer (CLI)
Detecta frameworks, linguagens e servidores.

wappalyzer https://site.com

## nmap (fingerprinting)
Descobre versões e serviços.

nmap -sV -sC -O <IP>

---

# 🔌 4. Portas e Serviços

## nmap
Scanner completo de portas e serviços.

nmap -sV <IP>  
nmap -sC <IP>  
nmap -p- <IP>

## rustscan
Scanner extremamente rápido.

rustscan -a <IP>

---

# 🌍 5. DNS / Domínios / Subdomínios

## dig
Consulta registros DNS.

dig site.com ANY

## nslookup
Consulta simples de DNS.

nslookup site.com

## host
Consulta rápida de DNS/IP.

host site.com

## dnsenum
Enumeração completa de DNS.

dnsenum site.com

## subfinder
Descoberta de subdomínios.

subfinder -d site.com

## amass
Enumeração avançada de subdomínios.

amass enum -d site.com

---

# 📡 6. Inspeção de Serviços

## nc (netcat)
Testa conexões TCP/UDP.

nc -nv <IP> <PORT>

## telnet
Testa serviços manualmente.

telnet <IP> <PORT>

---

# 🔐 7. Informações de Domínio

## whois
Mostra informações sobre o domínio.

whois site.com

---

# 🧭 8. Rede

## ping
Testa conectividade.

ping <IP>

## traceroute
Mostra o caminho até o servidor.

traceroute <IP>

---

# 🧠 9. HTTP Security Headers — Aula Completa

Headers são **metadados** enviados junto com requisições HTTP.  
Eles dizem ao navegador **como se comportar**, e ao analista **como o servidor está configurado**.

---

## Strict-Transport-Security (HSTS)
Força uso de HTTPS e impede downgrade para HTTP.

Strict-Transport-Security: max-age=31536000; includeSubDomains

---

## X-Frame-Options
Evita clickjacking (site dentro de iframe).

X-Frame-Options: DENY

---

## X-Content-Type-Options
Evita MIME sniffing (navegador adivinhar tipo de arquivo).

X-Content-Type-Options: nosniff

---

## Content-Security-Policy (CSP)
Controla de onde scripts e recursos podem ser carregados.

Content-Security-Policy: default-src 'self'

---

## Referrer-Policy
Evita vazamento de URLs internas e tokens.

Referrer-Policy: no-referrer

---

## Permissions-Policy
Controla acesso a APIs do navegador (câmera, microfone, etc).

Permissions-Policy: geolocation=(), microphone=()

---

## Set-Cookie (com flags de segurança)
Protege cookies de sessão.

Set-Cookie: id=123; HttpOnly; Secure; SameSite=Strict

### Flags:
- HttpOnly → impede acesso via JavaScript  
- Secure → só envia via HTTPS  
- SameSite → protege contra CSRF  

---

# 🏁 Conclusão

Este documento reúne os comandos essenciais utilizados em atividades de **reconhecimento, enumeração e análise de superfície de ataque**, fundamentais para profissionais de **Red Team**, **Pentest** e **Segurança da Informação**.

Copie, cole e use como referência no seu portfólio.
