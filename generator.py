python3 -c '
import pandas as pd
import random
from datetime import datetime, timedelta

def gen_tc():
    d = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(8)]
    d10 = (sum(d[0:9:2]) * 7 - sum(d[1:8:2])) % 10
    d11 = (sum(d) + d10) % 10
    d.extend([d10, d11])
    return "".join(map(str, d))

def gen_p(cc, seen):
    res = []
    for _ in range(random.randint(1, 5)):
        while True:
            prefix = "500" if cc=="+90" else "555"
            p = f"{cc}{prefix}{random.randint(1000000, 9999999)}"
            if p not in seen:
                seen.add(p); res.append(p); break
    return " | ".join(res)

countries = [("+90", "TR"), ("+1", "US"), ("+44", "UK"), ("+49", "DE"), ("+33", "FR"), ("+81", "JP"), ("+7", "RU"), ("+82", "KR")]
first_m = ["Ahmet", "Mehmet", "James", "Hans", "Jean", "Yuki", "Dmitry"]
first_f = ["Ayse", "Fatma", "Sarah", "Helga", "Lea", "Sakura", "Elena"]
last_n = ["Yilmaz", "Kaya", "Smith", "Muller", "Lefebvre", "Tanaka", "Ivanov"]
domains = ["testmail.tr", "example.us", "dummy.de", "mail.uk", "demo.io"]

data, seen_p, seen_id = [], set(), set()

for i in range(1, 3001):
    cc, tag = random.choice(countries)
    g = random.choice(["Male", "Female"])
    fn = random.choice(first_m if g=="Male" else first_f)
    ln = random.choice(last_n)
    idn = gen_tc() if tag=="TR" else f"{tag}-{random.randint(1000000, 9999999)}"
    if idn in seen_id: idn += str(i)
    seen_id.add(idn)
    bd = (datetime(1960, 1, 1) + timedelta(days=random.randint(0, 16000))).strftime("%d.%m.%Y")
    data.append([gen_p(cc, seen_p), fn, ln, f"{fn.lower()}.{ln.lower()}{i}@{random.choice(domains)}", g, bd, idn, f"Dummy St. No:{random.randint(1,200)}, {tag}"])

df = pd.DataFrame(data, columns=["phone", "firstName", "lastName", "email", "gender", "birthDate", "idNumber", "address"])
df.to_csv("global-identities-3k-dataset.csv", index=False, encoding="utf-8-sig")
print("\n--- BASARILI: 3000 KAYIT MASAÜSTÜNDE! ---")
'
