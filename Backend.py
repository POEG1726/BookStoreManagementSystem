import hashlib
import json
import uuid
import re
from faker import Faker
import random
import string


def read_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


try:
    users = read_json("./users.json")
    books = read_json("./data.json")
except:
    users = {}
    books = {}


# Define the Book class
class Book:
    def __init__(self, name, desc, price, id, author, cover=None):
        self.name = name
        self.author = author
        self.price = price
        self.desc = desc
        self.id = id
        self.cover = cover  # Base64 encoded string if present, None otherwise


class User:
    def __init__(self, name, email, uniqID, pwd, cart=None, permission="user"):
        self.name = name
        self.email = email
        self.uniqID = uniqID
        self.pwd = pwd
        self.cart = cart if cart else {}
        self.permission = permission


def validate_user(email):
    global users
    # users = read_json("./users.json")
    for user in users.values():
        if user["email"] == email:
            return (False, "User Existed")
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    # Match the email against the pattern
    if re.match(pattern, email):
        return (True, "Succeed")
    else:
        return (False, "Format Wrong")


def hash_text(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()


# File operations
def read_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data if isinstance(data, dict) else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def write_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# Manage Books
def add_book(name: str, author: str, price: float, description: str, cover_path=None):
    global books
    # books = read_json("./data.json")
    if name == "" or author == "":
        return False
    for book in books.values():
        if book["name"] == name:
            return False
    id = generate_id()
    book = Book(
        name=name, desc=description, price=price, cover=cover_path, author=author, id=id
    )
    books[id] = book.__dict__
    write_json("./data.json", books)
    return True


def delete_book(book_id):
    global books, users
    try:
        # books = read_json("./data.json")
        del books[book_id]
        for user in users.values():
            if book_id in user["cart"].keys():
                del user["cart"][book_id]
        write_json("./users.json", users)
        write_json("./data.json", books)
        return True
    except:
        return False


def update_book(book_id, name, author, price, description, cover_path=None):
    global books
    try:
        books[book_id] = Book(
            name=name,
            desc=description,
            price=price,
            id=book_id,
            author=author,
            cover=cover_path,
        ).__dict__
        write_json("./data.json", books)
        return True
    except:
        return False


def generate_id():
    random_uuid = uuid.uuid4()
    short_uuid = str(random_uuid).replace("-", "")[:8]
    return short_uuid


def add_user(name: str, email: str, password: str, permission="user"):
    global users
    if name == "" or email == "" or password == "":
        return False
    res = validate_user(email)
    if res[0]:
        pass
    else:
        return False
    # users = read_json("./users.json")
    user_id = generate_id()
    user = User(
        name,
        permission=permission,
        uniqID=user_id,
        email=email.lower(),
        pwd=hash_text(password),
    )
    users[user_id] = user.__dict__
    write_json("./users.json", users)
    return (True, user_id)


def update_user(name: str, email: str, permission: str, cart: dict, user_id: str):
    global users
    try:
        users[user_id] = User(
            name,
            permission=permission,
            uniqID=user_id,
            email=email.lower(),
            cart=cart,
            pwd=look_up_user(user_id)["pwd"],
        ).__dict__
        write_json("./users.json", users)
        return True
    except:
        return False


def delete_user(user_id):
    global users
    try:
        # users = read_json("./users.json")
        del users[user_id]
        write_json("./users.json", users)
        return True
    except:
        return False


def authorization(email, password):
    global users
    # users = read_json("./users.json")
    for user in users.values():
        if user["email"] == email and user["pwd"] == hash_text(password):
            return (True, user["uniqID"])
    return False


def look_up_user(user_id: str):
    global users
    try:
        # users = read_json("./users.json")
        return users[user_id]
    except:
        return False


def look_up_book(book_id: str):
    global books
    try:
        # books = read_json("./data.json")
        return books[book_id]
    except:
        return False


def update_cart(user_id, book_id, quantity=1):
    global users
    try:
        # users = read_json("./users.json")
        # Retrieve the user and book
        user = users[user_id]
        user["cart"][book_id] = quantity
        write_json("./users.json", users)
        # print(f"Added 'book {book_id}' to {user['name']}'s cart.")
        return (True, book_id, quantity)
    except:
        return False


def delete_from_cart(user_id, book_id):
    global users
    try:
        # users = read_json("./users.json")
        user = users[user_id]
        del user["cart"][book_id]
        write_json("./users.json", users)
        return True
    except:
        return False


def generate_fake_users(num_users, randpwd=False):
    def generate_random_password(length=8):
        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choice(characters) for i in range(length))

    try:
        fake = Faker()
        for _ in range(num_users):
            name = fake.name()
            email = fake.email()
            if randpwd:
                password = generate_random_password()
            else:
                password = "1"
            add_user(name, email, password)
        return True
    except:
        return False


def generate_fake_books(num_books):
    try:
        fake = Faker()
        for _ in range(num_books):
            name = ''.join([f'{fake.word()} ' for _ in range(3)])
            author = fake.name()
            price = round(random.uniform(10.00, 100.00), 2)
            description = fake.paragraph(nb_sentences=3)
            add_book(name, author, price, description)
        return True
    except:
        return False


def loadCart(user_id):
    global users
    # users = read_json("./users.json")
    try:
        user = users[user_id]
        return user["cart"]
    except:
        return False


def loadBooks():
    return read_json("./data.json")


def loadUsers():
    return read_json("./users.json")


if __name__ == "__main__":
    pass
