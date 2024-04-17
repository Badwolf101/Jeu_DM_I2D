import time
import random
from colorama import Fore, Back, Style

#variables globales
#variables du jeu :
item = ["machette", "briquet", "lampe"]

randomInteral = []
animauxTues = 0
itemUtilise = []
succes = []
premiers = [2, 3, 5, 7, 11]
#perso a tourver
aTrouver = "femme"

#joueur :
userName = ""
backpack = []
sizebackpack = 2

#logo :
logoJeu2 = '''
  ####################################################################################
 ######################################################################################
##############    ###########           ######         ####            #################
##############    ##########    #####    ####    ##############    #####################
##############    ##########    #####    ####    ##############    #####################
##############    ##########    #####    #####        #########    #####################
##############    ##########    #####    ##########    ########    #####################
##############    ##########    #####    ##########    ########    #####################
###############         #####           #####         ##########  ######################
########################################################################################
########################################################################################
#####  ######         #####  ############         ######  #######  #####        ########
####    ####    ##########    ##########    ###    ####     ####    ####    ###    #####
####    ####    ##########    ##########    ###    ####       ##    ####    ####   #####
####    #####         ####    ##########    ###    ####    #   #    ####    ####    ####
####    ##########     ###    ##########           ####    ##       ####    ####   #####
####    ##########     ###    ##########    ###    ####    ####     ####    ###    #####
#####  #####          #####        ######  #####  ######  #######  #####         #######
 ######################################################################################
  ####################################################################################

'''
logoend = '''

 ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤      ¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤       ¤¤¤  ¤¤¤¤¤¤¤¤¤¤
 ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤      ¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤¤      ¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤
       ¤¤¤        ¤¤¤      ¤¤¤  ¤¤¤                 ¤¤¤           ¤¤¤¤¤     ¤¤¤  ¤¤¤      ¤¤¤
       ¤¤¤        ¤¤¤      ¤¤¤  ¤¤¤                 ¤¤¤           ¤¤¤ ¤¤    ¤¤¤  ¤¤¤      ¤¤¤
       ¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤  ¤¤   ¤¤¤  ¤¤¤      ¤¤¤ 
       ¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤   ¤¤  ¤¤¤  ¤¤¤      ¤¤¤ 
       ¤¤¤        ¤¤¤      ¤¤¤  ¤¤¤                 ¤¤¤           ¤¤¤    ¤¤ ¤¤¤  ¤¤¤      ¤¤¤
       ¤¤¤        ¤¤¤      ¤¤¤  ¤¤¤                 ¤¤¤           ¤¤¤     ¤¤¤¤¤  ¤¤¤      ¤¤¤
       ¤¤¤        ¤¤¤      ¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤      ¤¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤
       ¤¤¤        ¤¤¤      ¤¤¤  ¤¤¤¤¤¤¤¤¤¤¤¤        ¤¤¤¤¤¤¤¤¤¤¤¤  ¤¤¤       ¤¤¤  ¤¤¤¤¤¤¤¤¤¤
''' 

#fonctions :

def input_check(message, data_type, valid_input):
  print(Fore.YELLOW, end="")
  while True:
    try:
      response = data_type(input(message))
      if isinstance(valid_input, tuple):
        if response < valid_input[0] or response > valid_input[1]:
          raise ValueError()
      else:
        if response != valid_input:
          raise ValueError()
      print(Fore.RESET, end="")
      return response
    except ValueError:
      print("Veuillez entrer une réponse valide.")

def animation(type, caractre = '#', temps = 0.125, repete = 25):
    print(Fore.LIGHTGREEN_EX, "\n[", end="")
    for i in range(0, repete):
      print(caractre, end="", flush=True)
      time.sleep(temps)
    print("]\n", Fore.RESET)

def calculItem():
  items_non_utilises = []
  for element in item:
    if element not in itemUtilise:
      items_non_utilises.append(element)
      return items_non_utilises

def calculSucces():
  if aTrouver in succes:
    return "Trouver votre" + aTrouver
  else:
    return "0"

def plage():
  print("Vous avez choisi la plage\n")
  print("Après avoir exploré la plage pendant un moment, la nuit commence à tomber. Vous essayez donc de faire un feu pour vous réchauffer et vous reposer")
  if "briquet" in backpack and input_check("0 = vous ne faites rien, 1 = vous allumez le feu : ", int, (0, 1)) == 1:
    print("Vous rassemblez du bois et allumez le feu avec votre briquet, vous vous installez, vous réchauffez et commencez tout de suite à vous sentir mieux. Vous décidez de dormi car une longue journée d'exploration vous attend demain")
    time.sleep(6)
  else:
    print("Vous n'avez pas de briquet, vous devez donc essayer de faire du feu en frottant 2 morceaux de bois ensemble")
    nombreChoisi = input_check("Choisissez un nombre entre 1 et 10 : ", int, (1, 10))
    randomInteral.append(random.randint(1, 10))                       # l'ordinateur joue
    randomInteral.append(randomInteral[0] + 2)                        # l'ordinateur joue
    if nombreChoisi >= randomInteral[0] and nombreChoisi <= randomInteral[1]:
      print("Bravo ! Par chance vous avez réussi à faire du feu, vous vous installez et commencez à vous réchauffer . Vous décidez de dormir car une longue journée d'exploration vous attend demain")
    else:
      print("vous n'avez pas réussi à faire du feu, vous aviez une chance sur 3 de réussir, vous vous sentez très faible et vous décidez de dormir")
      time.sleep(1)
      end("Vous êtes mort de froid. Note : le briquet permet à coup sûr de faire du feu ;)")
  print("Une tempête se lève, vous vous réveillez en sursaut. Avec la marée haute la mer vient se déchaîner sur la plage et vous contraint à vous enfoncer dans la jungle.")
  time.sleep(3)

def Grotte():
  print("La grotte est très sombre, vous ne voyez rien")
  if "lampe" in backpack:
    if input_check("0 = vous ne faites rien, 1 = vous allumez la lampe torche : ", int, (0, 1)) == 1:
      itemUtilise.append("machette")
      print("Vous allumez la lampe torche, au bout d'un moment d'exploration vous trouver un sac abandonné contenant une fusée de détresse ! Vous l'ajoutez à votre sac et continuez votre exploration jusqu'à trouver la sortie")
      item.append("fusée de détresse")
      return 1
  else:
    print("Vous n'avez pas de lampe torche, vous continuez dans le noir")
    print("\nA taton, vous arrivez a ce qui semble une intersection, vous avez le choix entre aller à gauche ou à droite")
    if input_check("0 = à gauche, 1 = à droite : ", int, (0, 1)) == 1:
      print("Vous allez à droite, vous glissez et tombez dans un trou. Vous avez une blessure fatal et vous mourrez")
      end("Vous êtes mort. Note : la lampe torche permet de voir dans la grotte ;)")
    else:
      print("Alors que vous perdiez espoir, de la lumière apparait. A la sortie de la grotte vous découvrez un campement de fortune, votre", aTrouver, "est là !")
      print(Fore.GREEN + "Succès débloqué : vous avez trouvé votre", aTrouver, Fore.RESET)
      succes.append(aTrouver)
      print("Vous continuez à chercher un moyen de repartir de l'île")
      return 0

#eventements radom :
def animalSauvage(animal, tentative = 3, degat = 0):
  print('\n'"Vous croisez un", animal, "vous avez le choix entre le combattre ou le fuir")
  if input_check("0 = le fuir, 1 = le combattre : ", int, (0, 1)) == 1:
    if "machette" in backpack:
      while degat < 3 and tentative > 0:
        nbcible = random.randint(1, 10)
        nbchoisi = input_check("choisissez un chiffre entre 1 et 10 : ", int, (1, 10))
        if nbcible == nbchoisi:
          print("vous avez touché", animal, "en seulement ", tentative - tentative, "tentative, bravo !")
          degat = 3
          itemUtilise.append("machette")
          break
        else:
          print("vous n'avez pas touché", animal, "il vous reste ", tentative - 1, "tentative")
          tentative -= 1
          if tentative == 0:                                                                                #<----- décider si mort ou non
            print("vous n'avez pas touché", animal, "et etes contraint de fuire")
            time.sleep(1)
            return 0
        
      print("choisissez un chiffre entre 1 et 10")
      print("Vous avez combattu le ", animal, " et vous l'avez tué")
      time.sleep(1)
      return 1
    else:
      print("vous n'avez pas de quoi combattre", animal, "vous etes contraint de fuire")
      time.sleep(1)
      return 0
  else:
    print("vous avez fui")
    time.sleep(1)
    return 0

def end(endmsg, senario = 0):
  print(endmsg)
  if senario != 0:
    print("Vous avez réussi à vous échapper de l'île avec le sénario", senario)
    print("- Vous n'avez pas utilisé", *calculItem(), "item(s)")
    print("- Vous avez réalisé", calculSucces(), "succès(s)")
  print("\n------------------ Fin du jeu ! ------------------")
  print("LOS ISLAND a été réalisé par : \n" + Style.BRIGHT + "Pierre SCHOFIELD       Tiago RIBEIRO         Clément BRAZEAU" + Style.RESET_ALL)
  print(logoend)
  quit()

###########################################################################################################
#début du jeu : <===================================================
animation(1,"#", 0.01, 100)
print("Bienvenue dans", Fore.MAGENTA + Style.BRIGHT + "> LOST ISLAND < !" + Style.RESET_ALL)
time.sleep(2.5)
print(Fore.CYAN, logoJeu2, Fore.RESET)
userName = input("Entrez votre nom :"'\n')
print("Bonjour", userName, "!")
time.sleep(1)
print("\nVous incarnez un homme à la recherche de sa", aTrouver, "partie à l'aventure à des fin de recherche mais qui ne donne plus aucun nouvel depuis des semaines, sa dernière position connue était sur une île quelque part dans l'océan pacifique. Alors que vous vous dirigiez vers cette position une tempête s'est levée et vous a fait chavirer, vous vous réveillez sur une plage déserte avec le reste de votre bateau fortement endommagé. Autour de l'épave il y a quelques objets éparpillé et un sac à dos")
time.sleep(13)
print("\nVous avez le choix entre", len(item), "items :", *item, "mais votre sac ne peut contenir que", Fore.RED, sizebackpack, "objets", Fore.RESET)
while len(backpack) != 2:
  backpack.clear()
  for i in range(0, len(item)):
#for i in int(len(item)):
    print("Choisissez votre", i+1, "item :")
    print("Souhaitez vous prendre", item[i], "?")
    if input_check("0 = non, 1 = oui : ", int, (0, 1)) == 1:
      backpack.append(item[i])
      print("Vous avez pris", item[i], '\n')
    else:
      print("Vous n'avez pas pris", item[i], '\n')
  if len(backpack) == 2:
    continue
  print('\n'"Vous n'avez rien/trop pris d'item ! Veuillez recommencer.", '\n')

print("Votre sac contient :", Fore.CYAN)
print(*backpack, Fore.RESET)

animation(1,"#", 0.125, 25)

print("Après un certains temps vous devez choisir un endroit pour constrtuire un abris, vous avez le choix entre la plage qui est dégagée, sans relief, mais qui est proche de la mer, ou la forêt qui est plus éloignée de la mer mais qui est très dense et hostile.")

if input_check("0 = la plage, 1 = la jungle : ", int, (0, 1)) == 0:
  plage()

else:
    print("Vous avez choisi la jungle\n")

#=============jointure des 2 branches=============
animauxTues = animauxTues + animalSauvage("lion", 4, 0)

print("\nAprès un moment de marche dans la jungle, vous trouver une grotte au pied de la falaise et décidez de l'explorer")
if Grotte() == 1:
  print("\nAlors que vous marchez depuis un moment, vous appercevez un Hydravion qui passe au dessus de vous, vite ! Que souhaitez vous faire ?")
  if input_check("0 = vous cacher, 1 = tirer votre fusée de détresse : ", int, (0, 1)) == 1:
    print("Vous tirez votre fusée de détresse, l'avion semble l'avoir vu, il amerit non loin de l'ile et vous récupère. Vous êtes sauvé !")
    time.sleep(2)
    end("", 1)
else: 
  print("\nAprès un long moment à chercher un moyen de repartir de l'île, vous vous décidez à réparer votre bateau")
print("Vous avez besoin d'abattre un arbre, veuillez donner les 5 premier chiffres premiers (chiffre divisible par 1 et par eux même):")
for i in range(0, 5):
  while True:
    nbchoisi = input_check("Donnez le chiffre ", int, (premiers[i]))
    if nbchoisi == premiers[i]:
      print("Vous avez trouvé le", i+1, "ier/ème bon chiffre !\n")
      break
print("Vous avez récolté assez de bois et avez réussi à réparer votre bateau, vous retrez chez vous avec votre", aTrouver)
end("", 2)

#fin du jeu :