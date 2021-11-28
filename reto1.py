def open_or_senior(data):
    category = []

    for elements in data:
        if elements[0] >= 55 and elements[1] > 7:
            category.append('Senior')
        else:
            category.append('Open')
    return category


if __name__ == '__main__':
    
    data =  [[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]
    result = open_or_senior(data)  
    print(result)