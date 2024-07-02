import webbrowser
import time

def main():
    prenom_nom = input("Enter your first (prenom) and last (nom) names: ")

    url_collection = [
        "coding101", "critical101", "reverse", "cloud2", "IMR_cloud/course", "cryptocurrency",
        "cscrm", "cyberessentials", "IMR_RANS/course", "fcsm", "fcrm", "ici",
        "IMR4/course", "IMR6/course", "IMR_105/course"
    ]

    for url in url_collection:
        url_to_open = f"https://fedvte.usalearning.gov/publiccourses/{url}/gencert.php?Name={prenom_nom}"
        webbrowser.open_new(url_to_open)
        time.sleep(6)

if __name__ == "__main__":
    main()
