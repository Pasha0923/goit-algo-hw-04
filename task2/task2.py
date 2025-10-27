# завдання 2. розробити функцію get_cats_info(path), яка читає текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою та повертає список словників з інформацією про кожного кота.


with open('file.txt', 'w', encoding='utf-8') as file: 
    file.write("""60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5""")
    

def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file: # Ітеруємося по кожному рядку файлу
                try:
                    cat_id , cat_name, cat_age = line.strip().split(',') # Розділяємо рядок на частини за комою щоб отримати id, name та age окремо
                    print(cat_id, cat_name, cat_age)
                    cat_dict = {'id': cat_id,
                                'name': cat_name, 
                                'age': cat_age} # Створюємо словник
                    cats.append(cat_dict) # Додаємо інформацію до списку
                except (ValueError, IndexError):
                    print(f"❌ Некорректний формат рядка: {line.strip()}")
                    continue
        
        return cats
    except FileNotFoundError:
        print("❌ Файл не знайдено")
        return cats

cats_info = get_cats_info("file.txt")
print(cats_info)