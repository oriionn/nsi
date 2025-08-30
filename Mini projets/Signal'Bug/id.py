from datetime import datetime
from random import randint

def generate_id() -> str:
    """
    Générer un identifiant unique pour un fichier uploadé
    """
    date = int(datetime.timestamp(datetime.now()) * 1000)
    id = hex(date)[2:]
    id += hex(randint(256, 256*2^8))[2:]
    return id;

def generate_id_report(reports: list) -> int:
    """
    Générer un identifiant pour un rapport de bug
    """
    if len(reports) == 0:
        return 1
    reports = sorted(reports, key=lambda x:int(x["id"]), reverse=True)
    last_id = int(reports[0]["id"])
    return last_id + 1