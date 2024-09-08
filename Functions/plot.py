import matplotlib.pyplot as plt
import seaborn as sns

def plot(data_frame, x_label, y_label, title):
    plt.figure(figsize=(10,6))
    sns.barplot(x=data_frame.index, y=data_frame.values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation = 45)
    plt.show()

def by_month(data_frame, mMin):
    filtered_earthquakes = data_frame[data_frame["Magnitud"]>=mMin]
    earthquakes_by_month = filtered_earthquakes.groupby("Month").size()
    plt.figure(figsize=(10,6))
    sns.barplot(x=earthquakes_by_month.index, y=earthquakes_by_month.values)
    plt.xlabel("Mes")
    plt.ylabel("# de temblores")
    plt.title(f"Número de temblores de {mMin} o más por mes en México desde 1900")
    plt.show()

def magnitude_by_month(data_frame, mMin):
    filtered_earthquakes = data_frame[data_frame["Magnitud"]>=mMin]
    magnitude_by_month = filtered_earthquakes.groupby("Month")["Magnitud"].mean()
    plt.figure(figsize=(10,6))
    sns.barplot(x=magnitude_by_month.index, y=magnitude_by_month.values)
    plt.xlabel("Mes")
    plt.ylabel("Magnitud promedio")
    plt.title(f"Magnitud de temblores de {mMin} o más por mes en México desde 1900")
    plt.show()

def month_by_year(data_frame, mes, mMin):
    filtered_earthquakes = data_frame[data_frame["Magnitud"]>=mMin]
    mes_df = filtered_earthquakes[(filtered_earthquakes["Month"] == mes)]
    mes_by_year = mes_df.groupby("Year").size()
    meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
    plt.figure(figsize=(10,6))
    sns.barplot(x=mes_by_year.index, y=mes_by_year.values)
    plt.xlabel("Año")
    plt.ylabel("# de temblores")
    plt.title(f"Número de temblores de {mMin} o más en {meses[mes-1]} por año en México desde 1900")
    plt.xticks(rotation = 75)
    plt.show()
