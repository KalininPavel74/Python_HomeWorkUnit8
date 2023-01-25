# Модуль для запуска приложения.

# Сотрудники компании. Концепция MVC. SIDU. Console. Python. 

import model
import control
import export_import
import view_console as view

taskName = '''Задание  №1. Создать информационную систему
позволяющую работать с сотрудниками некой компании.
           '''
view.print_text("-----------------------------------\n\r" + taskName)

# Экспортировать первичные данные.
control.choice_first_data_for_DB()
# Показать записи (для наглядности происходящего)
view.print_list(export_import.get_DB_as_list_of_text(20))

# Выполнение операций из главного зациклинного меню
control.looped_menu()