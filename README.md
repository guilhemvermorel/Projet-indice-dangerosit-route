# Projet : Création d'un indice de dangerosité des routes pour l'application Waze

Le projet a commencé le 03 octobre 2021 et pris fin le 15 décembre 2021.


<B> Contexte : </B>

  La sécurité routière est à l’heure actuelle un axe politique prioritaire, la France à pour objectif de passer en dessous du seuil de 2 000 morts sur ses routes. Waze, qui est une application mobile d’aide à la conduite et d’assistance de navigation, cherche à participer activement à la diminution d’accidents mortelles en prévenant leurs utilisateurs d’évènement dangereux. En effet, depuis août 2020, à l’approche d’un passage à niveau l’application envoie aussi un message « Même près de chez moi je reste prudent. » aux utilisateurs ayant comme point de départ leur domicile, car selon leurs études les utilisateurs ont tendances à être moins vigilent dans les zones qu’ils connaissent.


<B> Problématique : </B>

  Actuellement, l’application ne dispose d’aucun indicateur pour fournir à ses usagers un indice sur le niveau de dangerosité de la route. Sur l’interface, seul la limitation de vitesse apparaît. Hors à elle seul, elle ne suffit pas a caractériser le danger . Ainsi, à partir de données d’accidents géolocalisées et des caractéristiques propres aux routes où ont eu lieu ces accidents, nous avons créer un indice de dangerosité de la route permettant d’évaluer la dangerosité de n’importe quelle route.


<B> Réalisation : </B>
  
  Ce git contient ainsi le programme qui caractérisent l'indice de dangerosité d'une route à partir de l'algorithme KModes. Il s'agit d'un aglorithme de clustering qui utilise la méthode des K plus proches voisins sur des variables catégoriales. 
  Le Dataset correspondant comporte un ensemble d'accidents et des variables associées à la forme de la route, la luminosité, etc. et est disponible sur 
 https://www.data.gouv.fr/fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2020/, qui contient des accidents de toute la France entre 2005 et 2020, et possède également un descriptif complet des variables.
  Le principe est le suivant, nous regroupons avec cet algorithme les routes qui se ressemblent entre elles. En classant, ensuite, ces différents clusters par nombre d'individus à l'intérieur, on obtient une échelle de dangerosité des routes. 
  La suite est alors simple, pour chaque nouvelles routes que l'on veut tester, on récupère ses informations sur l'API d'Open Street Map et on identifie son cluster d'appartenance. 
  
  On pourrait même aller plus loin en rajoutant des informations temporelles comme la météo, l'heure, la fréquentation. 
