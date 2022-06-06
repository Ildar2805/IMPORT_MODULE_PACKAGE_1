import application.salary as salary
import application.db.people as people
import datetime


def main():
    print(datetime.date.today())
    name = input('Please, write name:')
    employee = people.get_employees(name)
    salary.calculate_salary(employee)


if __name__ == "__main__":
    main()
