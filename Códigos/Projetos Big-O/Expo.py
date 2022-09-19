def expo(n, exp):
    pot = 1
    if exp < 0:
        return "error"
    elif exp == 0:
        pot = 1
    while exp != 0:
        pot *= n
        exp -= 1
    print(pot)
    
expo(3, 0)
        
'''Complexidade computacional
 - Melhor caso: O(1)
 - Médio caso: O(n)
 - Pior caso: O(n)
 '''