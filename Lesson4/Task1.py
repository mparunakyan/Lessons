from sys import argv


def calculate_salary(my_values):
    salary = my_values[0] * my_values[1] + my_values[2]
    return salary


try:
    script_name, rate, hours, bonus = argv
    my_params = [int(rate), int(hours), int(bonus)]
    print(f"Total income includes bonuses is {calculate_salary(my_params)} USD")
except ValueError as error:
    print(f"Error value or missed parameters - {error}")
