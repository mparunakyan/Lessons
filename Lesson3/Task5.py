def calc(input_string):
    global calculated_sum  # объявляем глобальную переменную, чтобы не перебрасывать лишнюю переменную
    current_string_sum = 0
    for i in input_string:
        if i.isdigit():
            current_string_sum += int(i)
            calculated_sum += int(i)
        else:
            if i.lower() == "q":  # ищем при вводе символ q либо Q, что задаст завершение операции суммирования
                print("You entered Q(q) and left process")
                print(f"{current_string_sum}({calculated_sum})")
                return True
    print(f"{current_string_sum}({calculated_sum})")
    return False


calculated_sum = 0
while True:
    my_string = input("Please enter numeric or Q to exit: ").split()
    # print(my_string)
    ret = calc(my_string)
    # print(calculated_sum)
    if ret:
        print(f"Final sum is {calculated_sum}")
        break
