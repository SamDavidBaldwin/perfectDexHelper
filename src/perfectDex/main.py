import os 
import json

if __name__ == "__main__":
  print("Default")
  home = os.path.abspath(os.getcwd())
  dex = home + "\src\lib\dex"


  for file in os.listdir(dex):    
    with open(dex + "\\" + file, "r") as f: 
      data = json.load(f)
      for i in data: 
        print(i,   data[i])
      
      f.close()
