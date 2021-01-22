# TODO:
# 1. Второй пункт задания


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
def print_result_to_file(res_dict):
    final_str = "("

    for v, k in res_dict.items():
        final_str += " {0} - {1} ;".format(k, v)
    
    final_str += " )"
    
    with open("files/output.txt", "w") as f:
        f.write(final_str)

def get_set_of_group_users(column):
    users_list = []
    
    for elem in column:
        if elem != "":
            users_list.extend(elem.split(','))

    return set(users_list)


def main():
    path_to_passwd = "files/etc/passwd"
    path_to_group = "files/etc/group"

    passwd = read_file_line_by_line(path_to_passwd)
    group = read_file_line_by_line(path_to_group)

    passwd_shell = get_column(passwd, 6)
    shell_users = count_users(passwd_shell)
    print_result_to_file(shell_users)

    group_names_column = get_column(group, 0)
    group_users_column = get_column(group, 3)
    users_set = get_set_of_group_users(group_users_column)


if __name__ == "__main__":
    main()