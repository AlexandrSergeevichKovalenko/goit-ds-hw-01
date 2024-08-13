from decor import input_error
from classes_for_program import *
import pickle

@input_error(expected_arg_count=2)
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error(expected_arg_count=3)
def change_contact(args, book: AddressBook):
    name, old_number, new_number, *_ = args
    record = book.find(name)
    if record:
        record.edit_phone(old_number, new_number)
        return "Contact updated."
    else:
        return f"There is no person with {name} name"

@input_error(expected_arg_count=1)
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    phone_result = f"{name}'s phone is "
    if record:
        for r in record.phones:
            phone_result += f"{r.value} "
        return phone_result
    else:
        return f"The name {name} you have asked for does not exist."
    
def show_all(book: AddressBook):
    if len(book.data) != 0:
        return str(book)
    else:
        return "There is no data to output."

@input_error(expected_arg_count=2)
def add_birthday(args, book):
    name, birthday_day, *_ = args
    message = "Birthday adedd."
    record = book.find(name)
    if record is None:
        return f"There is no person with {name} name"
    else:
        record.add_birthday(birthday_day)
        return message

@input_error(expected_arg_count=1)
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        return f"There is no person with {name} name."
    else:
        if record.birthday is not None:
            return f"{name}'s birthday is on {record.birthday.value.strftime('%d.%m.%Y')}"
        else:
            return f"{name} does not have a birthday set."

def birthdays(book):
    str = ""
    if len(book.get_upcoming_birthdays()) != 0:
        for i in book.get_upcoming_birthdays():
            str += f"{i}\n"
        return str
    else:
        return f"The data base is empty."

#book instance serialization function using pickle module
def save_data(book: AddressBook, filename = FILENAME):
    with open(filename, "wb") as record_file:
        pickle.dump(book, record_file)

#loading book from file or creating a new book instance if there is no file
def load_data():
    book = AddressBook()
    if FILENAME.is_file():
        with open(FILENAME, "rb") as record_file:
            book = pickle.load(record_file)
    return book









