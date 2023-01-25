# Модуль данных сотрудников компании

FIELD_NUM_ID     = 0 # поле ИД
FIELD_NUM_FIO    = 1 # поле Ф.И.О.
FIELD_NUM_POST   = 2 # поле должность
FIELD_NUM_SALARY = 3 # поле зарплата

FIELD_RUS_NAME_ID     = '№'
FIELD_RUS_NAME_FIO    = 'Ф.И.О.'
FIELD_RUS_NAME_POST   = 'Должность'
FIELD_RUS_NAME_SALARY = 'Зарплата'

FIELD_LAT_NAME_ID     = 'order_number' # поле ИД
FIELD_LAT_NAME_FIO    = 'fio' # поле Ф.И.О.
FIELD_LAT_NAME_POST   = 'post' # поле должность
FIELD_LAT_NAME_SALARY = 'salary' # поле зарплата

DB_RUS_NAME = 'Сотрудники компании'
DB_LAT_NAME = 'company_employees'
RECORD_LAT_NAME = 'record' # обозначение одной записи о сотруднике

FIELDS_LIST_RUS_NAME = (FIELD_RUS_NAME_ID, FIELD_RUS_NAME_FIO, FIELD_RUS_NAME_POST, FIELD_RUS_NAME_SALARY)
FIELDS_LIST_LAT_NAME = (FIELD_LAT_NAME_ID, FIELD_LAT_NAME_FIO, FIELD_LAT_NAME_POST, FIELD_LAT_NAME_SALARY)
QTY_FIELDS = len(FIELDS_LIST_RUS_NAME) # кол-во полей описывающих сотрудников компании

# Хранилище записей о сотрудниках компании
company_employees = []
# Максимальный номер записи (не уменьшается при удалении последней записи)
max_id = int(0)

# для всех других модулей данные о сотрудниках компании - это список состояций из списков
def get_DB_as_list_of_lists():
    return company_employees

def get_next_id():
    return max_id+1

def init_max_id():
    global max_id
    max_id = max(map(int, [lst[FIELD_NUM_ID] for lst in company_employees]))

def init(lst):
    for s in lst:
        company_employees.append(s)
    init_max_id()

def get_found_lists(search_text):
    lst = []
    for list1 in company_employees:
        for s in list1[1:]:
            if search_text in s:
                lst.append(list1)
                break
    return lst

def delete_by_id(id: int):
    for lst in company_employees:
        if str(id) == lst[FIELD_NUM_ID]:
            company_employees.remove(lst)
            return lst
    return None    

def add_record(fields):
    global max_id
    max_id += 1
    lst = [str(max_id),*fields]
    company_employees.append(lst)
    return lst

def update_by_id(id: int, fields):
    for i, lst in enumerate(company_employees):
        if str(id) == lst[FIELD_NUM_ID]:
            lst = [str(id), *fields]
            company_employees[i] = lst
            return lst
    return None    

