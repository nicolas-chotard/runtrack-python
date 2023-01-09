def phare(marche, hauteur_marche):

  hauteur_marche_metre = hauteur_marche / 100


  distance = (marche * 2) * hauteur_marche_metre


  total_distance = distance * 5 * 7


  print(f"Pour {marche} marches de {hauteur_marche} cm, le gardien parcours {total_distance:.2f} m par semaine.")


phare(10, 20)

