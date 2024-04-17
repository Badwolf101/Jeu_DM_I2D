from time import sleep

#variables globales
#variables du jeu :
item = ["machette", "briquet", "couteau"]


#joueur :
userName = ""
backpack = []
sizebackpack = 2

#id des objets :
#idmachette = 0 | idbriquet = 1
#1 veut dire possédé, 0 veut dire non pris par le joueur



t = ["a", "b", "c", "d"]
t = [34, 56, 2]
t_vide = []

#logo :
monLogo = '''        .$$$$$:$$$:$$$$$$$     _..._        .$$$SSSSSS$$$$$$$$$.
       .$$$$$:$$$$:$$$$$$$    ~.sggg.        "  .~(g )$$$$$$$$$$.
       $$$$$:$$$$$:$$$$$$$ .sS$$$$$$$$s.     : '"--"' `$$$$$$$$$$.
       `$$$:$$$$$$:$$$$$$$.$$" .. g"-. `.    `.-.._    `$$$$$$$$$$
        $$$:$$$$$$:$$$$$$$`$' ' `._.'   :      `---      $$$$$$$$$.
        $$$:.$$$$$:$$$$$$$    `---'  _.'                 $$$$$$$$$$$.
        $$$$$:$$$$:$$$$$$s      ----"           .        $$$$$$$$$$$$.
        $$$$$`.$$$:$$$$$$$.                      `-._   .$$$$$$$$$$$$$$Sss.
        $$$$$$`;$$:$$$$$$$$.         _.:         .'   ;  $$$$$$$$$$$$$$$$$$$.
       .s$$$$$$'$$`.$$$$$$$$.      .'  `.       ' _ .`.  $$$$$$$$$$$$$$$$$$$$Ss.
     .s$$$$$$$$$$$$:$$$$$$$$$     :  _   ~~-...'.'.'  :  $$$$$$$$$$$$$$$$$$$$$$$
   .s$$$$$$$$$$$$$$`.$$$$$$$$s      : .~-,-.-.~:'.'   :  $$$$$$$$$$$$$$$$$$$$$$
 .s$$$$$$$$$$$$$$$$$`$$$$$$$$$$.    `  ~-.`"""'.'      `.$$$$$$$$$$$$$$$$$$$' '''

#fonctions :
def readbackpack():
  for i in range(0, len(backpack)):
    if backpack[i] != 0:
        print(item[i])

#début du jeu :
print("Bienvenue dans >>>nomdu jeu<<<")
print(monLogo)
userName = input("enter votre nom :"'\n')
print("Hello " + userName + "!")

print("bla bla bla intro")
print("vous avez le choix entre", len(backpack), "items : ", item, "mais votre sac ne peut contenir que", sizebackpack, "objets")
#for i in range(0, len(backpack)):
for i in range(0, len(backpack)):
    print("choisissez votre", i+1, "item :")
    print("souhaitez vous prendre", item, "?")
    buffer = int(input("1 = oui, 0 = non :"))
    sleep(10)
    if buffer == 1:
        backpack.append(item[i])
        print("vous avez pris", item[i])
    else:
        print("vous n'avez pas pris", item[i])

print("vous avez pris")
print(backpack)
#print("vous avez pris")
#print(readbackpack())


