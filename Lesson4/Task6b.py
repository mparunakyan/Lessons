from itertools import cycle

ind = 1
try:
    my_phrase = input(f"Please enter phrase: ")
    last_number = int(input(f"Please enter last number: "))
    for el in cycle(my_phrase):
        print(el)
        ind += 1
        if ind > last_number:
            break
except ValueError as error:
    print(f"Error number or char entered with code {error}")

# Variation 2 based on iter and next
# iter = cycle(my_phrase)
# for i in range(last_number):
#     print(next(iter))