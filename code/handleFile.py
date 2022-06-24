def CreateFile(data,title):
    try:
        name ="../results/"+title+".txt"
        with open(name, "w", encoding="utf-8") as f:
            f.write(data)
            f.close()
        return "File Successfully Written"
    except:
        return "Error! While Writing File"
