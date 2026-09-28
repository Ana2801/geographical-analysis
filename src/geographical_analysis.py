# %%
import pandas as pd

from config import RAW_DATA

# 1. How many airports, airfields, and heliports exist in each country and continent?
# %%
airports = pd.read_csv(RAW_DATA / "airports.csv")
airports.drop_duplicates()
# %%
# Clean closed airports, airfields, and heliports
airports = airports[airports["type"] != "closed"]
# %%
# Removing missing countries and continents
airports_country = airports.dropna(subset="iso_country")
airports_continent = airports.dropna(subset="continent")
# %%
# Separated airports, airfields, and heliports:
sum_airports_country = (
    airports_country.groupby(["iso_country", "type"]).size().unstack(fill_value=0)
)
print(
    "Number of airports, airfields, and heliports in each country: \n",
    sum_airports_country,
)
# %%
sum_airports_continent = (
    airports_continent.groupby(["continent", "type"]).size().unstack(fill_value=0)
)
print(
    "Number of airports, airfields, and heliports in each continent: \n",
    sum_airports_continent,
)

# %%
# All airports, airfields, and heliports:
sum_all_country = airports_country.groupby("iso_country")["type"].size()
print(
    "Total number of airports, airfields, and heliports in each country: \n",
    sum_all_country,
)
# %%
sum_all_continent = airports_continent.groupby("continent")["type"].size()
print(
    "Total number of airports, airfields, and heliports in each continent: \n",
    sum_all_continent,
)


# 2. What is the average elevation of the airports, airfields, and heliports in each country?
# %%
# Separate airports, airfields and heliports in each country:
avg_elevation_separately = (
    airports.groupby(["iso_country", "type"])["elevation_ft"]
    .mean()
    .unstack(fill_value=0)
)
print(
    "Average elevation of airports, airfields, and heliports in each country: \n",
    avg_elevation_separately,
)

# %%
# All airports, airfields and heliports in each country:
avg_elevation = airports.groupby("iso_country")["elevation_ft"].mean()
print(
    "Average elevation of all airports, airfields, and heliports in each country: \n",
    avg_elevation,
)


# 3. What is the estimated population of each country?
# %%
geonames = pd.read_csv(RAW_DATA / "geonames.csv")
geonames.drop_duplicates()
# %%
geonames_population = geonames.dropna(subset="population")
estimated_population = geonames_population.groupby("country_code")["population"].sum()
print("Estimated population of each country: \n", estimated_population)


# 4. How many cities, towns, and other settlements are recorded in each country?
# %%
geonames_P = geonames[geonames["feature_class"] == "P"]
geonames_recorded_P = geonames_P.dropna(subset="name")  # recorded settlements
settlements = geonames_recorded_P.groupby("country_code")["feature_class"].size()
print("Number of settlements in each country: \n", settlements)


# 5. What are the minimum, maximum, and average elevations of settlements in each country?
# %%
geonames_elevation = geonames_P.dropna(
    subset="elevation"
)  # remove missing elevation values
min_elevation = geonames_elevation.groupby("country_code")["elevation"].min()
max_elevation = geonames_elevation.groupby("country_code")["elevation"].max()
avg_elevation = geonames_elevation.groupby("country_code")["elevation"].mean()
# %%
print("Minimum elevation of settlements in each country: \n", min_elevation)
# %%
print("Maximum elevation of settlements in each country: \n", max_elevation)
# %%
print("Average elevation of settlements in each country: \n", avg_elevation)


# 6. Which are the highest and lowest elevated settlements in the world with populations greater than 100,000?
# %%
geonames_population = geonames_elevation[geonames_elevation["population"] > 100000]
highest_elevated_settlements = geonames_population.loc[
    geonames_population["elevation"].idxmax()
]["name"]
lowest_elevated_settlements = geonames_population.loc[
    geonames_population["elevation"].idxmin()
]["name"]

print(
    "Highest elevated settlement in the world with populations greater than 100,000: ",
    highest_elevated_settlements,
)
print(
    "Lowest elevated settlement in the world with populations greater than 100,000: ",
    lowest_elevated_settlements,
)


# 7. Which are the highest and lowest elevated airports, airfields, and heliports in the world?
# %%
# Removing airports, airfields, and heliports with missing elevation values
airports_elevation = airports.dropna(subset="elevation_ft")

# %%
# Separate airports, airfields and heliports:
highest_elevated = airports_elevation.loc[
    airports_elevation.groupby("type")["elevation_ft"].idxmax(), ["type", "name"]
]
lowest_elevated = airports_elevation.loc[
    airports_elevation.groupby("type")["elevation_ft"].idxmin(), ["type", "name"]
]

print(
    "Highest elevated airport, airfield, and heliport in the world: \n",
    highest_elevated,
)
print("\n")
print(
    "Lowest elevated airport, airfield, and heliport in the world: \n", lowest_elevated
)

# %%
# All together:
all_highest_elevated = airports_elevation.loc[
    airports_elevation["elevation_ft"].idxmax()
]["name"]
all_lowest_elevated = airports_elevation.loc[
    airports_elevation["elevation_ft"].idxmin()
]["name"]

print(
    "Highest elevated airport, airfield, and heliport in the world: ",
    all_highest_elevated,
)
print(
    "Lowest elevated airport, airfield, and heliport in the world: ",
    all_lowest_elevated,
)


# %%
