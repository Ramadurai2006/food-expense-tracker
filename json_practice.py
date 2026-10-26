import json
expenses=[{"category":"food","amount":150},{"category":"travel","amount":50}]
with open("expenses.json","w")as file:json.dump(expenses,file,indent=4) 
print("expenses saved successfully!")
with open("expenses.json","r")as file:
    saved_data = json.load(file)
    print(saved_data)