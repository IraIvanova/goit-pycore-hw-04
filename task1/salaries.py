import files_utilities

def total_salary(path):
    salaries_data = files_utilities.load_data(path)
    cleaned_data = clean_data(salaries_data)
    total_sum = sum(cleaned_data)
    average_salary = total_sum / len(cleaned_data)

    return total_sum, average_salary

def clean_data(salaries_data: list[str]) -> list[float]:
    return [float(employee.split(',')[1].strip()) for employee in salaries_data if employee.strip()]
