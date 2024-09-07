import os
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import Functions.common as funciones
mMin = 6.0
mMax = 6.0
# Leemos el archivo
df = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Data/SSNMX69.csv")

# Hacemos nueva entrada con la fecha ya formateada como a pandas le gusta
df["Date"] = pd.to_datetime(df["Fecha"])
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Creamos otros data frames
earthquakes_by_month = df.groupby("Month").size()
magnitude_by_month = df.groupby("Month")["Magnitud"].mean()

funciones.plot(earthquakes_by_month, "Mes", "#", f"Número de temblores de {mMin} o más por mes en México desde 1900")
funciones.plot(magnitude_by_month, "Mes", "Magnitud", f"Magnitud de temblores de {mMin} o más por mes en México desde 1900")

# Otra vez, para ver los temblores en septiembre por año
september_df = df[(df["Month"] == 9) & (df["Magnitud"] >= mMax)]
september_by_year = september_df.groupby("Year").size()
funciones.plot(september_by_year, "Año", "#", f"Número de temblores de {mMax} o más en Septiembre por año en México desde 1900")