# Модуль управления.

import model
import export_import
import view_console as view

START_CSV = 'start.csv'
OUT_CSV = 'out.csv'
OUT_TXT = 'out.txt'
OUT_XML = 'out.xml'
OUT_HTML = 'out.html'

menu1 = '''Импортировать данные базу данных сотрудников компании:
1. start.csv
2. out.csv
:'''

menu2 = '''Меню:
1. Отобразить первые 20 записей
2. Поиск
3. Удалить запись по номеру строки
4. Добавить запись
5. Изменить данные в записи
6. Экспортировать данные в файлы "out.*" разных форматов
7. Выйти из программы с экспортом данных
8. Выйти из программы без экспорта данных
:'''

# Выбрать и наполнить базу сотрудников компании первичными данными.
def choice_first_data_for_DB():
    a = view.input_int_value(menu1, 1)
    if   a == 1: 
        lst = export_import.import_list_of_lists_from_CSV(START_CSV, model.QTY_FIELDS)
        model.init(lst)
    elif a == 2: 
        lst = export_import.import_list_of_lists_from_CSV(OUT_CSV, model.QTY_FIELDS)
        model.init(lst)

def export_DB_in_files():
    # CSV
    file_name = OUT_CSV
    qty = export_import.export_list_of_lists_to_CSV(
        file_name, model.get_DB_as_list_of_lists())
    view.print_text(f'Экспортировано {qty} записей в файл {file_name}.')
    # TXT
    file_name = OUT_TXT
    qty = export_import.export_list_to_TXT(
        file_name, export_import.get_DB_as_list_of_text())
    view.print_text(f'Экспортировано {qty} записей в файл {file_name}.')
    # XML
    file_name = OUT_XML
    qty = export_import.export_DB_to_XML(file_name)
    view.print_text(f'Экспортировано {qty} записей в файл {file_name}.')
    # HTML
    file_name = OUT_HTML
    qty = export_import.export_DB_to_HTML(file_name)
    view.print_text(f'Экспортировано {qty} записей в файл {file_name}.')


# Выполнение операций из главного зациклинного меню
def looped_menu():

    while(True):
        a = view.input_int_value('\n\r'+menu2, 1)

        if   a == 1: # 1. Отобразить первые 20 записей
            view.print_list(export_import.get_DB_as_list_of_text(20))

        elif a == 2: # 2. Поиск
            search_text = view.input_str_value('Введите текст для поиска: ')
            lists = model.get_found_lists(search_text)
            if lists:
                view.print_text('')
                view.print_text(f'Найденные записи ({search_text}):')
                text_lists = []
                for lst in lists:
                    text_lists.append(export_import.get_record_as_text(lst))
                view.print_list(text_lists)
            else: view.print_text(f'Записи с текстом "{search_text}" не найдены.')

        elif a == 3: # 3. Удалить запись по номеру строки
            id = view.input_int_value('Введите номер записи для удаления: ')
            lst = model.delete_by_id(id)
            view.print_text('')
            if lst:
                view.print_text('Удалена запись:')
                view.print_text(export_import.get_record_as_text(lst))
            else: view.print_text(f'Ошибка. Запись {id} не найдена и не удалена.')

        elif a == 4: # 4. Добавить запись
            fio    = view.input_str_value('Введите Ф.И.О.: ')
            post   = view.input_str_value('Введите должность: ')
            salary = view.input_str_value('Введите зарплату: ')
            lst = model.add_record([fio, post, salary])
            view.print_text('')
            if lst:
                view.print_text('Запись добавлена:')
                view.print_text(export_import.get_record_as_text(lst))
            else: view.print_text(f'Ошибка. Запись не добавлена.')

        elif a == 5: # 5. Изменить данные в записи
            id     = view.input_int_value('Введите номер записи для изменения данных: ')
            fio    = view.input_str_value('Введите Ф.И.О.: ')
            post   = view.input_str_value('Введите должность: ')
            salary = view.input_str_value('Введите зарплату: ')
            lst = model.update_by_id(id, [fio, post, salary])
            view.print_text('')
            if lst:
                view.print_text(f'Исправлена запись с номером {id}:')
                view.print_text(export_import.get_record_as_text(lst))
            else: view.print_text(f'Запись с номером {id}" не найдена и не исправлена.')

        elif a == 6: # 6. Экспортировать данные в файлы "out.*" разных форматов
            export_DB_in_files()
        elif a == 7: # 7. Выйти из программы с экспортом данных
            export_DB_in_files()
            exit()
        elif a == 8: # 8. Выйти из программы без экспорта данных
            exit()

