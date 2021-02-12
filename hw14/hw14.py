"""
    Модуль pickle:

    Преимущества:
    1. Реализует эффективную сереализацию и десериализацю объектов Python в поток байтов.

    Недостатки:
    1. Плохо защищен. Необходимо быть уверенным в том, какие данные распаковываются.
    2. Формат, в котором записываются объекты, не читаем для человека.
"""

import pickle


class Employee:
    def __init__(self, name, phone, salary=10000):
        self.name = name
        self.phone = phone
        self.salary = salary

    def print_salary_info(self):
        print("Employee {} gets {} Rubles".format(self.name, self.salary))

    def add_salary(self, delta=5000):
        self.salary = self.salary + delta

    def add(self, other_empl):
        new_name = self.name + "&" + other_empl.name
        new_phone = str(round((int(self.phone) + int(other_empl.phone)) / 2))
        new_salary = self.salary + other_empl.salary
        return Employee(new_name, new_phone, new_salary)

    __add__ = add

    def __del__(self):
        print(self.name + " is FIRED!!!")


def dump_employee(file, employee):
    with open(file, 'wb') as f:
        pickle.dump(employee, f)


def main():
    Mary = Employee("Mary", "89214118060")
    dump_employee("../files/employee.pickle", Mary)


if __name__ == '__main__':
    main()
