import factoria
if __name__ == '__main__':
    mi_factoria = factoria.Factoria()

    #Factoria, crea a una persona!
    persona = mi_factoria.get_persona('Gordon Freeman', 'M', 27)
    #se ha creado una persona masculina
    print (persona) 
    # print persona.get_nombre()
    # print persona.get_genero()