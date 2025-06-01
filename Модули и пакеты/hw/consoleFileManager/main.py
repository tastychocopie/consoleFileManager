import module

#Консольный файловый менеджер
print('Консольный файловый менеджер 2025 v1')
while True:
    print('INFO: Это меню')
    print('1. Создать папку')
    print('2. Удалить (файл/папку)')
    print('3. Копировать (файл/папку)')
    print('4. Просмотр содержимого рабочей директории')
    print('5. Просмотреть только папки')
    print('6. Просмотреть только файлы')
    print('7. Просмотр информации об операционной системе')
    print('8. Создатель программы')
    print('9. Играть в викторину')
    print('10. Мой банковский счет')
    print('11. Смена рабочей директории')
    print('12. Сохранить содержимое рабочей директории в файл')
    print('13. Выход')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        module.createFolder()
    elif choice == '2':
        module.deleteObj()
    elif choice == '3':
        module.copyFile()
    elif choice == '4':
        module.getInfo()
    elif choice == '5':
        module.getDirInfo()
    elif choice == '6':
        module.getFileInfo()
    elif choice == '7':
        module.getOsInfo()
    elif choice == '8':
        module.showCreator()
    elif choice == '9':
        module.runQuiz()
    elif choice == '10':
        module.bankAccount()
    elif choice == '11':
        module.changeWorkingDirectory()
    elif choice == '12':
        module.saveDirectoryContents()
    elif choice == '13':
        break #exit
    else:
        print('Неверный пункт меню')