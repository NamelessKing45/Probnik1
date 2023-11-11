password = str(input('Придумайте пароль\t'))
input_string = str(input("input password\t"))
input_string += "-False password"
input_string = input_string.replace(password + '-False password', password + '-Try password')
print(input_string)