from itertools import count


try:
    start_number = int(input(f"Please enter start number: "))
    last_number = int(input(f"Please enter last number: "))
    for el in count(start_number):
        if el > last_number:
            break
        else:
            print(el)
except ValueError as error:
    print(f"Error number or char entered with code {error}")
print("*" * 25)
