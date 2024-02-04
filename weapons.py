import json
import os

class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.tags = []

    def set_tags(self, *args):
        for tag in args:
            self.tags.append(tag)

    def toJSON(self):
        return {self.name: {"type": self.type,"tags": self.tags}}

def save(item, filename='items.json'):
    data = load(filename)
    if item.name in data:
        return -1
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            existing_data = json.load(f)
        existing_data.update(item.toJSON())
    else:
        existing_data = item.toJSON()

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(existing_data, f, ensure_ascii=False, sort_keys=True, indent=4)
        return 1

def load(filename='items.json'):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def read():
    data = load()
    for key in data.keys():
        print(key,data[key])


test_item = Item("Sword","Sword")
test_item.set_tags("Sword","Knight")
save(test_item)
read()