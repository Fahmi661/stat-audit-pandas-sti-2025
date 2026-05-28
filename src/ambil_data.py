import requests
import pandas as pd
import time

TOKEN = "YOUR_GITHUB_TOKEN_HERE"  
HEADERS = {"Authorization": f"token {TOKEN}"}

def ambil_issues():
    issues = []
    page = 1
    print("Mengambil issues...")
    
    while True:
        url = "https://api.github.com/repos/pandas-dev/pandas/issues"
        params = {
            "state": "closed",
            "per_page": 100,
            "page": page
        }
        response = requests.get(url, headers=HEADERS, params=params)
        data = response.json()
        
        if not data:
            break
            
        issues.extend(data)
        print(f"Halaman {page} — total: {len(issues)}")
        page += 1
        time.sleep(1)  # hindari rate limit
        
        if page > 50:  # batasi 5000 issues dulu
            break
    
    return issues

def ambil_prs():
    prs = []
    page = 1
    print("Mengambil Pull Requests...")
    
    while True:
        url = "https://api.github.com/repos/pandas-dev/pandas/pulls"
        params = {
            "state": "closed",
            "per_page": 100,
            "page": page
        }
        response = requests.get(url, headers=HEADERS, params=params)
        data = response.json()
        
        if not data:
            break
            
        prs.extend(data)
        print(f"Halaman {page} — total: {len(prs)}")
        page += 1
        time.sleep(1)
        
        if page > 50:  # batasi 5000 PRs dulu
            break
    
    return prs

# Jalankan
issues = ambil_issues()
prs = ambil_prs()

# Simpan ke CSV
df_issues = pd.DataFrame(issues)
df_prs = pd.DataFrame(prs)

df_issues.to_csv("data/raw/issues_raw.csv", index=False)
df_prs.to_csv("data/raw/prs_raw.csv", index=False)

print("Selesai! File tersimpan di data/raw/")
