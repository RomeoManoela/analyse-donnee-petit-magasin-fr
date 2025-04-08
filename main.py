import numpy as np
import pandas as pd

import streamlit as st

st.title("Visualisation des données")

data: pd.DataFrame = pd.read_csv("data/ventes.csv")

# calculer une nouvelle colonne
data["Montant"]: pd.Series = np.round(data["Quantite"] * data["Prix_unitaire"], 2)

st.write("Données")
st.write(data)

# convertir la date en datetime
data["Date"]: pd.Series = pd.to_datetime(data["Date"])

mean: float = data["Montant"].mean()
max_montant: float = data["Montant"].max()
min_montant: float = data["Montant"].min()

# nombre de ventes par produit
ventes_par_produit: pd.DataFrame = (
    data.groupby("Produit")["Quantite"].sum().rename("Ventes")
)
print(ventes_par_produit)
ventes_par_produit.to_csv("data/ventes_par_produit.csv")

# ventes par mois
ventes_par_mois: pd.DataFrame = (
    data.groupby(data["Date"].dt.month_name(locale="fr_FR.utf8"))["Quantite"]
    .sum()
    .rename("Ventes")
    .rename_axis("Mois")
)
print(ventes_par_mois)
ventes_par_mois.to_csv("data/ventes_par_mois.csv")
