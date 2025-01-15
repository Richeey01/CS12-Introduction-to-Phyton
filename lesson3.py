# a = int(input("Write first number:"))
# b = int(input("Wrote second number:"))
#
# s = a*b
# print(s)


# a = float(input("Write 1 num:"))
# b = float(input("write 2 num:"))
# s = a+b
# s2 = int(s)
# print("a + b =", a, "+", b, "=", s, "=", s2)
#



# a = float(input("Write a num:"))
# b = float(input("Write b num:"))
#
# print(f"a + b = {a} + {b} = {a + b}")


# name = str(input("Write your name:"))
# age = int(input("How old are you?:"))
# hobby = str(input("What is your hobby?:"))
# print(f"Your name is {name}, You're is {age} old, and Your hobby is {hobby}")


money = 100
pop = 3.17
cola = 5.23
glass = 9.79
beer = 7.79

print(f"Сегодня был хороший день и я пошел в кино, и, что бы не заскучать, решил купить попкорн за {pop}$,\n"
      f" колу за {cola}$ и 3D-очки за {glass}$. Купив все это у меня осталось {money - pop - cola - glass}$.\n "
      f"Из-за того, что у меня было хорошее настроение, я решил угостить двух друзей пивом за {beer * 2}$ на двоих.\n"
      f" Итого у меня осталось {money - pop - cola - glass - beer * 2}$\n"
      f"Я решил оставить {round(float((money - pop - cola - glass - (beer * 2)) - int(money - pop - cola - glass - beer * 2)), 2)} цента на благотворительность.")