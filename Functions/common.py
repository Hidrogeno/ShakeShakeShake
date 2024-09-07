import matplotlib.pyplot as plt
import seaborn as sns

def plot(data_frame, x_label, y_label, title):
    plt.figure(figsize=(10,6))
    sns.barplot(x=data_frame.index, y=data_frame.values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()