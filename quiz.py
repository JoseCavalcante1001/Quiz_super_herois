import os
import time
import random
questoes = [["Qual é o nome do tio do Spider-man?","Benjamin Franklin Parker","Ben Parker","Benjamin Parker","a","A"],["O que o Thor fazia com suas cabras quando ele estava perdido e com fome?","Mandava elas caçar","Ordenava elas a procurar ajuda","Arrancava partes delas e comia","c","C"],["Quais os 6 membros dos Vingadores que aparecem no primeiro filme?","Homem Formiga, Capitão América, Pantera Negra, Homem-Aranha, Thor e Hulk","Homem de Ferro, Capitão América, Viúva Negra, Gavião Arqueiro, Hulk e Thor","Homem de Ferro, Viúva Negra, Pantera Negra, Mulher Maravilha, Thor e Vespa","b","B"],["Qual é a origem do traje preto do Peter Parker?","O Simbionte é trazido de uma expedição espacial e o Peter o pega em um laboratório?","Peter o adquire em Battleworld depois de ter o seu uniforme destruído","O simbionte é feito a partir do sangue do Peter e depois se une a ele","b","B"],["Quem é o personagem mais rápido dos quadrinhos?","Wally West","Eobard Thawne","Barry Allen","a","A"],["Como o Thanos conseguiu a joia da realidade?","Roubando-a do Colecionador","Eliminando o Visão","Sacrificando Gamora","a","A"],['Qual das alternativas tem todos os vilões que pertencem a dc?',"Coringa, Poderosa, Harley Quinn, Mulher-Gato, Flash Reverso","Coringa, Apocalypse, Mulher-Gato, Monstro do Pântano","Arraia Negra, Exterminador, Batroc, Coringa","b","B"],["Por qual nome o héroi Shazam era conhecido?","Capitão Marvel","Invencible","White Adam","a","A"],["Qual espécie do herói Nuclear?","Inumano","Mutante","Meta-humano","c","C"],["Qual é a identidade secreta da feiticeira escarlate?","Vanessa Maximoff","Wanda Maximoff","Carmen Marximoff","b","B"]]

carregamento = 0
contador_corretas = 0
ordem_quest = 1
executar=True

entrada = str(input("                                                       BEM VINDO AO QUIZ\nEsse quiz tem perguntas relacionadas aos heróis dos universos Marvel e DC, vamos ver se você é um fanático, aperte qualquer tecla para iniciar.\n!Caso queira parar de responder o quiz digite (stop)!\n"))
time.sleep(0.5)
print("Começando")
while (carregamento<=100):
  time.sleep(0.5)
  print(carregamento,"%")
  time.sleep(0.5)
  os.system("cls")
  carregamento+=20
print("_"*120)
def perg(questions):
  time.sleep(1)  
  return f"{ordem_quest}ª pergunta:\n{questoes[questions][0]}"
def alte(options):
  time.sleep(1)  
  return f"Alternativas:\na) {questoes[options][1]}\nb) {questoes[options][2]}\nc) {questoes[options][3]}"
def repet(repetir_casoerro):
    global contador_corretas
    print("")
    print("REPETINDO\n\ncorreção ativada,\n")
    print(f"ALTERNATIVAS:\na) {questoes[repetir_casoerro][1]}\nb) {questoes[repetir_casoerro][2]}\nc) {questoes[repetir_casoerro][3]}")
    res = str(input("Qual das alternativas é verdadeira?\n"))
    if(res==questoes[repetir_casoerro][4] or res==questoes[repetir_casoerro][5]):
      contador_corretas=contador_corretas+1
      for tempo in range(3):
        time.sleep(0.5)
        print(tempo+1)
      time.sleep(0.5)  
      return "Resposta correta!"
    elif(res=="a" or res=="A" or res=="b"or res=="B" or res=="c" or res=="C"):      
      for tempo in range(3):
        time.sleep(0.5)
        print(tempo+1)
      time.sleep(0.5)  
      return "Resposta incorreta"
    else:
        print("Resposta inválida")
        return repet(repetir_casoerro-0)
def verifi(resposta_correta):
    global contador_corretas
    res= str(input("Qual das alternativas é verdadeira?\n"))    
    if(res==questoes[resposta_correta][4] or res==questoes[resposta_correta][5]):
        contador_corretas=contador_corretas+1
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('3')
        time.sleep(0.5)
        return "Resposta correta!"
    elif(res=="stop" or res=="Stop" or res=="STOP"):
      return "Quiz encerrado"
    elif res=="a" or res=="A" or res=="b"or res=="B" or res=="c" or res=="C":
        time.sleep(0.5)
        print("1")
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('3')
        time.sleep(0.5)  
        return "Resposta errada"
    else:
        print("Resposta inválida")
        return repet(resposta_correta)
def deno():
    global ordem_quest, contador_corretas,executar
    den=str(input("Deseja jogar denovo?\n"))
    if(den=="sim" or den=="SIM" or den=="Sim" or den=="s" or den=="S" or den=="ss" or den=="SS" or den=="Ss"):
        ordem_quest=1
        contador_corretas=0
        random.shuffle(questoes)
        return "                                                       BEM VINDO AO QUIZ"
    elif(den=="não" or den=="NÃO" or den=="Não" or den=="n" or den=="N" or den=="nao" or den=="NAO" or den=="Nao"):
        executar=False
        return 'obrigado por jogar'
    else:
      print("Resposta não compreendida")
      return deno()
def quiz():
  for numeracao_perguntas in range(len(questoes)):
    global ordem_quest,getVerifi
    print(perg(numeracao_perguntas))
    print(alte(numeracao_perguntas))
    getVerifi=verifi(numeracao_perguntas)
    print(getVerifi)
    if(getVerifi=="Quiz encerrado"):
      break
    time.sleep(1)
    os.system("cls")
    ordem_quest+=1
while(executar):
    print(quiz())
    os.system("cls")
    print("Agradecemos pela sua participação no quiz, sua pontuação foi ",contador_corretas,"/",len(questoes))
    if(getVerifi=="Quiz encerrado"):
      executar=False
    else:
      print(deno())
print("SESSÃO ENCERRADA")