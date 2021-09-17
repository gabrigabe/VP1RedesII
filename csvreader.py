import csv

path = './tabela.csv' #Diretorio
ip = '0.0.0.0' #IP a ser procurado

arqcsv = csv.reader(open(path),delimiter=',')

for linha in arqcsv:
    if(ip == linha[0]):
            print("Foi encontrada uma interface de saida para o IP", ip, "Que é:", linha[2])
    else:
      print("Nao foram encontrada uma interface para este endereço na linha", linha)
    
