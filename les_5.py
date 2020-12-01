# # ------------------------------------1-----------------------------
'''
Создать программно файл в текстовом формате, записать
в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()

# # ------------------------------------2-----------------------------
'''
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

my_file = open('file_2.txt', 'r')
content = my_file.read()
print(f'Фаил: \n {content}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
print(f'Количество строк: {len(content)}')
my_file = open('file_2.txt', 'r')
content = my_file.readlines()
for i in range(len(content)):
    print(f'Количество символов: {i + 1} - ой строки {len(content[i])}')
my_file = open('file_2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
my_file.close()


# ------------------------------------3-----------------------------
'''
Создать текстовый файл (не программно), построчно записать
фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней
величины дохода сотрудников.
'''

with open('slave.txt', 'r') as my_file:
    slave = []
    poor = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        slave.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, slave)) / len(slave)}')

# ------------------------------------4-----------------------------
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские
числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

rus = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_file = []
with open('file_3.txt', 'r') as file:
    #content = file.read().split('\n')
    for i in file:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file_new.txt', 'w', encoding ="utf-8") as file_2:
    file_2.writelines(new_file)
# # не понимаю почему на выходе хрень со странными символами :/?
# ------------------------------------5-----------------------------
'''
    Создать (программно) текстовый файл, записать в него программно
    набор чисел, разделенных пробелами. Программа должна
    подсчитывать сумму чисел в файле и выводить ее на экран.
'''

def nab():
    try:
        with open('file_5.txt', 'w+') as file_f:
            line = input('Введите цифры через пробел \n')
            file_f.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))

    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода-вывода')
nab()
