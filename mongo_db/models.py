from mongoengine import *


# connect(host="mongodb+srv://goitlearn:<password>@cluster0.4gtzf39.mongodb.net/?retryWrites=true&w=majority")
connect(host='mongodb://localhost:27017/Contacts')


class User(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    meta = {'allow_inheritance': True}


class TextPost(Post):
    birthday = StringField()
    address = StringField()


class LinkPost(Post):
    email = StringField()
