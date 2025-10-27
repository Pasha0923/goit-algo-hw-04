
# Парсер команд. Частина, яка відповідає за розбір введених користувачем рядків, виділення з рядка ключових слів та модифікаторів команд.
def parse_input(user_input): 
    cmd, *args = user_input.split() 
    cmd = cmd.strip().lower() 
    return cmd, *args
# Функція для додавання контакту до словника контактів
def add_contact(args, contacts): # Функція приймає args (який є списком і містить ім'я та телефонний номер) та словник контактів contacts
    if len(args) != 2:  
        return "❌Error: 'add' command must include exactly two arguments: name and phone" 
    name, phone = args # Розпаковуємо список args (ім'я та телефонний номер) на змінні name та phone
    contacts[name] = phone # Додаємо новий контакт до словника contacts, де ім'я є ключем, а телефонний номер є значенням
    return f" ✔ Contact '{name} {phone}' has been added to list."  

#Функція для зміни номера телефону існуючого контакту
def change_contact(args, contacts): 
    if len(args) != 2: # Перевіряємо чи передано саме два аргументи
        return "❌Error: 'change' command must include exactly two arguments: name and new phone" 
    name, new_phone = args 
    if name in contacts: 
        contacts[name] = new_phone 
        return f" ✔ Contact '{name}' has been updated with new phone number '{new_phone}'" 
    else:
        return f"❌ Error: Contact '{name}' not found" 

#Функція для показу номера телефону існуючого контакту
def show_phone(args, contacts):
    if len(args) != 1: # Перевіряємо чи передано саме один аргумент
        return "❌Error: 'phone' command must include exactly one argument: name" 
    name = args[0] 
    if name in contacts:
        phone = contacts[name] 
        return f" ✔ Contact '{name}' has phone number '{phone}'"  
    else:
        return f"❌ Error: Contact '{name}' not found"  

#Функція для показу всіх контактів у словнику
def show_all(contacts):
    if not contacts: 
        return "No contacts stored" 
    result_lines = ["All contacts:"] 
    for name, phone in contacts.items(): 
        result_lines.append(f"{name}: {phone}") 
    return "\n".join(result_lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input: # Перевіряємо чи користувач ввів порожній рядок
                continue # Якщо порожній, пропускаємо ітерацію та запитуємо команду знову
        command, *args = parse_input(user_input) 
        print(f"Command: {command} Arguments: {args}") 
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
           print(add_contact(args, contacts))  
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))       
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
