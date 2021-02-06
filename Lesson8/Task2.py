class MyException(Exception):
    def __init__(self, message):
        self.message = message


try:
    a = int(input("Please enter divisible argument: "))
    b = int(input("Please enter divider argument: "))
    if b == 0:
        raise MyException("Exception: 0 divider found")
except (ValueError, MyException) as error:
    print(error)
else:
    print(a / b)
