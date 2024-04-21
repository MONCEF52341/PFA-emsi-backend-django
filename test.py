import requests

API_URLS = [
    "admin",
    "api/collaborateurs/",
    "api/collaborateurs/1/",
    "api/demandeabsence/",
    "api/demandeabsence/1/",
    "api/equipe/",
    "api/equipe/1/",
    "api/entitejuridique/",
    "api/entitejuridique/1/",
    "api/lieutravail/",
    "api/lieutravail/1/",
    "api/emploi/",
    "api/emploi/1/",
    "api/contrat/",
    "api/contrat/1/",
    "api/heurescontractuelles/",
    "api/heurescontractuelles/1/",
    "api/politiqueabsences/",
    "api/politiqueabsences/1/",
    "api/compteurabsences/",
    "api/compteurabsences/1/",
    "api/typeabsence/",
    "api/typeabsence/1/",
    "api/cycle/",
    "api/cycle/1/",
    "api/configuration/",
    "api/configuration/1/",
    "api/seniority/",
    "api/seniority/1/"
]

def test_urls():
    success=0
    notfound=0
    erreurserveur=0
    unknown=0
    answer_rate=0
    success_rate=0
    fail_rate=0
    for url in API_URLS:
        response = requests.get(f"http://localhost:8000/{url}")
        if response.status_code == 200:
            print(f"✅ URL {url} : OK (Statut {response.status_code})")
            success=success+1
        elif response.status_code == 404:
            print(f"🗿 URL {url} : ERREUR 404 (Non trouvé)")
            notfound=notfound+1
        elif response.status_code == 500:
            print(f"💥 URL {url} : ERREUR 500 (Erreur interne du serveur)")
            erreurserveur=erreurserveur+1
        else:
            print(f"❌ URL {url} : ERREUR (Statut {response.status_code})")
            print(response.text)
            unknown=unknown+1
        answer_rate = round((success+notfound) / len(API_URLS)*100)
        success_rate = round((success) / len(API_URLS)*100)
        fail_rate= round((unknown+erreurserveur) / len(API_URLS)*100)
    print("\nPourcentage de réponse ✅ + 🗿: " +str(answer_rate) + "%\n")
    print("\nPourcentage de réponse Valide ✅ : " +str(success_rate) + "%\n")
    print("\nPourcentage d'erreur 💥 + ❌: " +str(fail_rate) + "%\n")
    print("✅ = " +  str(success))
    print("🗿 = " +  str(notfound))
    print("💥 = " +  str(erreurserveur))
    print("❌ =  " +  str(unknown))

    

if __name__ == "__main__":
    test_urls()
