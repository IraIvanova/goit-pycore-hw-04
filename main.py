# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import task1.salaries as salaries
import task2.cats_info as cats_information


def print_hi():
    total, average = salaries.total_salary("task1/salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    cats_info = cats_information.get_cats_info("task2/cats.txt")
    print(cats_info)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
