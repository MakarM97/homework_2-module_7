file_name = 'file_homework.txt'
with open(file_name) as file:
    for line in file:
        print(line, end='')
print(file.closed)
# Оператор виз позволяет котнролировать вход в блок кода и выход, плюс сам поумолчанию закрывает файл как я понял