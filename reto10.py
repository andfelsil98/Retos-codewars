def tickets(people):
    ticket_price = 25
    acumulate =0
    for p in people:

        if p == ticket_price:
            acumulate += p
            


        elif p > ticket_price:
            result = p - ticket_price
            if result <= acumulate:
                acumulate += ticket_price
        
            else:
                return print('NO')
            
    return print('YES')
        

 



if __name__ == '__main__':
    # tickets([25, 25, 50])
    # tickets([25, 100]) 
    tickets( [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100])