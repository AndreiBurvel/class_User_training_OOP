password_often = []
with open('most_used_passwords.txt', mode='r', encoding='utf-8') as f:
    for i in f:
        password_often.append(i.strip())


if __name__ == "__main__":
    print(password_often)