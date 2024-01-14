def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Please enter a user name"
        except ValueError:
            return "Please provide both name and phone"
        except IndexError:
            return "Invalid command format"

    return wrapper


def add_handler(name, number):
    contacts[name] = number
    return f"Added name: {name}, phone number: {number}"


def hello_handler():
    return "How can I help you?"


def change_handler(name, number):
    contacts[name] = number
    return f"Changed name: {name}, phone number: {number}"


def phone_handler(name):
    try:
        number = contacts[name]
        return f"Phone number: {number}"
    except KeyError:
        return f"Contact {name} not found"

def main():
    print("Welcome to Contact Assistant!")

    command_handlers = {
        "hello": hello_handler,
        "add": add_handler,
        "change": change_handler,
        "phone": phone_handler,
    }

    while True:
        user_input = input("> ").lower()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "show all":
            print(contacts)
            continue

        handler_name, *args = user_input.split(" ")
        handler = command_handlers.get(handler_name)
        if handler is not None:
            print(handler(*args))
        else:
            print(f"Unknown command. Available commands: {', '.join(command_handlers.keys())}")

if __name__ == "__main__":
    contacts = {}
    main()
