# def digital_root(n):
#     inte_number = 0
#     acumulate = 0
#     while n != 0:
#         last_number = n % 10   ##se queda unicamente con el ultimo digito
#         n //= 10  ##se queda con la parte entera del numero
#         acumulate += last_number ##suma el ultimo numer registrado con el acumulado

#     if acumulate> 9:
#         digital_root(acumulate)
#     else:

#         return print(acumulate)


# if __name__ == '__main__':
#     digital_root(16)
#     digital_root(942)
#     digital_root(132189)
#     digital_root(493193)
def digital_root(n):
    inte_number = 0
    acumulate = 0
    while n != 0:
        last_number = n % 10   ##se queda unicamente con el ultimo digito
        n //= 10  ##se queda con la parte entera del numero
        acumulate += last_number ##suma el ultimo numer registrado con el acumulado

    if acumulate> 9:
        digital_root(acumulate)
    else:

        return acumulate


if __name__ == '__main__':
    digital_root(16)
    digital_root(942)
    digital_root(132189)
    digital_root(493193)
    