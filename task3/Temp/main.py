
import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

if len(sys.argv) < 2:
    print(" ❌ Вкажіть шлях до папки як аргумент командного рядка!")
    print(" ✔ Наприклад: python main.py C:\Users\Pasha\Desktop\Проекти GitHub\goit-algo-hw-04\task3")
    sys.exit(1)

path = sys.argv[1]  # Отримуємо шлях до папки з аргументів командного рядка
print(Fore.YELLOW + f"🔍 Обробка папки: {path}") # шлях переданий скрипту через аргумент командного рядка

# Функція для рекурсивного обходу папки
def parse_folder(folder_path): 
    try:
        folder = Path(folder_path) # Створюємо об'єкт Path з переданого шляху 
        if not folder.exists(): # Перевірка чи існує шлях
            print(Fore.RED + f"❌ Вказаний шлях не існує: {folder_path}")
            return
        if folder.is_file(): # Якщо шлях вказує на файл, а не на папку то виводимо його ім'я
            print(Fore.GREEN + f"📄 {folder.name}")
            return

        for element in folder.iterdir(): # Ітеруємося по елементах папки рекурсивно проходячи всі підпапки
            if element.is_file(): # Якщо елемент є файлом а не папкою, виводимо його ім'я
                print(Fore.GREEN + f"📄 File: {element.name}")
            elif element.is_dir(): # Якщо елемент є папкою, виводимо її ім'я та викликаємо функцію рекурсивно щоб пройтися по її вмісту
                print(Fore.BLUE + f"📁folder: {element.name}")
                parse_folder(element) 

    except Exception as e:
        print(Fore.RED + f"❌ Помилка при обробці '{folder_path}': {e}")

parse_folder(path)