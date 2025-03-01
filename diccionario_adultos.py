meme_dict = {
            "CRINGE": "algo excepcionalmente raro o embarazoso",
            "LOL": "una respuesta común a algo gracioso",
            "VOID": "algo que tiene un contexto turbio",
            "SKIBIDI": "es una palabra que hace referencia a una serie animada web, no tiene un significado como tal"
            }

word = input("Escribe una palabra que no entiendas: ").upper()

if word in meme_dict.keys():
   print("Esto significa que es", meme_dict[word])
else:
    print('Lo sentimos pero la palabra no está en el diccionario')

