import time
import random

#variables globales
#variables du jeu :
item = ["machette", "briquet", "lampe"]
scenario = None #* sert de tempon à chaque situation, écrase la situation précédente

randomInteral = []

animauxTues = 0
itemUtilise = []

#joueur :
userName = ""
backpack = []
sizebackpack = 2

#logo :
logoJeu = '''
  #########################################################################################################################################################
 ###########################################################################################################################################################
#####    ###########           ######         ####            ############  ######         #####  ############         ######  #######  #####        ########
#####    ##########    #####    ####    ##############    ###############    ####    ##########    ##########    ###    ####     ####    ####    ###    #####
#####    ##########    #####    ####    ##############    ###############    ####    ##########    ##########    ###    ####       ##    ####    ####   #####
#####    ##########    #####    #####        #########    ###############    #####         ####    ##########    ###    ####    #   #    ####    ####    ####
#####    ##########    #####    ##########    ########    ###############    ##########     ###    ##########           ####    ##       ####    ####   #####
#####    ##########    #####    ##########    ########    ###############    ##########     ###    ##########    ###    ####    ####     ####    ###    #####
######         #####           #####          #########  #################  #####          #####        ######  #####  ######  #######  #####         #######
 ###########################################################################################################################################################
  #########################################################################################################################################################

'''

#fait moi le meme logo mais en 2 partie, avec LOST en premier et ISLAND en deuxieme sur deux niveaux différents
logoJeu2 = '''
  ####################################################################################
 ######################################################################################
##############    ###########           ######         ####            #################
##############    ##########    #####    ####    ##############    #####################
##############    ##########    #####    ####    ##############    #####################
##############    ##########    #####    #####        #########    #####################
##############    ##########    #####    ##########    ########    #####################
##############    ##########    #####    ##########    ########    #####################
###############         #####           #####          #########  ######################
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

#fonctions :
def oneOrZero(message):
  while True:
    try:
      oneOrZero = int(input(message))
      if oneOrZero == 1 or oneOrZero == 0:
        return oneOrZero
      else:
        print("Erreur, veuillez choisir parmi les choix proposés")
    except ValueError:
      print("Erreur, veuillez choisir parmi les choix proposés")
#fait moi une fonction dynamique où je peux spécifer en argument les valeurs acceptées et qui continue tant que l'input n'est pas valide  

def animation(type, caractre = '#', temps = 0.125, repete = 25):
  if type == 1:
    print("\n[", end="")
    for i in range(0, repete):
      print(caractre, end="", flush=True)
      time.sleep(temps)
    print("]\n")
  elif type == 2:
    """                                     #<---------------------------------------- optionel j'ai pas fini
    print("\n[", end="")
    for i in range(0, repete):
      print(caractre, end="", flush=True)
      time.sleep(temps)
    print("]\n")"""

def plage():
  print("Vous avez choisi la plage\n")
  print("Après avoir exploré la plage pendant un moment, la nuit commence à tomber. Vous essayer donc faire un feu pour vous réchauffer et vous reposer")
  if "briquet" in backpack and oneOrZero("0 = vous ne faites rien, 1 = vous allumez le feu : ") == 1:
    print("vous rassemblez du bois et allumez le feu avec votre briquet, vous vous installez réchauffer et commencer tout de suite a vous sentir mieux")
    time.sleep(1)
  else:
    print("vous n'avez pas de briquet, vous devez donc essayer de faire du feu en frotant 2 morceaux de bois ensemble")
    nombreChoisi = int(input("choisissez un chiffre entre 1 et 12 : "))
    randomInteral.append(random.randint(1, 10))
    randomInteral.append(randomInteral[0] + 2)
    if nombreChoisi >= randomInteral[0] and nombreChoisi <= randomInteral[1]:
      print("Bravo ! par chance vous avez réussi à faire du feu, vous vous installez réchauffer et commencer tout de suite a vous sentir mieux")
      time.sleep(1)
    else:
      print("vous n'avez pas réussi à faire du feu, vous aviez une chance sur 3 de réussir, vous vous sentez très faible et vous décidez de dormir")
      time.sleep(1)
      quit("Vous êtes mort de froid. Note : le briquet permet à coup sur de faire du feu ;)")

def calculItem():
  items_non_utilises = []
  for element in item:
    if element not in itemUtilise:
        items_non_utilises.append(element)
        return items_non_utilises

#eventements radom :
def animalSauvage(animal, tentative = 2, degat = 0):
  print("Vous croisez un ", animal, ", vous avez le choix entre le combattre ou le fuir")
  if oneOrZero("0 = le fuir, 1 = le combattre : ") == 1:
    if "machette" in backpack:
      while degat < 3 and tentative > 0:
        nbcible = random.randint(1, 10)
        nbchoisi = int(input("choisissez un chiffre entre 1 et 10 : "))
        if nbcible == nbchoisi:
          print("vous avez touché ", animal, "en seulement ", tentative - tentative, "tentative, bravo !")
          degat = 3
          itemUtilise.append("machette")
          break
        else:
          print("vous n'avez pas touché ", animal, "il vous reste ", tentative - 1, "tentative")
          tentative -= 1
          if tentative == 0:                                                                                #<----- décider si mort ou non
            print("vous n'avez pas touché ", animal, "vous etes contraint de fuire")
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


#début du jeu : <===================================================
animation(1,"#", 0.01, 100)
print("Bienvenue dans > LOST ISLAND < !")
time.sleep(2.5)
print(logoJeu2)
userName = input("Entrez votre nom :"'\n')
print("Bonjour " + userName + "!")

print("bla bla bla intro")
print("vous avez le choix entre", len(item), "items : ", *item, "mais votre sac ne peut contenir que", sizebackpack, "objets")
while len(backpack) != 2:
  backpack.clear()
  for i in range(0, len(item)):
#for i in int(len(item)):
    print("Choisissez votre", i+1, "item :")
    print("Souhaitez vous prendre", item[i], "?")
    if oneOrZero("0 = non, 1 = oui : ") == 1:
      backpack.append(item[i])
      print("Vous avez pris", item[i], '\n')
    else:
      print("Vous n'avez pas pris", item[i], '\n')
  if len(backpack) == 2:
    continue
  print('\n'"Vous n'avez rien/trop pris d'item ! Veuillez recommencer.", '\n')

print("Votre sac contient :")
print(*backpack)

animation(1,"#", 0.125, 25)

print("après un certains temps bla bla vous devez choisir un endroit pour constrtuire un abris, vous avez le choix entre la plage qui est dégagée, sans relief, mais qui proche de la mer, ou la forêt qui est plus éloignée de la mer mais qui est très dense et hostile.")

if oneOrZero("0 = la plage, 1 = la jungle : ") == 0:
  plage()

else:
    print("Vous avez choisi la jungle\n")
    animauxTues = animauxTues + animalSauvage("lion", 2, 0)


print('\n'"Vous êtes arrivé a la fin du du jeu !"'\n'"Voici un récapitulatif :")
print("- Vous avez tué(e)", animauxTues, "animaux")
#fait moi un code qui compare la liste itemUtilise avec la liste item et qui affiche les items non utilisés
print("- Vous n'avez pas utilisé", calculItem(), "item(s)")
print("- Vous avez tué(e)")
quit("Fin du jeu")
#fin du jeu :
