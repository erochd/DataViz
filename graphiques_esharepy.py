import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



final_reviews = pd.read_csv('final_reviews_corrected.csv')

sns.countplot(x = "final_rating", hue="marketplace", data = final_reviews)
plt.xlabel('Notes Finales')
plt.ylabel('Nombre')
plt.title("Notes par marketplace")
plt.show()

#################################

top_sellers_rating = [3,8,9]

condition = final_reviews['seller_id'].isin(top_sellers_rating)
df_sellers_ratings = final_reviews[condition]

sns.countplot(x = "final_rating", hue="seller_id", data = df_sellers_ratings)
plt.xlabel('Notes Finales')
plt.ylabel('Nombre')
plt.title("Notes pour le top 3 des vendeurs")
plt.show()

######################

private_data = pd.read_csv("private_sales_data.csv")

private_data["day"] = pd.to_datetime(private_data["day"])

private_data["weekday"] = private_data["day"].dt.weekday

private_data["month"] = private_data["day"].dt.month

labels = ['janv', 'fev', 'mars', 'avr', 'mai', 'juin', 'juillet', 'aout', 'sept','oct']

private_data["mois_lettres"] = private_data["month"].map(dict(zip(range(1,13), labels)))
sns.countplot(x = "mois_lettres", order = ['janv', 'fev', 'mars', 'avr', 'mai', 'juin', 'juillet', 'aout', 'sept','oct'], data = private_data)
plt.xlabel('Mois')
plt.ylabel('Nombre')
plt.title("Nombre de ventes par mois")
plt.show()

labels_jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']

private_data['jours_semaine'] = private_data["weekday"].map(dict(zip(range(0,7), labels_jours)))
sns.countplot(x = "jours_semaine", order=['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'], data = private_data)
plt.xlabel('Jours de la semaine')
plt.ylabel('Nombre')
plt.title("Nombre de ventes selon le jour de la semaine")
plt.show()

############################

top_months = [4,1,6]
top_sellers = [4,8,10]

labels = ['janv', 'fev', 'mars', 'avr', 'mai', 'juin', 'juillet', 'aout', 'sept','oct']


condition_2 = private_data['seller_id'].isin(top_sellers)
df_months_sellers = private_data[condition_2]

df_months_sellers_new = df_months_sellers.groupby(['seller_id','month']).sum()
df_months_sellers_new.reset_index(inplace=True)
df_months_sellers_new["Mois"] = df_months_sellers_new["month"].map(dict(zip(range(1,13), labels)))
sns.catplot(x='seller_id', y='average_selling_price', hue = 'Mois', hue_order = labels, kind = 'bar', data=df_months_sellers_new)
plt.xlabel('Identifiant du vendeur')
plt.ylabel('Prix de vente moyen')
plt.title("Prix de vente moyen pour le top 3 des vendeurs entre janvier et octobre")
plt.show()