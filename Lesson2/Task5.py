my_list = [7, 5, 3, 3, 2]
newval = int(input("Please enter new Value: "))
i = 0
while i < len(my_list):
    #print(i)
    if newval <= my_list[i]:
        #print(f"index {i} {newval} < {my_list[i]}")
        i += 1
        if i == len(my_list):
            my_list.append(newval)
            break
    else:
        my_list.insert(i, newval)
        break

print(f"Новое значение вставлено по индексу {i}")
print(f"Обновленный список {my_list}")

