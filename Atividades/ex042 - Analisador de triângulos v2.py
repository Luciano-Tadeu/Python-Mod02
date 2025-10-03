a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO")
    elif a != b and b != c:
        print("Os segmentos acima PODEM FORMAR um triângulo ESCALENO")
    else:
        print("Os segmentos acima PODEM FORMAR um triângulo ISÓCELES")
else:
    print("Ose segmentos acima NÃO PODEM FORMAR um triângulos")