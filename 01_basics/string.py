chai = "Masala chai"
first_char = chai[0]
print(first_char)

slice_chai = chai[0:6]
print(slice_chai)

num_list = "0123456789"
print(num_list[:])
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:2])
print(num_list[-1:])

print(chai.lower())
print(chai.upper())

chai = "    Masala chai    "
print(chai.strip())

chai = "Lemon chai"
print(chai.replace("Lemon","Ginger"))
print(chai)

chai = "Lemon, Ginger, Masala, Mint"
print(chai.split(", "))

chai = "Masala chai"
print(chai.find("chai"))

chai = "Masala chai chai chai"
print(chai.count("chai"))


chai_type = "Masala"
quantity = 2
order = "I ordered {} cups of {} chai"
print(order.format(quantity, chai_type))


chai_variety = ["Lemon", "Masala", "Ginger"]
print(", ".join(chai_variety))

print(len(chai))

for letter in chai:
    print(letter)

chai = "He said, \"Masala chai is awesome\" "
print(chai)

chai = r"Masala\nChai"
print(chai)

chai = r"c:\user\pwd"
print(chai)

chai = "Masala chai"
print("Masala" in chai)