from models import Post, LinkPost, TextPost, User


def save_to_db(f_name, l_name, phone_user, birthday_user, address_user, email_user):
    author_user = User(first_name=f'{f_name}', last_name=f'{l_name}', phone=f'{phone_user}').save()

    post1 = TextPost(title='Birthday, Address', author=author_user)
    post1.birthday = f'{birthday_user}'
    post1.address = f'{address_user}'
    post1.save()

    post2 = LinkPost(title='Email', author=author_user)
    post2.email = f'{email_user}'
    post2.save()


def receive_data():
    print('Please. Enter the data:')
    f_name = input('first_name: ')
    l_name = input('last_name: ')
    phone_user = input('phone: ')
    birthday_user = input('birthday: ')
    address_user = input('address: ')
    email_user = input('email: ')
    return f_name, l_name, phone_user, birthday_user, address_user, email_user


def main():
    f, l, p, b, a, e = receive_data()
    save_to_db(f, l, p, b, a, e)
    print("Data saved")
    print('If you need add new data, enter "y", else "n"')
    res = input('>>> ')
    if res == 'n':
        print('Data processing is complete!')
    else:
        main()


if __name__ == '__main__':
    main()
