import os
import datetime


nome = input("Nome: ")
idade = input("Idade: ")
profisao = input("proisão: ")
frase_do_dia = input("Frase do dia: ")


data_atual = datetime.date.today()
data_formatada = data_atual.strftime("%d-%m-%Y")


pasta_data = os.path.join(os.getcwd(), data_formatada)
if not os.path.exists(pasta_data):
    os.makedirs(pasta_data)


nome_arquivo = f"{nome}.txt"
caminho_arquivo = os.path.join(pasta_data, nome_arquivo)


with open(caminho_arquivo, "w") as arquivo:
    arquivo.write(nome)
    arquivo.write(idade)
    arquivo.write(profisao)
    arquivo.write(frase_do_dia)

print(f"Os dados foram salvos em {caminho_arquivo}")
