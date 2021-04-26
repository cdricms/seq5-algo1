from data import accounts


## B1
def account_exist(uid, pdw, logs: list):
    for account in logs:
        if account["login"] == uid and account["password"] == pdw:
            return True

    return False

print(account_exist("frodon", "mdp123", accounts))


## B2
def account_index(uid, psw, logs):

    for index in range(len(logs)):
        if logs[index]["login"] == uid and logs[index]["password"] == psw:
            return index

    return -1


print(account_index("merry", "psw789", accounts))
