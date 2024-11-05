def create_inventory(items):
    inventory={}
    for item in items:
        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]= 1
        

    return inventory
print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

    


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item]+=1

        else:
            inventory[item]=1
    return inventory
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item]-=1
            if inventory[item]<=0:
                inventory[item]=0
        
    return inventory
print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))
    


def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
   


def list_inventory(inventory):
    result=[]
    for item, quantity in inventory.items(): 
        if quantity > 0:  
            result.append((item, quantity)) 
    
    return result  
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))

