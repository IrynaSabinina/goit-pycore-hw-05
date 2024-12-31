def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Please provide the required arguments."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"
    return inner

# Функція для додавання контакту
@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError  # Генеруємо помилку, якщо немає достатньо аргументів
    name, phone = args
    if name in contacts:
        return f"Contact with name '{name}' already exists. Use 'change' to update the phone."
    contacts[name] = phone
    return f"Contact '{name}' added."

# Функція для зміни контактного номера
@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError  # Генеруємо помилку, якщо немає достатньо аргументів
    name, new_phone = args
    if name not in contacts:
        raise KeyError  # Генеруємо помилку, якщо контакт не знайдений
    contacts[name] = new_phone
    return f"Contact '{name}' updated."

# Функція для показу телефонного номера
@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise ValueError  # Генеруємо помилку, якщо не вказано ім'я
    name = args[0]
    if name not in contacts:
        raise KeyError  # Генеруємо помилку, якщо контакт не знайдений
    return f"{name}'s phone: {contacts[name]}"

# Функція для показу всіх контактів
def show_all(contacts):
    if not contacts:
        raise ValueError  # Генеруємо помилку, якщо немає контактів
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result

# Функція для обробки введення команд
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")
    print("You can use the following commands:")
    print("'add [name] [phone]' - Add a new contact.")
    print("'change [name] [new phone]' - Change the phone number of an existing contact.")
    print("'phone [name]' - Show the phone number of a specific contact.")
    print("'all' - Show all contacts.")
    print("'exit' or 'close' - Exit the program.")
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue  # Skip if input is empty

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) < 2:  # Check if name or phone is missing
                print("Give me name and phone please.")
            else:
                print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            if len(args) < 1:  # Check if name is missing
                print("Specify the name.")
            else:
                print(show_phone(args, contacts))
        elif command == "all":
            # No need to use the input_error decorator here
            try:
                print(show_all(contacts))
            except ValueError:
                print("No contacts found.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
