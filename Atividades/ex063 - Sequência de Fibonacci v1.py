print("-"*15)
print("Sequência de Fibonacci")
print("-"*15)
num = int(input("Quantos termos você quer mostrar? "))
c = 3
a1 = 1
a2 = 1
an = 0
print("~"*30)

if num == 3:
    print("0 -> 1 -> 1 -> ", end='')
elif num == 2:
    print("0 -> 1 -> ", end='')
elif num == 1:
    print("0 -> ", end='')
elif num <= 0:
    print("Número inválido!")
else:
    print("0 -> 1 -> 1 -> ", end='')    
    while c < num:
        an = a1 + a2
        a2 = a1
        a1 = an
        print("{} -> ".format(an), end='')
        c += 1
print("FIM")
print("~"*30)