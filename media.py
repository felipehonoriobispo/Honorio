nota1 = float(input('Entre com a primeira nota   '))
nota2 = float(input('Entre com a Segunda nota   '))
nota3 = float(input('Entre com a Terceira nota  '))
nota4 = float(input('Entre com a Quarta nota    '))

soma = nota1+nota2+nota3+nota4
media = soma/4

if (media>7):
    print('Sua media é : ',media, 'parabéns você foi APROVADO')

if (media>5.5):
    print('Sua media é : ',media, 'você esta de RECUPERAÇÃO')
else:
    print('Sua media é : ',media, 'e você foi REPROVADO')