import random #importing libraries

print("Выберите ваш язык\n" 
    "choose your language\n" 
    "1- English\n" 
    "2 - Русский") # We give the user a choice of language

choise_lan = int(input())

if choise_lan == 1:

    # Welcome the user and tell the rules
    print ("Welcome to the game guess the number \n")
    print("The rules are as follows:\n")
    print("The computer guesses one number from 1 to 100\n")
    print("Your task is to guess this number \n")
    print("The computer will give you hints\n")

    # Asking the user if he is ready to play
    confirm = str(input("Are you ready to play? yes or no?\n"))


    if confirm.lower() == 'yes': # Starting the game
        the_hidden_number = random.randint(1 , 100) # Guessing a number
        print("You have started the game\n")
        print ("The number is guessed, the game begins, start typing \n") # We write that we have started the game

        pop = None # Setting an empty pop variable

        while pop != the_hidden_number: # Running an infinite loop until the number is guessed

            pop = int(input("Your number\n")) # asking the user for the number
            
            # We compare the number of the user and the hidden number, and if it is less than the hidden number, we write to the user about it
            if pop < the_hidden_number :
                print("Your number is less than the desired one")

            # We compare the user's number and the hidden one, and if it is more than the hidden one, we write to the user about it
            elif pop > the_hidden_number :
                print("Your number is higher than the number you were wondering about")

            # Congratulations to the user if he guessed the number
            else:
                 print("Congratulations!🎉 You guessed the number:" , [the_hidden_number])

        # Asking the user if he wants to play again
        replay = str(input("Do you want to play more?"))
            
        # If he wants to try again, then run the game again
        if replay == "yes":
            print ("A new game has begun")
            
        # If not, end the game
        else:
            exit()

    # saying goodbye to the user
    else:
        exit("goodbye")

if choise_lan == 2:

    # Приветствуем пользователя и рассказываем правила
    print("Приветствуем вас в игре угадай число\n") 
    print("Правила таковы:\n")
    print("Компьютер загадывает одно число от 1 до 100\n")
    print("Ваша задача угадать это число\n")
    print("Компьютер будет давать вам подсказки\n")

    # Спрашиваем пользователя готов ли он играть
    confirm = str(input("Готовы ли вы играть? да или нет?\n"))


    if confirm.lower() == 'да': # Начинаем игру
        the_hidden_number = random.randint(1 , 100) # Загадываем число
        print("Вы начали игру\n")
        print("Число загадано игра начинается начинайте вводить\n") # Пишем что начали игру

        pop = None # Задаем пустую переменную pop

        while pop != the_hidden_number: # Запускаем бесконечный цикл пока число не будет угадано

            pop = int(input("Ваше число\n")) # спрашиваем число у пользователя
            
            # Сравниваем число пользователя и загаданное и если оно меньше загаданного пишем пользователю об этом
            if pop < the_hidden_number : 
                print("Ваше число меньше загаданного")

            # Сравниваем число пользователя и загаданное и если оно больше загаданного пишем пользователю об этом
            elif pop > the_hidden_number :
                print("Ваше число больше загаданного")

            # Поздравляем пользователя если он угадал число
            else:
                print("Поздравляю!🎉 Вы угадали число:" , [the_hidden_number])

            # Спрашиваем пользователя хочет ли он сыграть еще раз
            replay = str(input("Хотите сыграть еще?"))
            
            # Если хочет еще раз то запускаем игру еще раз
            if replay == "да":
                print("Новая игра началась")
            
            # Если нет заканчиваем игру
            else:
                exit()

    # прощаемся с пользователем
    else:
        exit("досвидания")