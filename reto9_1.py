from string import ascii_lowercase

def is_pangram(s):
    s = s.lower()
    for char in ascii_lowercase:
        if char not in s:
            return print(False)
    return print(True)

if __name__ == '__main__':
    is_pangram("The quick, brown fox jumps over the lazy dog!")