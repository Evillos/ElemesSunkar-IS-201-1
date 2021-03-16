#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
print("---Игра---")
print("Камень/Ножницы/Бумага")
app = random.randint(1, 3)
if app == 1:
    gg = "Камень"
elif app == 2:
    gg = "Ножницы"
else:
    gg = "Бумага"
print("1)Камень")
print("2)ножницы")
print("3)Бумага")
try:
    x = int(input("Напиши число:/n> "))
    if x == 1:
        print("")
        print("ты выбрал: камень")
        print("компьютер выиграл: " + str(gg))
        print("")
        if app == 1:
            print("Draw :/")
        elif app == 2:
            print("Ты выиграл! :3")
        else:
            print("Компьютер выиграл\n ты проиграл! :c")
            print("")
    elif x == 2:
        print("")
        print("Ты выбрал: Ножницы")
        print("Компьютер выбрал: " + str(gg))
        print("")
        if app == 1:
            print("Компьютер выиграл\n ты проиграл! :c")
        elif app == 2:
            print("Draw :/")
        else:
            print("Ты выиграл! :3")
            print("")
    elif x == 3:
        print("")
        print("Ты выбрал: бумагу")
        print("компьютер выбрал " + str(gg))
        print("")
        if app == 1:
            print("Ты выиграл! :3")
        elif app == 2:
            print("Компьютер выиграл\n ты проиграл! :c")
        else:
            print("Draw :/")
        print("")
    else:
        print("Выберите цифру: 1/2/3!")
except ValueError:
    print("Ошибка разрешается выбирать только целые числа")


# In[ ]:




