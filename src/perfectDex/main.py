import os 
import json

if __name__ == "__main__":
  print("Default")
  home = os.path.abspath(os.getcwd())
  dex = home + "\src\lib\dex"
  learnsets = home + "\src\lib\learnsets"

  for file in os.listdir(learnsets):   
    with open(learnsets + "\\" + file, "r") as f:
      #Kill the first line 
      f.readline()

      for row in f:
        #Split the CSV row into a list
        out = row.split(",")        
        #Remove empty string elements from the list
        out  = list(filter(lambda x: len(x) > 0, out))
        #Kill the newline char and the dex num
        out = out[1:-1]
        #Separate the elements into lists of [task, num] instead of task(num)
        for i in range(len(out)):
          if "(" in out[i]:
            #Get characters after the first parens, and remove the second parens
            num = out[i].split("(")[1][0:-1]
            out[i] = [out[i].split(" (")[0], num]
            print(out[i])
            
        print(out)   

  #Read the created CSV files for the remaining tasks
  for file in os.listdir(dex):    
    with open(dex + "\\" + file, "r") as f: 
      data = json.load(f)
      for i in data: 
        print(i,   data[i])
      
      f.close()
