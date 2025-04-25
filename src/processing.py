def filter_by_state(dict_in,
                    state=True):
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
