import os
import shutil
import pytest
import platform
from io import StringIO
import sys
from unittest.mock import patch

from module import (
    createFolder,
    deleteObj,
    copyFile,
    getInfo,
    getDirInfo,
    getFileInfo,
    getOsInfo,
    showCreator,
    runQuiz,
    bankAccount,
    changeWorkingDirectory
)


# Вспомогательные функции для тестов
def create_test_file(filename, content=""):
    with open(filename, 'w') as f:
        f.write(content)


def create_test_dir(dirname):
    os.makedirs(dirname, exist_ok=True)


# Тесты для функции createFolder
def test_create_folder(tmp_path):
    os.chdir(tmp_path)
    test_dir = "test_folder"

    # Тест создания новой папки
    with patch('builtins.input', return_value=test_dir):
        createFolder()
        assert os.path.exists(test_dir)
        assert os.path.isdir(test_dir)

    # Тест попытки создания существующей папки
    with patch('builtins.input', return_value=test_dir):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            createFolder()
            output = fake_out.getvalue().strip()
            assert "уже существует" in output or output == ""


# Тесты для функции deleteObj
def test_delete_obj(tmp_path):
    os.chdir(tmp_path)

    # Создаем тестовые файл и папку
    test_file = "test_file.txt"
    test_dir = "test_dir"
    create_test_file(test_file)
    create_test_dir(test_dir)

    # Тест удаления файла
    with patch('builtins.input', return_value=test_file):
        deleteObj()
        assert not os.path.exists(test_file)

    # Тест удаления папки
    with patch('builtins.input', return_value=test_dir):
        deleteObj()
        assert not os.path.exists(test_dir)

    # Тест попытки удаления несуществующего объекта
    with patch('builtins.input', return_value="nonexistent"):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            deleteObj()
            output = fake_out.getvalue().strip()
            assert "не существует" in output


# Тесты для функции copyFile
def test_copy_file(tmp_path):
    os.chdir(tmp_path)

    # Создаем тестовые файл и папку
    test_file = "original.txt"
    test_dir = "original_dir"
    create_test_file(test_file, "test content")
    create_test_dir(test_dir)

    # Тест копирования файла
    with patch('builtins.input', side_effect=[test_file, "copy.txt"]):
        copyFile()
        assert os.path.exists("copy.txt")
        with open("copy.txt") as f:
            assert f.read() == "test content"

    # Тест копирования папки
    with patch('builtins.input', side_effect=[test_dir, "copy_dir"]):
        copyFile()
        assert os.path.exists("copy_dir")
        assert os.path.isdir("copy_dir")

    # Тест попытки копирования несуществующего объекта
    with patch('builtins.input', side_effect=["nonexistent", ""]):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            copyFile()
            output = fake_out.getvalue().strip()
            assert "не существует" in output


# Тесты для функций получения информации
def test_get_info(tmp_path, capsys):
    os.chdir(tmp_path)

    # Создаем тестовые файлы и папки
    create_test_file("file1.txt")
    create_test_dir("dir1")

    # Тест getInfo
    getInfo()
    captured = capsys.readouterr()
    assert "file1.txt" in captured.out
    assert "dir1" in captured.out

    # Тест getDirInfo
    getDirInfo()
    captured = capsys.readouterr()
    assert "dir1" in captured.out
    assert "file1.txt" not in captured.out

    # Тест getFileInfo
    getFileInfo()
    captured = capsys.readouterr()
    assert "file1.txt" in captured.out
    assert "dir1" not in captured.out


# Тест для функции getOsInfo
def test_get_os_info(capsys):
    getOsInfo()
    captured = capsys.readouterr()
    assert "Система:" in captured.out
    assert "Версия ОС:" in captured.out
    assert platform.system() in captured.out


# Тест для функции showCreator
def test_show_creator(capsys):
    showCreator()
    captured = capsys.readouterr()
    assert "Автор:" in captured.out
    assert "Хё-Кю Шин" in captured.out
    assert "github.com/tastychocopie" in captured.out


# Тесты для функции runQuiz
def test_run_quiz():
    # Тест с правильными ответами
    inputs = ['3', '2', '2']  # Правильные ответы на вопросы
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            runQuiz()
            output = fake_out.getvalue()
            assert "Ваш результат: 3 из 3" in output
            assert "100%" in output

    # Тест с неправильными ответами
    inputs = ['1', '1', '1']  # Неправильные ответы
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            runQuiz()
            output = fake_out.getvalue()
            assert "Ваш результат: 0 из 3" in output
            assert "0%" in output


# Тесты для функции bankAccount
def test_bank_account():
    # Тест пополнения счета
    inputs = ['1', '100', '4']  # Пополнение на 100 и выход
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bankAccount()
            output = fake_out.getvalue()
            assert "Новый баланс: 100" in output

    # Тест покупки
    inputs = ['1', '200', '2', '150', 'test purchase', '3', '4']  # Пополнение, покупка, история, выход
    with patch('builtins.input', side_effect=inputs):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            bankAccount()
            output = fake_out.getvalue()
            assert "Остаток: 50" in output
            assert "Покупка 'test purchase'" in output
            assert "История операций" in output


# Тесты для функции changeWorkingDirectory
def test_change_working_directory(tmp_path):
    # Создаем тестовую структуру
    test_dir = os.path.join(tmp_path, "test_dir")
    os.makedirs(test_dir)

    # Тест успешной смены директории
    with patch('builtins.input', side_effect=[test_dir, 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            changeWorkingDirectory()
            output = fake_out.getvalue()
            assert "Новая рабочая директория:" in output
            assert "test_dir" in output

    # Тест с несуществующей директорией
    with patch('builtins.input', side_effect=['nonexistent_dir', 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            changeWorkingDirectory()
            output = fake_out.getvalue()
            assert "не существует" in output

    # Тест с указанием файла вместо директории
    test_file = os.path.join(tmp_path, "test_file.txt")
    with open(test_file, 'w') as f:
        f.write("test")

    with patch('builtins.input', side_effect=[test_file, 'exit']):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            changeWorkingDirectory()
            output = fake_out.getvalue()
            assert "не является директорией" in output