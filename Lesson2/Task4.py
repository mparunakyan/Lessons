my_string = "Однажды русский генерал из гор к Тифлису проезжал синхрофазатрон"
my_string = my_string.split(" ")
for strnum, i in enumerate(my_string):
    print(f"{strnum+1} {i[:10:]}")
