# Datetime


````python
from datetime import datetime


print(datetime.now())  # 2023-01-12 16:29:22.704860
print(datetime.now().day)  # 12
print(datetime.now().month)  # 1
print(datetime.now().year)  # 2023


# criar uma data
meu_aniversario = datetime(2023, 6, 2)
print(meu_aniversario)  # 2023-06-02 00:00:00


# recebendo os dados de um usuário (strptime transforma STRING para DATETIME)
data_de_aniversario = datetime.strptime(
    input('Qual a data do seu aniversário? '), '%d/%m/%Y')
print(data_de_aniversario)


# calculando o INTERVALO entre duas datas
data_atual = datetime.now()
prazo = data_de_aniversario - data_atual
print(prazo.days)
````