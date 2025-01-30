from bot_functions import one, two

spisok2 = []
spisok = []
while True:
    print('''
    1. Просмотр списка задач
    2. Добавить задачу
    3. Пометка задачи как выполненной
    4. Удаление задачи
    5. Очистка списка
    6. Пока до встречи''')
    nomer_deistvie = int(input('Введите номер действия: '))

    if nomer_deistvie == 1:
        one(spisok)
    elif nomer_deistvie == 2:
        dobavlenie = input('Введите задачу: ')
        two(spisok, [dobavlenie])
    elif nomer_deistvie == 3:
        completed = [False] * 100
        def three():
            for number, task in enumerate(spisok, 1):
                status = "Выполнена" if completed[number - 1] else "Не выполнена"
                print(f"{number}. {task} - {status}")
            task_number = int(input("Введите номер задачи, чтобы отметить её выполненной: "))
            completed[task_number - 1] = True
            print(f"Задача '{spisok[task_number - 1]}' теперь выполнена.")
        three()
    elif nomer_deistvie == 4:
        def four():
            nomer_thadachi = int(input('введите номер задачи: '))
            spisok.remove(spisok[nomer_thadachi])
        four()
    elif nomer_deistvie == 5:
        def five():
            spisok = []
            print(spisok)
        five()
        break
    elif nomer_deistvie == 6:
        def six():
            print('пока до встречи')
        six()
        break