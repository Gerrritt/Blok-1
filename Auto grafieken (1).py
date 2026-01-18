# Naam: Gerjan Remmelink
# Datum: 28-9-2025
# UItleg code: In deze code zijn twee grafieken gemaakt uit een de dataset die over autoprijzen gaat.
# Packages importeren
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset inladen
df = pd.read_csv("/Users/remme/Downloads/Datasets voor tech opdracht 3/vehicle_price_prediction.csv")  # pas pad aan indien nodig

# Data schoonmaken
df_clean = df.dropna(subset=["mileage", "price", "year", "transmission"])

# 1. Scatterplot: mileage vs price, kleur = year
plt.figure(figsize=(12,8))
sc = plt.scatter(
    df_clean["mileage"],
    df_clean["price"],
    c=df_clean["year"],
    cmap="viridis",
    alpha=0.7
)
plt.xlabel("Kilometerstand")
plt.ylabel("Prijs (USD)")
plt.title("Relatie tussen kilometerstand, prijs en bouwjaar")
cbar = plt.colorbar(sc)
cbar.set_label("Bouwjaar")
plt.show()

# 2. Barplot: gemiddelde prijs per merk en transmissie, uitgesplitst per brandstof
# Om overzicht te houden nemen we de top 10 meest voorkomende merken
top_makes = df_clean["make"].value_counts().nlargest(10).index
df_top = df_clean[df_clean["make"].isin(top_makes)]

plt.figure(figsize=(14,8))
sns.barplot(
    data=df_top,
    x="make",
    y="price",
    hue="transmission",
    ci=None,
    order=top_makes  # zorgt dat merken in volgorde van populariteit blijven
)
plt.title("Gemiddelde prijs per merk en transmissietype (top 10 merken)", fontsize=16)
plt.xlabel("Merk")
plt.ylabel("Gemiddelde prijs (USD)")
plt.legend(title="Transmissie")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
