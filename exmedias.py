listam=[]
i=0
j=0
calculo = 0

while j < 4:
    j+=1
    media_inserida = float(input('Entre com a ' + str(j)+' nota'))
    listam.append(media_inserida)

while i < 4:
    calculo += listam[i]
    i += 1

print(listam)
media = calculo/4
print(media)
if(media>=7):
    print('Sua média é:', media, ' Parabéns você foi APROVADO !')
elif (media>=5.5):
    print('Sua média é :', media, 'Você ficou de RECUPERAÇÃO')
elif (media<=5.0):
    print('Sua média é :', media, 'E infelizmente você foi REPROVADO')