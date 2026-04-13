from datetime import date

ano = int(input('em que ano você nasceu: '))
mes = int(input('em que mês você nasceu: '))
dia = int(input('em que dia você nasceu: '))

hoje = date.today()
nascimento = date(ano, mes, dia)
idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

print(f'sua idade é: {idade} anos.')

if idade < 16:
    print('menor de 16 anos e você não pode votar ainda.')
elif 16 <= idade < 18 or idade >= 70:
    print('o seu voto e opcional.')
else:
    print('você tem 18 anos ou mais e o seu voto é obrigatório.')