import numpy as np
import pandas as pd

data: pd.DataFrame = pd.read_csv('data/ventes.csv')

# convertir la date en datetime
data['Date']: pd.Series = pd.to_datetime(data['Date'])

# calculer une nouvelle colonne
data['Montant']: pd.Series = np.round(data['Quantite'] * data['Prix_unitaire'], 2)

mean: float = data['Montant'].mean()
max_montant: float = data['Montant'].max()
min_montant: float = data['Montant'].min()

# nombre de ventes par produit
ventes_par_produit: pd.DataFrame = data.groupby('Produit')['Quantite'].sum()
print(ventes_par_produit)






