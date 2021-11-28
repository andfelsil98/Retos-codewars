from string import ascii_lowercase

def is_pangram(s):
    converted_string = ''.join(char for char in s if char.isalpha())  ##isalnum me verifica si en la cadena tengo elementos alfabeticos(letras) si si me los mete en la nueva lista sino los quita. no tiene en cuenta ni numeros ni caracteres especiales
    converted_string = converted_string.lower()
    print(set(ascii_lowercase))
    print(set(converted_string))
    if set(converted_string) >= set(ascii_lowercase):
        return print(True)
    else:
        return print(False)

    # print(set(converted_string)) ##set me permite filtrar datos repetidos y devolverme un conjunto de datos
    # # return False
    
    # print(ascii_lowercase) ##me imprimie el abecedario en minusculas


if __name__ == '__main__':
    is_pangram("The quick, brown fox jumps over the lazy dog!")

