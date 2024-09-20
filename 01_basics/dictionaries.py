chai_types = {"Masala": "Spicy", "Ginger": "Zesty", "Green": "Mild"}

print(chai_types["Masala"])  

print(chai_types.get("Ginger"))
chai_types["Green"] = "Fresh"
print(chai_types)

for chai in chai_types:
    print(chai, chai_types[chai])

for key, value in chai_types.items():
    print(key, value)

if "Masala" in chai_types:
    print("I have masala chai")

print(len(chai_types))

chai_types["Earl Grey"] = "Citrus"
chai_types.pop("Ginger")
print(chai_types)

chai_types.popitem()
print(chai_types)

del chai_types["Green"]

print(chai_types)

chai_types_copy = chai_types.copy()

tea_shop = {
    "chai": {
        "Masala" : "Spicy",
        "Ginger" : "Zesty"
    },
    "Tea": {
        "Green": "Mild",
        "Black": "Strong"
    }
}

print(tea_shop)
print(tea_shop["chai"]["Ginger"])

squared_nums = {x:x**2 for x in range(6)}
print(squared_nums)

squared_nums.clear()
print(squared_nums)

keys = ["Masala", "Ginger", "Lemon"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys,default_value)

print(new_dict)
