from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() 
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def add():
        name = input("Account Name: ")
        pwd = input("Password: ")

        with open("passwords.txt",'w') as f:
            f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
             
    
def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,password = data.split("|")
            print("User:",user,"Password:",fer.decrypt(password.encode()).decode())


while True:
    mode = input("Do you like to add a new password or view an existing password ? Type: view/add : or press q to Quit ").lower()

    if mode == 'q':
        break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Not a valid option")
        continue


