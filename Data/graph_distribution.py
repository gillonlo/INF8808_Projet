from matplotlib import pyplot as plt
import pandas as pd

# Lire le fichier CSV dans un DataFrame pandas
chemin_fichier = 'projet_data_4.csv'
df = pd.read_csv(chemin_fichier, sep=";")
print(df)

# Sélectionner la colonne à utiliser
colonne = 'G-PK90'
df_select = df[colonne]

# Créer un histogramme avec 10 intervalles, une couleur de remplissage 'skyblue' et une couleur de bordure 'black'
plt.hist(df_select, bins=10, color='skyblue', edgecolor='black')

# Ajouter des étiquettes et un titre
plt.xlabel(colonne)
plt.ylabel('Fréquence')
plt.title('Histogramme de '+colonne)

# Enregistrer le graphique sous forme d'image PNG dans le dossier './graph' avec un nom spécifique
plt.savefig('./graph/4_Figure_'+colonne+'.png')