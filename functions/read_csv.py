import csv
from classes.solider import Solider


def read_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


def create_solider(path):
    soliders_list = []
    soliders = read_csv(path)
    for solider in soliders:
        personal_id = solider["מספר אישי"]
        first_name = solider["שם פרטי"]
        last_name = solider["שם משפחה"]
        gender = solider["מין"]
        city = solider["עיר מגורים"]
        distance = solider["מרחק מהבסיס"]
        obj = Solider(personal_id=personal_id, first_name=first_name, last_name=last_name,
                      gender=gender, city=city, distance=distance)

        soliders_list.append(obj)

    return soliders_list
