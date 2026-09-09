import pickle

filePath = "/Users/shengpang/Desktop/lblDev/IDAES/idaes-ui/running_server.pickle"
with open(filePath, "rb") as file:
    runningServer = pickle.load(file)
    print(runningServer)
