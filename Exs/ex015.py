kms = float(input('Digite quantos kms foram rodados'))
dias = float(input('Digite quantos dias voce ficou com o carro'))
total = (kms * 0.15) + (dias * 60)
print('O total é R${}'.format(total))
