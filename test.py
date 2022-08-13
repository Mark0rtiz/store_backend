
me = {
    "first_name": "Mark",
    "last_name": "Ortiz",
    "fav_color": "red",
    "hobbies": [],
    "address": {
        "number": 4300,
        "street": "Newton",
        "city": "San Diego",
    }
}

# get data from dict
print(me["first_name"])

#modify
me["fav_color"] = "pink"

#add
me["age"] = 31

# read non existing key
# print(me["title"]) #crash the code

#check if the key exists 
if "title" in me:
    print(me["title"])

address = me["address"]
print(address["street"] + "" + str(address["number"]))