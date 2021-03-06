from ast import literal_eval
import csv

def getDataDict(filename):
    with open('Data/'+filename+'.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row is not None:
                for key, colStr in row.items():
                    try:
                        row[key] = literal_eval(colStr)
                    except:
                        raise Exception("Data Formated badly:", colStr, "in \""+ str(dict(row)) +"\"")
                return dict(row)
        return {}

def addDataItem(filename, key, value):
    fieldnames = list(getDataDict(filename).keys())
    d = getDataDict(filename)
    if key in d:
        return False
    with open('Data/'+filename+'.csv', 'w') as csv_file:
        d[key] = value
        fieldnames.append(key)
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(d)
    return True

def editDataItem(filename, key, value):
    key = str(key)
    d = getDataDict(filename)
    if key not in d:
        return False
    d[key] = value
    with open('Data/'+filename+'.csv', 'w') as csv_file:
        fieldnames = list(d.keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(d)
    return True

def deleteDataItem(filename, key):
    d = getDataDict(filename)
    if key not in d:
        return False
    del d[key]
    with open('Data/'+filename+'.csv', 'w') as csv_file:
        fieldnames = list(d.keys())
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(d)
    return True

def tupleToHex(color):
    if not isinstance(color, tuple) and len(color) != 3:
        raise AssertionError(color + "is not a tuple of length 3")
    colHex = ""
    for val in color:
        mod = str(hex(int(val)))[2:]
        colHex += mod if len(mod) > 1 else '0'+mod
    return colHex


def colorDifference(colA, colB):
    return (colA[0]-colB[0],colA[1]-colB[1],colA[2]-colB[2])

if __name__ == "__main__":
    addDataItem('sequences', 'FadeTime', 1)
