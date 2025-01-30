def show_list(kollekcia):
    for i in kollekcia:
        status = 'Не выполнено'
        if i[1]:
            status = 'Выполнено'
        print(i[0], status)

def add_to_list(colecsia, znachenie_dla_dobavlenie):

    colecsia.append([znachenie_dla_dobavlenie, False])

def remove_from_list(colecsia, nomer_dla_udalenia):
    colecsia.remove(colecsia[nomer_dla_udalenia])

def clear_list(colecsia):
    colecsia = []






