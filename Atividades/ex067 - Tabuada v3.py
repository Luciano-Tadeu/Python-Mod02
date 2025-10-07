
while True:
    c = 1    
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*50)
    if num < 0:
        break
    while c <= 10:
        mult = c*num
        print(f"{num} x {c} = {mult}")
        c += 1
    print("-"*50)
print("PROGRAMA DE TABUADA ENCERRADO. Volte sempre!")