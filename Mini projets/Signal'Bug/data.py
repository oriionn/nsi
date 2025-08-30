from csv import DictReader, DictWriter
from id import generate_id_report
from os import remove, path

def add_report(name: str, email: str, description: str, version: str, screenshots: list[str]):
    """
    Ajouter un rapport de bug à la liste
    """
    file = open("data.csv", "r+")
    data = list(DictReader(file, delimiter=";"))
    item_id = generate_id_report(data)
    item = {
        "id": item_id, "name": name, "email": email, "description": description, "version": version, "screenshots": ",".join(screenshots)
    }

    w = DictWriter(file, item.keys(), delimiter=";")
    w.writerow(item)
    file.close()

def remove_report(id: str):
    """
    Supprimer un rapport de bug à partir de son identifiant
    """
    file = open("data.csv", "r")
    data = list(DictReader(file, delimiter=";"))
    file.close()

    file = open("data.csv", "w")
    first_item = data[0]

    # Supprimer les screenshots uploadés
    id_filter = [screenshots_to_list(d) for d in data if d["id"] == id]
    if len(id_filter) != 0:
        screenshots = id_filter[0]["screenshots"]
        for screenshot in screenshots:
            p = path.join("static", "uploads", screenshot)
            if path.exists(p):
                remove(p)

    # Update CSV
    data = [d for d in data if d["id"] != id]
    w = DictWriter(file, first_item.keys(), delimiter=";")
    w.writeheader()
    w.writerows(data)
    file.close()

def screenshots_to_list(report: dict) -> dict:
    """
    Convertir les screenshots d'un rapport de bug en list à la place d'un str
    """
    report["screenshots"] = report["screenshots"].split(",");
    return report

def get_reports() -> list:
    """
    Récupérer la liste des rapports de bug
    """
    file = open("data.csv")
    data = list(DictReader(file, delimiter=";"))
    data = [screenshots_to_list(d) for d in data]
    return data