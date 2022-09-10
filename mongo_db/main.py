import argparse
import sys
from functools import wraps

from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017")
db = client.myAddressBook.users

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--phone', nargs='+')
parser.add_argument('--email')
parser.add_argument('--birthday')
parser.add_argument('--address')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
_id = my_arg.get('id')
name = my_arg.get('name')
phone = my_arg.get('phone')
email = my_arg.get('email')
birthday = my_arg.get('birthday')
address = my_arg.get('address')


class ExceptionValidation(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ExceptionValidation(f'Вхідні данні не валідні: {func.__name__}{args}')
        result = func(*args)
        return result

    return wrapper


# def find_by_id(_id):
#     result = db.insert_one({"_id": ObjectId(_id)})
#     return result

def find_by_id(_id):
    result = db.find_one({"_id": ObjectId(_id)})
    return result


@validate
def create(name, phone, email, birthday, address):
    result = db.insert_one({
        "name": name,
        "phone": phone,
        "email": email,
        "birthday": birthday,
        "address": address
    })
    return find_by_id(result.inserted_id)


@validate
def find():
    return db.find()


@validate
def update(_id, name, phone, email, birthday, address):
    r = db.update_one({"_id": ObjectId(_id)}, {
        "$set": {
            "name": name,
            "email": email,
            "phone": phone,
            "birthday": birthday,
            "address": address
        }
    })
    print(r)
    return find_by_id(_id)


@validate
def remove(_id):
    r = db.delete_one({"_id": ObjectId(_id)})
    return r


def main():
    try:
        match action:
            case 'create':
                r = create(name, phone, email, birthday, address)
                print(r)
            case 'find':
                r = find()
                [print(el) for el in r]
            case 'update':
                r = update(_id, name, phone, email, birthday, address)
                print(r)
            case 'remove':
                r = remove(_id)
                print(r)
            case _:
                print('Unknowns command')
    except ExceptionValidation as err:
        print(err)


if __name__ == '__main__':
    main()
    # print(find_by_id("631a76cce0afa9d8edab50ea"))
