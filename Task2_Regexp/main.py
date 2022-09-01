import re
import csv

pattern = r'(\+7|8)\s*(\(?(\d{3})\)?) ?-?(\d{3})-?(\d{2})-?(\d{2})(\s?)\(?(доб.)?\s*(\d*)\)?'
substitution = r'+7(\3)\4-\5-\6\7\8\9'


def names(raw_list):
    for contact in raw_list[1:]:
        full_name = (contact[0] + ' ' + contact[1] + ' ' + contact[2]).strip()
        full_name_list = full_name.split(' ')
        if len(full_name_list) == 3:
            contact[0], contact[1], contact[2] = full_name_list[0], full_name_list[1], full_name_list[2]
        elif len(full_name_list) == 2:
            contact[0], contact[1] = full_name_list[0], full_name_list[1]
    return raw_list


def phones(raw_list, pattern, substitution):
    for contact in raw_list:
        contact[5] = re.sub(pattern, substitution, contact[5])
    return raw_list


def doubles(raw_list):
    count = 1
    contacts_list_cycle = raw_list[1:]
    for contact in raw_list[1:]:
        for contact_compare in contacts_list_cycle[count:]:
            if contact[0] == contact_compare[0] and contact[1] == contact_compare[1]:
                if contact[2] == '':
                    contact[2] = contact_compare[2]
                if contact[3] == '':
                    contact[3] = contact_compare[3]
                if contact[4] == '':
                    contact[4] = contact_compare[4]
                if contact[5] == '':
                    contact[5] = contact_compare[5]
                if contact[6] == '':
                    contact[6] = contact_compare[6]
                raw_list.remove(contact_compare)
        count += 1
    return raw_list


def improvement(file, pattern, substitution):
    with open(file) as f:
        rows = csv.reader(f, delimiter=',')
        raw_list = list(rows)

    names_list = names(raw_list)
    names_phones_list = phones(names_list, pattern, substitution)
    final_contacts_list = doubles(names_phones_list)

    with open('phonebook.csv', 'w') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_contacts_list)


if __name__ == '__main__':
    improvement('phonebook_raw.csv', pattern=pattern, substitution=substitution)
