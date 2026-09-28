# %%
import pandas as pd

from config import RAW_DATA

# %% Add columns from the 'geoname' table to 'allCountries' file
columns = [
    "geonameid",
    "name",
    "asciiname",
    "alternatenames",
    "latitude",
    "longitude",
    "feature_class",
    "feature_code",
    "country_code",
    "cc2",
    "admin1_code",
    "admin2_code",
    "admin3_code",
    "admin4_code",
    "population",
    "elevation",
    "dem",
    "timezone",
    "modification_date",
]

geonames = pd.read_csv(
    RAW_DATA / "allCountries.txt",
    sep="\t",
    header=None,
    names=columns,
    low_memory=False,
)


# %%
geonames.to_csv(RAW_DATA / "geonames.csv", index=False)
