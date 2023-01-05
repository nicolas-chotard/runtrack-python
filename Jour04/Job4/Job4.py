def fruits():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append(["melon"])
    fruits.insert(2,"mangue")
    return fruits
print(fruits())