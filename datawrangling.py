# Naam: Gerjan Remmelink
# Opdracht: Tech opdracht 2: Data wrangling

import pandas as pd

# Toon alle kolommen
pd.set_option('display.max_columns', None)

# Toon alle rijen
pd.set_option('display.max_rows', None)

#1. CSV inladen
df = pd.read_csv("/Users/remme/Downloads/movie_plots.csv", sep=",", encoding="utf-8")

#2. Inspectie
print(df.head())
print(df.info())

#3. Aantal films per Origin/Ethnicity
aantal_films = df["Origin/Ethnicity"].value_counts()
print(aantal_films)

#4. Bollywood films
bollywood_df = df[df["Origin/Ethnicity"] == "Bollywood"]
print(bollywood_df)

#5. Turkse films na 2000
turkish_after_2000 = df[
    (df["Origin/Ethnicity"] == "Turkish") &
    (df["Release Year"] > 2000)
]
print(turkish_after_2000)

#6. Subset van kolommen
new_df = df[["Title", "Release Year", "Origin/Ethnicity", "Plot"]]
print(new_df)

#7. Kolomnamen aanpassen
new_df = df[["Title", "Release Year", "Origin/Ethnicity", "Plot"]].copy()
new_df.rename(columns={"Release Year": "Year", "Origin/Ethnicity": "Origin"}, inplace=True)
print(new_df.head())

