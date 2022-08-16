documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

print('Команды для ввода:', 'p - выводит имя человека по номеру документа, которому он принадлежит', 's – выводит номер полки по номеру документа, на которой он находится', 'l - выводит список всех документов','a – добавит новый документ в каталог и в перечень полок',  'd – удаляет документ из каталога и из перечня полок', 'm – переместит документ с текущей полки на целевую', 'as - добавит новую полку', sep='\n')


#p – people 
def get_name():
    num = input('Введите номер документа ')
    for doc in documents:
        if doc['number'] == num:
            return doc['name']
            break
    return 'Документ отсутствует в базе' 
  
#s – shelf 
def get_shelf(num):
    for key, value in directories.items():
        for doc_num in value:
            if doc_num in num:
                return print(key)
    else: 
      print('Такой документ не найден')
  
#l – list  
def list_doc():
    for doc in documents:
        print(doc['type'], ' "',doc['number'],'" ','"',doc['name'], '"', sep='')
      
#a – add 
def add_doc(num, type_num, name_num, shelf):
    for key, value in directories.items():
        if key == shelf:
            value.append(num)
            new_doc = {'type': type_num, 'number': num, 'name': name_num}
            documents.append(new_doc)
            return print('Документ добавлен')
          
#d-del
def delete_doc(num):
    for doc in documents:
        if doc['number'] == num:
            print('Документ Удален')
            return documents.remove(doc)
        else:
            x = 'Такой документ не найден в каталоге'
    return print(x)
def delete_dir(num):
    for value in directories.values():
        if num in value:
                value.remove(num)
                return True
    print('Такой документ не найден на полке')
    return False
  #d – delete 
def delete_num(num):
    return delete_doc(num), delete_dir(num)     
  
#m – move 
def move_doc(num, shelf):
    for key, value in directories.items():
        if key == shelf:
            if delete_dir(num):
                value.append(num)
                print('Документ перемещен на новую полку')
                return 
        else:
          print('Такая полка отсутствует')
        break
#as – add shelf 
def add_shelf(num):
    directories.setdefault(num, [])
    return print('Полка добавлена') 

while True:
     command = input('Введите команду: ')
     if command == 'p':
      print(get_name())
     elif command == 's':
        num = input('Введите номер документа: ')
        get_shelf(num)
     elif command == 'l':
        list_doc()
     elif command == 'a':
        num = input('Введите номер документа для добавления: ')
        type_num = input('Введите тип документа для добавления: ')
        name_num = input('Введите имя владельца документа для добавления: ')
        shelf = input('Введите номер полки для добавления документа: ')
        add_doc(num, type_num, name_num, shelf)
     elif command == 'd':
        num = input('Введите номер для удаления: ')
        delete_num(num)
     elif command == 'm':
        num = input('Введите номер документа для перемещения: ')
        shelf = input('Введите номер полки: ')
        move_doc(num, shelf)
     elif command == 'as':
        num = input('Введите номер новой полки для добавления: ')
        add_shelf(num)
     else:
        print('Вы ввели неправильную команду')      