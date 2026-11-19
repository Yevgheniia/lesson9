
pillow_price = 650
blanket_price = 1700
lamp_price = 500
keychain_price = 60

pillow_quantity = 0
blanket_quantity = 0
lamp_quantity = 0
keychain_quantity = 0

print("Меню дій: ")
print("1 додати товар ")
print("2 видалити товар ")
print("3 очистити кошик ")
print("4 показати вміст кошики та суму покупки ")
print("5 вихід ")

while True:


    choise = int(input("Виберіть дію: "))

    if choise < 1 or choise > 5:
        print("Ви ввели неправильний код меню.")
        continue
    elif choise == 5:
        break
    elif choise == 1:
        product_choice = input("Введіть назву товару ● подушка  ● ковдра ● лампа ● брелок: ")
        if product_choice == "подушка":
            pillow_quantity += int(input(f"Введіть кількість {product_choice}"))
        elif product_choice == "ковдра":
            blanket_quantity += int(input(f"Введіть кількість {product_choice}"))
        elif product_choice == "лампа":
            lamp_quantity += int(input(f"Введіть кількість {product_choice}"))
        elif product_choice == "брелок":
            keychain_quantity += int(input(f"Введіть кількість {product_choice}"))
        else:
            print("Ви ввели невірний товар")
            continue
    elif choise == 2:
        product_choice = input("Введіть назву товару для видалення ● подушка  ● ковдра ● лампа ● брелок: ")
        if product_choice == "подушка":
            pillow_quantity -= int(input(f"Введіть кількість {product_choice} для видалення"))
        elif product_choice == "ковдра":
            blanket_quantity -= int(input(f"Введіть кількість {product_choice} для видалення"))
        elif product_choice == "лампа":
            lamp_quantity -= int(input(f"Введіть кількість {product_choice} для видалення"))
        elif product_choice == "брелок":
            keychain_quantity -= int(input(f"Введіть кількість {product_choice} для видалення"))
        else:
            print("Ви ввели невірний товар")
            continue
    elif choise == 3:
        print("Корзина очищена")
        pillow_quantity = 0
        blanket_quantity = 0
        lamp_quantity = 0
        keychain_quantity = 0
    else:
        total_sum = pillow_quantity * pillow_price + blanket_quantity * blanket_price + lamp_quantity * lamp_price + keychain_quantity * keychain_price
        print(f"У Вас в кошику \n подушка - {pillow_quantity} шт на суму {pillow_quantity * pillow_price}  грн"
              f"\n ковдра - {blanket_quantity} шт на суму {blanket_quantity * blanket_price} грн"
              f"\n лампа - {lamp_quantity} шт на суму {lamp_quantity * lamp_price } грн "
              f"\n брелок - {keychain_quantity} шт на суму {keychain_quantity * keychain_price} грн"
              f"\n Загальна сума: {total_sum} грн")
