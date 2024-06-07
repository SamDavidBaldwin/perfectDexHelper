import os 
import json
from perfectDex import perfectDex

def createJSONForDex(list):
  with open(dex + "\\" + list[0] + "_" + list[1].lower() + ".json", "w", encoding = 'utf-8') as f:
    #Create Empty JSOn
    output = {}
    #Manually create name field
    output["name"] = list[1]
    #Create JSON for tasks
    output["tasks"] = {}
    #For each task, create a pair of the number of times the task has been achieved and the number required to complete
    for element in list[2:]:
      output["tasks"][element[0]] = [0,  element[1]]
    json.dump(output, f)

def readInTasks():
  for file in os.listdir(tasks):   
    with open(tasks + "\\" + file, "r") as f:
     #Kill the first line 
      f.readline()
      for row in f:
      #Split the CSV row into a list
        out = row.split(",")        
        #Remove empty string elements from the list
        out  = list(filter(lambda x: len(x) > 0, out))
        #Kill the newline char and the dex num
        out = out[0:-1]
        #Separate the elements into lists of [task, num] instead of task(num)
        for i in range(len(out)):
          if "(" in out[i]:
            #Get characters after the first parens, and remove the second parens
            num = out[i].split("(")[1][0:-1]
            out[i] = [out[i].split(" (")[0], num]
        createJSONForDex(out)     

def resetStatus():
  #Idea for reset
  # if (input("Would you like to reset")) == "T":
  #   for file in os.listdir(dex):
  #    if os.path.exists(dex + "\\" + file):
  #     os.remove(dex + "\\" + file)
  return

def createProfile():
  location = home + "\\src\\lib\\user\\"
  print(location)
  while True: 
    name = input("Provide a user name")
    if os.path.exists(location+name):
       pass
    else:
      os.mkdir(location+name)
      break

def loadProfile():
  return

def removeProfile():
  return

def updateProfileManual():
  return

def updateProfileAutomatic():
  return

def monitor():
  return

def suggest(): 
  sugg = perfectDex()
  sugg.testMethod()

if __name__ == "__main__":
  print("Default")
  home = os.path.abspath(os.getcwd())
  dex = home + "\src\lib\dex"
  tasks = home + "\src\lib\\tasks"
  exit = True

  options = [
    "<--------------COMMANDS ------------->",
    "1: Init",
    "2: Reset",
    "3: New Profile",
    "4: Load Profile",
    "5: Remove Profile",
    "6: Update Profile (Manual)",
    "7: Update Profile (Automatic)",
    "8: Monitor Screen for Updates",
    "9: Suggestions",
    "0: Quit", 
    "--------------------------------------"
  ]

  func = {
    "1": readInTasks,
    "2": resetStatus,
    "3": createProfile,
    "4": loadProfile,
    "5": removeProfile,
    "6": updateProfileManual,
    "7": updateProfileManual,
    "8": monitor,
    "9": suggest,
  }

  while exit == True:
    print("\n".join(options))
    command = input("Command: ")
    if command == "0":
      exit = False
      break
    if command in func:
      func[command]()
    else: 
      print("Command not found")
    
    
    
  #Reading in the master tasks file to create individual CSV's for each dex entry
      #Create the CSV file in the dex
  #Read the created CSV files for the remaining tasks
  #for file in os.listdir(dex):    
    #with open(dex + "\\" + file, "r") as f: 
     # data = json.load(f)
      #for i in data: 
      #  print(i,   data[i])
      #
      #f.close()
