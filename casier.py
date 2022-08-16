def casier():

  print("! casier ! \n")
  print("pour plus d'aide taper 'aide' \n")
  
  #règle du jeu :
  def aide():
    print("""règle du jeu :
  - gesion :
  
    ° création : vous pouvez en crée avec un code à 4 
      chiffres (le prix des casier influs sur la sécurité)
    
    ° modification : vous pouvez modifier le code des
      casier
    
    ° éléments : vous povez ajouter des éléments dans
      votre casier, ce qui peut vous raporter de l'argent,
      plus l'objet vaux chère, plus vous en gagnerez par 
      rapport au temps
  
  
  - attaque :
  
    ° attaque : mes autres utilisateur peuvent attaquer
      vos casier via le moyens qu'ils souhaite, 
      brute force, failles...
    ° sécurité : avec des amélioration vous pouvez mieux
      sécurisé vos casier

  - commandes: 'commandes' pour la liste des commandes
    """)

  def commandes():
    #faire quelque chose
  
  console = input("casier $ ")
  
  if console == 'aide':
    print("\n")
    aide()

casier()


