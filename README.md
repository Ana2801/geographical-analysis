# geographical-analysis
Data analysis project for gaining insights related to airports, airfields, heliports, settlements, elevation, and population in each country across the world.

Using data from two data sources:

- OurAirports
- GeoNames

The GeoNames `allCountries.txt` file does not contain column headers.
The `add_columns.py` script assigns the official 'geonames' table column names and saves the resulting dataset as `data/raw/geonames.csv`.

Data processing and developing data solutions from the files in `data/raw` folder is done in the `geographical_analysis.py` script.