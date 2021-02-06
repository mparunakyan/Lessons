class MyException(Exception):
    def __init__(self, message):
        self.message = message


a = []
while True:
    b = input("Please enter next number: ")
    try:
        if not b.replace("-", "").replace(",", "").replace(".", "").isdigit():
            raise MyException(f"{25 * '_'}Exception: no digit found{25 * '_'}")
    except (ValueError, MyException) as error:
        print(error)
        if b == "stop":
            break
    else:
        a.append(b)
        print(f"Our list contains: {a}")
print(5 * "*")
print(f"Finalizing program: our list contains {a}")
