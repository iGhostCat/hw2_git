def filter_by_state(dict_in : list,
                    state=True) -> list:
    ''' Функция фильтрации списка операций пользователя по статусу выполнения, принимает
        на вход список словарей операций, возвращает список словарей, отфильтрованный по
        значению статуса выполнения '''
    status = ''
    if state:
        status = 'EXECUTED'
    else:
        status = 'CANCELED'

    dict_out = []
    for dic in dict_in:
        if dic['state'] == status:
            dict_out.append(dic)
    return dict_out


def sort_by_date(dict_in : list, direction = True):
    ''' Функция сортировки словарей в списке по дате, принимает список словарей и
        необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
        Функция должна возвращать новый список, отсортированный по дате'''
    sorted_dict = sorted(dict_in, key=lambda d: d['date'], reverse=direction)
    return sorted_dict
