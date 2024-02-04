import json
import os

class Item:
    def __init__(self, name: str, type: str, desc: str, tags: [], modifiers: dict):
        self.name = name
        self.type = type
        self.desc = desc
        self.tags = tags
        self.modifiers = modifiers

    def set_tags(self, *args):
        self.tags.clear()
        for tag in args:
            self.tags.append(tag)

    def set_modifiers(self, tag, level, desc):
        self.modifiers[tag][level] = desc

    def toJSON(self):
        return {self.name: {"name": self.name,"type": self.type,"tags": self.tags, "modifiers": self.modifiers}}

def save(item, filename='items.json'):
    data = load(filename)
    if item.name in data:
        return -1
    if os.stat(filename).st_size <= 1:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, sort_keys=False, indent=4)
    try:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
            existing_data.update(item.toJSON())
        else:
            existing_data = item.toJSON()
    except:
        return -1

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, sort_keys=False, indent=4)
            return 1
    except:
        return -1

def load(filename='items.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except:
        print("No data found or an error occured")
        return {}

def read(type="", searched=""):
    data = load()
    try:
        for key in data.keys():
            if type == "":
                print(key,data[key])
            else:
                for key2 in data[key].keys():
                    if searched in data[key][key2]:
                        print(key,data[key])
    except Exception as e:
        print("Error has occured: ",e)
        return -1
    return 1

def remove(item_name, filename='items.json'):
    data : dict = load()
    if item_name in data.keys():
        data.pop(item_name)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=4)
            return 1
    else:
        return -1

while True:

    choice = input("Do you want to create a new item? (y/n)  ")
    if choice.lower() == "n":
        break
    item_name = input("Choose a name for your item:\n")
    item_desc = input("Write a desc for your item:\n")
    item_type = input("Choose a type for your item:\n")
    item_tags = []

    while True:
        tag = input("Type in a tag you'd like to add. Leave empty if you wish to proceed.\n")
        if tag == "":
            break
        else:
            if not tag in item_tags:
                item_tags.append(tag)
            else:
                print("Tag was already added")
    modifier_tags = []

    while True:
        modifier_tag = input("Type in modifier tags you'd like to add. Leave empty if you wish to proceed.\n")
        if modifier_tag == "":
            break
        else:
            if not modifier_tag in modifier_tags:
                modifier_tags.append(modifier_tag)
            else:
                print("Modifier tag was already added")
    modifiers_dict = {}

    for modifier_tag in modifier_tags:
        print(f"--//{modifier_tag}//--\n")
        modifier_levels = ""

        while not modifier_levels is int:
            try:
                modifier_levels = int(input(f"How many levels would you like to add to modifier: {modifier_tag}?\n"))
                break
            except:
                print("You need to type in a number.\n")

        for level in range(int(modifier_levels)):
            print(f"--///{level}///--\n")
            modifier_desc = input(f"Write in description for this modifier level: {level} \n")
            to_dict = {level: modifier_desc}

            try:
                modifiers_dict[modifier_tag][level] = modifier_desc
            except:
                modifiers_dict.setdefault(modifier_tag, to_dict)

            print(modifiers_dict)
    new_item = Item(item_name,item_type,item_desc,item_tags,modifiers_dict)
    save(new_item)

read()