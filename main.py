from pprint import pprint
import csv
import re


# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)-\3-\4-\5 \6\7'


# TODO 1: выполните пункты 1-3 ДЗ
# Поместить ФИО по местам, привести телефоны в единый формат
new_list = list()
for item in contacts_list:
    full_name = ' '.join(item[:3]).split(' ')
    result = [full_name[0], full_name[1], full_name[2], item[3], item[4],
              re.sub(PHONE_PATTERN, PHONE_SUB, item[5]), item[6]]
    new_list.append(result)


# Убрать дублирующие записи и пустые строки
for i in new_list:
    for j in new_list:
        if i[0] == j[0] and i[1] == j[1]:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]

    result_list = list()
    for info in new_list:
        if info not in result_list:
            result_list.append(info)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
# Вместо contacts_list подставьте свой список
    datawriter.writerows(result_list)