import pandas as pd
def load_data():
    data1 = pd.read_csv("data/saudi-arabia-planned-and-installed-renewables-by-project.csv", sep=';')
    data2 = pd.read_csv("data/renewable_energy_projects.csv", sep=',')
    return data1, data2

def split_installed_planned(df):
    installed = df[df["Installed / Planned"] == "Installed"]
    planned = df[df["Installed / Planned"] == "Planned"]
    return installed, planned
