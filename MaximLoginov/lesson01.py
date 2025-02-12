# 1$ = 101,91 руб 

while True:


    a = 0
    type_money = {"Российский рубль" : 0.009812, "Доллар" : 1.0, "Евро" : 1.02, "Юань" : 0.136387, "Тенге" : 0.001895, "Лира" : 0.0282209, "Дирхам ОАЭ" : 0.272259, "Гривна" : 0.023649, "Беллорусский рубль" : 0.287389}
    print("(Российский рубль, Доллар, Евро, Юань, Тенге, Лира, Дирхам ОАЭ, Гривна, Беллорусский рубль)")
    money_one_text = input("Выберите валюту в которую будете переводить и впишите сюда: ")

    if money_one_text == "Российский рубль":
        a = type_money["Российский рубль"]
    if money_one_text == "Доллар":
        a = type_money["Доллар"]
    if money_one_text == "Евро":
        a = type_money["Евро"]
    if money_one_text == "Юань":
        a = type_money["Юань"]
    if money_one_text == "Тенге":
        a = type_money["Тенге"]
    if money_one_text == "Лира":
        a = type_money["Лира"]
    if money_one_text == "Дирхам ОАЭ":
        a = type_money["Дирхам ОАЭ"]
    if money_one_text == "Гривна":
        a = type_money["Гривна"]
    if money_one_text == "Беллорусский рубль":
        a = type_money["Беллорусский рубль"]

    money_two_text = int(input("Выберите количество долларов из которых будете переводить и впишите сюда: "))

    b = money_two_text
    answer = b/a
    print("Получилось:", answer)
    print("")