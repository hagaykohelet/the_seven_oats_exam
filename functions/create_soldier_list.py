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
        distance = int(solider["מרחק מהבסיס"])
        if check_personal_id(personal_id):
            obj = Solider(personal_id, first_name, last_name, gender, city, distance)

            soliders_list.append(obj)

    return soliders_list


def sort_soldier_by_distance(soldiers: list) -> list:
    length = len(soldiers)
    for i in range(length):
        swapped = False
        for j in range(0, length -i-1):
            if soldiers[j].distance < soldiers[j+1].distance:
                soldiers[j], soldiers[j+1] = soldiers[j+1],soldiers[j]
                swapped = True
        if not swapped:
            return soldiers
    return soldiers


