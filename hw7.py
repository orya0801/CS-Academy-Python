"""
    Результат работы программы находится в файле /files/output.txt
"""


# Чтение файла и преобразование файла в двумерный список
def read_file_line_by_line(path):
    with open(path, 'r') as f:
        strings = f.read().splitlines()

    list_params = []

    for string in strings:
        list_params.append(string.split(':'))

    return list_params


# Выбираем данные из нужного столбца двумерного списка
def get_column(list_params, n):
    column = []

    for l in list_params:
        column.append(l[n])

    return column


# Считаем количество пользователей каждой оболчки
def count_users(column):
    column_set = set(column)
    count_dict = {}

    for elem in column_set:
        count = column.count(elem)
        count_dict.update({elem: count})

    return count_dict


# Формируем строку из словаря и записываем ее в файл
def print_result_to_file_1(res_dict):
    final_str = "("

    for v, k in res_dict.items():
        final_str += " {0} - {1} ;".format(k, v)

    final_str += " )"

    with open("files/output.txt", "w") as f:
        f.write(final_str)


def get_dict_groups_with_users_uid(group, passwd):
    res_dict = {}

    for elem in group:
        group_name = elem[0]
        group_id = elem[2]
        users = elem[3].split(',')
        users_uids = []

        for elem_pswd in passwd:
            if group_id == elem_pswd[3] or elem_pswd[0] in users:
                users_uids.append(elem_pswd[2])

        res_dict.update({group_name: users_uids})

    return res_dict


def print_result_to_file_2(group_users_uids):
    res_str = "("

    for k, v in group_users_uids.items():
        v_str = ','.join(v)
        res_str += f" {k}:{v_str}, "

    res_str += ")"

    with open("files/output.txt", "a") as f:
        f.write(f"\n{res_str}")


def main():
    path_to_passwd = "files/etc/passwd"
    path_to_group = "files/etc/group"

    passwd = read_file_line_by_line(path_to_passwd)
    group = read_file_line_by_line(path_to_group)

    # Оболчки пользователей
    passwd_shell = get_column(passwd, 6)
    shell_users = count_users(passwd_shell)
    print_result_to_file_1(shell_users)

    # uid-ы пользователей всех групп файла /etc/group
    group_users_uid = get_dict_groups_with_users_uid(group, passwd)
    print_result_to_file_2(group_users_uid)


if __name__ == "__main__":
    main()
