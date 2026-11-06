# Write your code here :-) Очень важный комментарий на одну строку
a=10
b=5

if a > b:
    print("A больше B")
    print(b -b)
else:
    print("B больше или равно A")
    print(b-a)
'''
комментарий большей важности
многострочный
'''
print("Конец")

def open_file(filename):
    print("Чтение файла",filename)
    with open(filename) as f:
       return f.read()
print("готово")