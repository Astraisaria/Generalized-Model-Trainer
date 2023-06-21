import pandas as pd
from sklearn import preprocessing as p

def openFile(fPath):
    if fPath[-3:] == "csv":
        f = pd.read_csv(fPath)
    elif fPath[-4:] == "xlsx":
        f = pd.read_excel(fPath)

def diplayTop(f, n = 10):
    f.head(n)

def displayBottom(f, n = 10):
    f.tail(n)

def displayFileInformation(f):
    shape = f.shape
    nRows = shape[0]
    nColumns = shape[1]
    cols = f.columns.tolist()
    colDataTypes = [f[i].dtype for i in cols]
    for i in range(nColumns):
        if colDataTypes[i] == "object":
            colDataTypes[i] = "string"
    #f.iloc[:, cols] or f.iloc[:, [col1, col2, etc]] chooses those columns
    print(f"Here is some basic information about the inputted data:\nNumber of rows - {nRows}\nNumber of columns - {nColumns}\n")
    for i in range(nColumns):
        print(f"{i + 1}. {cols[i]} ({colDataTypes[i]})")
    print("The following columns have empty values:\n")

def transData(f, cols, colDataTypes):
    for i in range(len(cols)):
        if colDataTypes[i] == "string":
            f[cols[i]] = f[cols[i]].astype(float)
    mm = p.MinMaxScaler()
    fFloat = f.loc[:, f.dtypes == "float64"]
    fScaled = pd.DataFrame(mm.fit_transform(fFloat), index = fFloat.index, columns = fFloat.columns)
    dupl = fScaled.T[fScaled.T.duplicated()]
    f.drop(dupl.columns.tolist(), axis = 1)

def dataFill(f, colName):
    f[colName] = f[colName].fillna(f[colName].mean())