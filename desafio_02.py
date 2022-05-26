lista = [2];

novaLista = [];

for i in lista:
    lista = [1, i]
    for x in lista:
        if len(lista) > 1 :
            number = i
            listaFiltrada = len(list(filter(lambda x: x == number, lista)))
    print(lista)
