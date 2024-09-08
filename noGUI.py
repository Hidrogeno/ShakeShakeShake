import os
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import Functions.plot as plot
mMin = 5.0

# Leemos el archivo
df = pd.read_csv(os.path.dirname(os.path.abspath(__file__))+"/Data/SSNMX.csv")

# Hacemos nueva entrada con la fecha ya formateada como a pandas le gusta
df["Date"] = pd.to_datetime(df["Fecha"])
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Usamos la libreria plot para mostrar las gráficas que queremos
plot.by_month(df,mMin)
plot.magnitude_by_month(df,mMin)

for mes in range(1,13):
    plot.month_by_year(df,mes,mMin)