import os
while True:
    tarama = str(input("""
    1) Wafw00f ile Waf Tespiti
    2) Nmap İle Port Tarama
    3) Nmap İle Zaafiyet Tarama 
    4) Uniscan İle Zaafiyet Tarama
    5) Sqlmap İle Sql İnjection
                            coded by arda6
    """))
    if tarama == '1':
        site = str(input("Hedef Site:"))
        os.system("sudo wafw00f" + site + "")
    elif tarama == '2':
        site = str(input("Hedef Site:"))
        os.system("sudo nmap -T4 -A -sV -Pn --script firewall-bypass " + site + "")
    elif tarama == '3': 
        site = str(input("Hedef Site:"))
        os.system("sudo nmap -T4 -A -sV -Pn --script vuln " + site + "")
    elif tarama == '4':
        site = str(input("Hedef Site"))
        os.system("sudo uniscan -u " + site + "-qweds")
    elif tarama == '5':
        site = str(input("Açıklı Url :"))
        tamper = str(input("Seçilecek Tamper :  between /  binary /  space2comment /  hex3char :"))
        os.system("sqlmap -u " + site + "--random-agent --tamper="+tamper+ "--hex --dbs")

