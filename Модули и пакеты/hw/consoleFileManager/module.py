#Модуль для консольного файлового менеджера
import os
import shutil
import platform

"""
Функция создания папки
"""

def createFolder():
    #Ввод наименования папки
    dirName = input('Введите название папки: ')
    try:
        os.mkdir(dirName)
        print(f'Папка {dirName} создана успешно')
    except FileExistsError:
        print()
    except Exception as e:
        print(f"Ошибка: {e}")

def deleteObj():
    try:
        nameToDelete = input('Введите название папки или файла для удаления: ')
        if os.path.isfile(nameToDelete):
            os.remove(nameToDelete)
            print(f"Файл '{nameToDelete}' удален.")
        
        elif os.path.isdir(nameToDelete):
            os.rmdir(nameToDelete)
            print(f"Папка '{nameToDelete}' удалена.")
        else:
            print(f"'{nameToDelete}' не существует.")
    except Exception as e:
        print(f"Ошибка: {e}")

def copyFile():
    source_name = input("Введите название копируемого файла/папки: ")
    # проверка на существования файла/папки
    try:
        # os.path.isfile(source_name) проверка на истинность формата файла
        if os.path.isfile(source_name):
            destination_name = input("Введите новое название файла, которого вы хотите скопировать : ")
            shutil.copy(source_name, destination_name)
            print(f"Файл '{source_name}' скопирован в '{destination_name}' успешно.")
        # os.path.isdir(source_name) проверка на истинность формата папки
        elif os.path.isdir(source_name):
            destination_name = input("Введите новое название папки, которого вы хотите скопировать : ")
            shutil.copytree(source_name, destination_name)
            print(f"Directory '{source_name}' has been copied to '{destination_name}' successfully.")
        else:
            print(f"'{source_name}' не существует.")
    except Exception as e:
        print(f"Ошибка программы: {e}")

def getInfo():
    # Получаем текущую рабочую директорию
    current_directory = os.getcwd()

    # Получаем список всех объектов в директории
    contents = os.listdir(current_directory)

    # Выводим содержимое
    for item in contents:
        print(item)

def getDirInfo():
    import os
    # Получаем текущую рабочую директорию
    current_directory = os.getcwd()

    # Получаем список всех объектов в директории
    contents = os.listdir(current_directory)

    # Фильтруем только папки
    folders = [item for item in contents if os.path.isdir(os.path.join(current_directory, item))]

    # Выводим только папки
    for folder in folders:
        print(folder)

def getFileInfo():
    import os
    # Получаем текущую рабочую директорию
    current_directory = os.getcwd()

    # Получаем список всех объектов в директории
    contents = os.listdir(current_directory)

    # Фильтруем только файлы
    folders = [item for item in contents if os.path.isfile(os.path.join(current_directory, item))]

    # Выводим только файлы
    for folder in folders:
        print(folder)

def getOsInfo():
    #Выводит информацию об операционной системе.
    print("Информация об операционной системе:")
    print(f"Система: {platform.system()}")  # e.g., Windows, Linux, Darwin (macOS)
    print(f"Версия ОС: {platform.release()}")  # Версия ОС (e.g., 10, 22.04.1)
    print(f"Полная версия: {platform.version()}")  # Детали сборки
    print(f"Архитектура: {platform.architecture()[0]}")  # 64-bit или 32-bit
    print(f"Имя компьютера: {platform.node()}")  # Сетевое имя устройства
    print(f"Процессор: {platform.processor()}")  # Модель процессора

    # Дополнительная информация для Linux/macOS
    if platform.system() == "Linux":
        print(f"Дистрибутив: {platform.freedesktop_os_release().get('PRETTY_NAME', 'Неизвестно')}")
    elif platform.system() == "Darwin":
        print(f"macOS версия: {platform.mac_ver()[0]}")

def showCreator():
    # Вывод информации студента
    developer_info = {
        "Автор": "Хё-Кю Шин",
        "Версия программы": "1.0.0",
        "Дата релиза": "20.04.2025",
        "Контактный email": "example@mail.ru",
        "GitHub": "github.com/tastychocopie",
        "Лицензия": "ДЗ-шная программа",
    }

    print("=== Информация о разработчике ===")
    for key, value in developer_info.items():
        print(f"{key}: {value}")


def runQuiz():
    #Запускает викторину с вопросами и вариантами ответов
    questions = [
        {
            "question": "Какая столица Франции?",
            "options": ["Берлин", "Мадрид", "Париж", "Рим"],
            "correct_answer": 2  # Индекс правильного ответа (начиная с 0)
        },
        {
            "question": "Какой язык программирования самый популярный в 2025 году?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "correct_answer": 1
        },
        {
            "question": "Сколько планет в Солнечной системе?",
            "options": ["7", "8", "9", "10"],
            "correct_answer": 1
        }
    ]

    score = 0

    print("Добро пожаловать в викторину! Выберите номер правильного ответа.\n")

    for idx, question_data in enumerate(questions, 1):
        print(f"Вопрос {idx}: {question_data['question']}")
        for i, option in enumerate(question_data["options"], 1):
            print(f"{i}. {option}")

        # Проверка ввода пользователя
        while True:
            try:
                user_answer = int(input("Ваш ответ (1-4): ")) - 1  # Переводим в 0-based индекс
                if 0 <= user_answer < len(question_data["options"]):
                    break
                else:
                    print("Пожалуйста, введите число от 1 до 4!")
            except ValueError:
                print("Ошибка! Введите число.")

        # Проверка правильности ответа
        if user_answer == question_data["correct_answer"]:
            print("✅ Правильно!\n")
            score += 1
        else:
            correct_option = question_data["options"][question_data["correct_answer"]]
            print(f"❌ Неверно! Правильный ответ: {correct_option}\n")

    # Вывод итогового результата
    total_questions = len(questions)
    print(f"=== Викторина завершена ===")
    print(f"Ваш результат: {score} из {total_questions}")
    print(f"Процент правильных ответов: {int((score / total_questions) * 100)}%")


def bankAccount():
    balance = 0
    history = []

    while True:
        print("\nТекущий баланс:", balance)
        print("1. Пополнить счет")
        print("2. Совершить покупку")
        print("3. История операций")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            amount = float(input("Введите сумму пополнения: "))
            balance += amount
            history.append(f"Пополнение: +{amount}")
            print(f"Счет пополнен на {amount}. Новый баланс: {balance}")

        elif choice == "2":
            amount = float(input("Введите сумму покупки: "))
            if amount > balance:
                print("Недостаточно средств на счете!")
            else:
                item = input("Введите название покупки: ")
                balance -= amount
                history.append(f"Покупка '{item}': -{amount}")
                print(f"Покупка '{item}' на {amount} выполнена. Остаток: {balance}")

        elif choice == "3":
            print("\nИстория операций:")
            for operation in history:
                print(operation)
            if not history:
                print("История пуста")

        elif choice == "4":
            print("Выход из программы")
            break

        else:
            print("Неверный ввод, попробуйте еще раз")


def changeWorkingDirectory():
    #Функция для смены рабочей директории с обработкой разных форматов путей
    while True:
        print(f"\nТекущая рабочая директория: {os.getcwd()}")
        print("Введите путь к новой директории (абсолютный или относительный)")
        print("Или введите 'exit' для выхода")

        user_input = input("> ").strip()

        if user_input.lower() == 'exit':
            print("Выход из программы")
            break

        try:
            # Обработка домашней директории (~)
            if user_input.startswith('~'):
                path = os.path.expanduser(user_input)
            else:
                path = os.path.abspath(user_input)

            # Проверка существования пути
            if not os.path.exists(path):
                print(f"Ошибка: путь '{path}' не существует!")
                continue

            # Проверка что это директория
            if not os.path.isdir(path):
                print(f"Ошибка: '{path}' не является директорией!")
                continue

            # Смена директории
            os.chdir(path)
            print(f"Успешно! Новая рабочая директория: {os.getcwd()}")

            # Демонстрация содержимого новой директории
            print("\nСодержимое директории:")
            for item in os.listdir():
                print(f" - {'📁' if os.path.isdir(item) else '📄'} {item}")

        except Exception as e:
            print(f"Произошла ошибка: {str(e)}")