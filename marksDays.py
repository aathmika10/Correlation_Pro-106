import plotly_express as py
import csv
import numpy as np

def getData(dataPath):
    Marks=[]
    daysPresent=[]
    with open (dataPath) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            daysPresent.append(float(row["Days Present"]))
            Marks.append(float(row["Marks In Percentage"]))
    return{"x":daysPresent,"y":Marks}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation coefficient is:" ,correlation[0,1])

def setup():
    dataPath="marksDays.csv"
    dataSource=getData(dataPath)
    findCorrelation(dataSource)

setup()