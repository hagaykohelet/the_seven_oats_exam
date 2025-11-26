import csv
from classes.solider import Solider


def read_csv(path):
    rows = []
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


def check_personal_id(num) -> bool:
    check_num = num
    while check_num >= 10:
        check_num //= 10
    if check_num == 8:
        return True
    else:
        return False


def create_solider(path) -> list[dict]:
    soliders_list = []
    soliders = read_csv(path)
    for solider in soliders:
        personal_id = int(solider["מספר אישי"])
        first_name = solider["שם פרטי"]
        last_name = solider["שם משפחה"]
        gender = solider["מין"]
        city = solider["עיר מגורים"]
        distance = solider["מרחק מהבסיס"]
        if check_personal_id(personal_id):
            obj = Solider(personal_id=personal_id, first_name=first_name, last_name=last_name,
                          gender=gender, city=city, distance=distance)

            soliders_list.append(obj)

    return soliders_list


CSV = "../data_solider/hayal_300_no_status.csv"
print(create_solider(CSV))
