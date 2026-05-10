num = int(input('Digite o número da tabuada a ser criada: '))
ct = 1

while ct <= 10:
    res = num * ct
    print(f'{num} x {ct} = {res}')
    ct +=1
print('Fim da tabuada')