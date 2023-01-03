def Produits_Alimentaire(type, saison):
  if type == "fruits":
    if saison == "hiver":
      print("orange, mandarine et kiwi")
    elif saison == "été":
      print("Poire, fraise, cassis")
  elif type == "légume":
    if saison == "hiver":
      print("carotte, topinambour, endive")
    elif saison == "été":
      print("artichaut, aubergine, navet")


Produits_Alimentaire("légume", "été")
Produits_Alimentaire("fruits", "hiver")