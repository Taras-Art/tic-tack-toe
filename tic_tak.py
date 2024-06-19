def game():
    ground = [
        [" ", "|", " ", "|", " "],
        ["-", "|", "-", "|", "-"],
        [" ", "|", " ", "|", " "],
        ["-", "|", "-", "|", "-"],
        [" ", "|", " ", "|", " "],
    ]

    turns = {0: {1: 0, 2: 2, 3: 4}, 2: {4: 0, 5: 2, 6: 4}, 4: {7: 0, 8: 2, 9: 4}}
    flag = True
    cnt = 0
    total_x = []
    total_zero = []
    all_step_user = []
    winner_combat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7],
    ]
    choise_sumbols = input("Кем будешь играть?")
    if choise_sumbols == "0":
        cnt += 1
    elif choise_sumbols != "0" and choise_sumbols != "X":
        print("Будешь тогда Крестом!")

    # Вывод поля
    def print_ground():
        for i in range(len(ground)):
            print(*ground[i])

    # Определение победителя
    def winner(why):
        for el in winner_combat:
            cnt = 0
            for turn in why:
                if turn in el:
                    cnt += 1
                    if cnt == 3:
                        print_ground()
                        return True

    while flag:
        # Выводим поле
        print_ground()

        user_step = input()
        # проверяем был ли такой ход и запускаем основную программу
        if user_step.isdigit():
            user_step = int(user_step)
            if user_step not in all_step_user:
                all_step_user.append(user_step)
                if cnt % 2 == 0:
                    add = "X"
                    total_x.append(user_step)
                else:
                    add = "0"
                    total_zero.append(user_step)
                # Добавляем ход на поле
                for a, b in turns.items():
                    if user_step in b:
                        ground[a][b[user_step]] = add
            else:
                print("Такое уже было")
            # Определяем победителя
            if winner(total_x):
                print("Победа за Крестами!")
                flag = False
            elif winner(total_zero):
                print("Победа за Нулями!")
                flag = False

            cnt += 1

            if len(all_step_user) == 9:
                print("Ну тут ничья")
                flag = False
        else:
            print("Только цифры!")


ask = input("Сыграем?")
while ask.lower() != "нет":
    game()
    ask = input("Сыграем?")
