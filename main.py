from datetime import datetime


try:
    with open("sample.log", "r") as file:
        logs = file.readlines()
except FileNotFoundError:
    print("CHYBA: Zadaný soubor nebyl nalezen.")
    exit()

if not logs:
    print("Soubor je prázdný. Nejsou žádné záznamy k analýze.")
    exit()

count_failed_login = 0


user_failed_login = {}
user_failed_times = {}

for line in logs:
    if "Failed login" in line:
        parts = line.split()
        if len(parts) < 8:
            continue
        if parts[6] != "user":
            continue
        date = parts[0]
        time = parts[1]
        timestamp = f"{date} {time}"
        try:    
            parsed_time = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue    
        user = parts[7]
        if user not in user_failed_times:
            user_failed_times[user] = []
        user_failed_times[user].append(parsed_time)
          
        count_failed_login += 1
        
        if user in user_failed_login:
            user_failed_login[user] += 1
        else:
            user_failed_login[user] = 1

# Detekce uživatelů s alespoň 5 neúspěšnými pokusy
suspicious_found = False
for user, count in user_failed_login.items():
    if count >= 5:
        suspicious_found = True
        print(f"Uživatel: {user} počet pokusů přihlášení: {count}.")
   
if not suspicious_found:
    print("Žádný uživatel nemá 5 nebo více neúspěšných přihlášení.")
# Sledujeme, zda byla nalezena podezřelá série přihlášení
attack_found = False   
# Kontrola jednotlivých uživatelů
for user, times in user_failed_times.items():
    times.sort()
    #Detekce alespoň 5 neuspěšných přihlášení během 5 minut
    for index in range(4, len(times)):
        difference = (times[index] - times[index - 4]).total_seconds()
        if difference <= 300:
            attack_found = True
            print(f"WARNING: Uživatel {user} - možný brute-force útok (alespoň 5 neúspěšných přihlášení během 5 minut).")
            break
# Pokud nebyla nalezena žádná podezřelá série 
if not attack_found:
    print("Analýza dokončena. Nebyla nalezena žádná podezřelá série.")

print(f"Celkový počet neúspěšných přihlášení: {count_failed_login}.")