##enunciado
#Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

# Valid inputs examples:
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
# Invalid input examples:
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089

def is_valid_IP(strng):
    cont = 0
    ip = strng.split('.')
    for i in ip:
        if i[0] != '0':
            if int(i) > 0 or int(i) < 255:
                cont += 1
    if cont < 4:
        return False
    return True
            
        


if __name__ == '__main__':
    result = is_valid_IP('055.255.255.255')
    print(result)