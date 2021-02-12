import pickle
from hw14 import Employee


def get_employee(file):
    with open(file, "rb") as f:
        employee = pickle.load(f)

        return employee


def main():
    emp = get_employee("../files/employee.pickle")
    print(emp.name)


if __name__ == '__main__':
    main()
