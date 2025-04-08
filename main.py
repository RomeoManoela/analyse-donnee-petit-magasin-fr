import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("Visualisation des données de ventes")

# Chargement et préparation des données
data: pd.DataFrame = pd.read_csv("data/ventes.csv")
data["Montant"]: pd.Series = np.round(data["Quantite"] * data["Prix_unitaire"], 2)
data["Date"]: pd.Series = pd.to_datetime(data["Date"])

# 1. Statistiques principales
mean: float = data["Montant"].mean()
max_montant: float = data["Montant"].max()
min_montant: float = data["Montant"].min()
idx_max: int = data["Montant"].idxmax()
idx_min: int = data["Montant"].idxmin()

stats_df: pd.DataFrame = pd.DataFrame(
    {
        "Statistique": ["Moyenne", "Maximum", "Minimum"],
        "Valeur": [mean, max_montant, min_montant],
        "Produit": ["", data.loc[idx_max, "Produit"], data.loc[idx_min, "Produit"]],
    }
)

st.write("### Statistiques clés")
st.write(stats_df)

# 2. Ventes par produit
ventes_par_produit: pd.DataFrame = (
    data.groupby("Produit")["Quantite"].sum().rename("Quantité").rename_axis("Produit")
)
st.write("### Ventes par produit")
st.bar_chart(ventes_par_produit)

# 3. Ventes par mois
ventes_par_mois: pd.DataFrame = (
    data.groupby(data["Date"].dt.month_name(locale="fr_FR.utf8"))["Quantite"]
    .sum()
    .rename("Quantité")
    .rename_axis("Mois")
)
st.write("### Ventes par mois")
st.bar_chart(ventes_par_mois)

# 4. Distribution des montants
st.write("### Distribution des montants")
fig, ax = plt.subplots()
ax.hist(data["Montant"], bins=20, edgecolor="black")
ax.set_xlabel("Montant")
ax.set_ylabel("Fréquence")
ax.set_title("Distribution des montants de vente")
st.pyplot(fig)
