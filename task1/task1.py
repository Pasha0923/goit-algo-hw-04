# завдання 1 - розробити функцію total_salary(path), яка аналізує текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів і повертає загальну та середню суму заробітної плати всіх розробників.


with open('example.txt', 'w', encoding='utf-8') as file:
    file.write("""Alex Korp,5000
Nikita Borisenko,6000
Sitarama Raju,3000 
Jonson Brown,1000
Jamie Jones,6500""")

def total_salary(path):
    total_salary = 0
    salaries = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            
            for line in file:
                try:
                    salary_list = line.strip().split(',') # Перетворюємо рядок у список та розділяємо комою
                    # print(salary_list)
                 
                    salary = float(salary_list[1]) # Отримуємо значення зарплати зі списку 
                    # print(salary) 
                    total_salary += salary
                    print(total_salary)
                    salaries.append(salary) # Добавили в словник значення зарплат
                    print(salaries)
                except (ValueError, IndexError):
                    print(f"❌ Введіть корректний формат: наприклад 'Alex Jackson,3000'")
    except FileNotFoundError:
        print("❌ Файл не знайдено")
    if len(salaries) == 0:
        print("❗ Відсутні дані для розрахунку середнього значення") 
        return 0, 0
    average_summary = total_salary / len(salaries) 
    print(average_summary)
    return total_salary, average_summary
   
total, average = total_salary("example.txt") 
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")



