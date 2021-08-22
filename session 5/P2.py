Dict1={
    "Key 1":"value 1",
    "key 2":"value 2",
    2:[3,4,6,8],
    "tuple":(23,56,46,88),
}

print(list(Dict1.keys()))
print(list(Dict1.values()))
print(list(Dict1.items()))
Dict1.__setitem__("key3","value4")
print(Dict1)

# Dict2={
#     "Key 1":"value1",
#     "key5":"value7",
#     "kay6":"value8"
# }
# Dict1.update(Dict2)
# print(Dict1)
# print(Dict1.get("Key 1"))
# print(Dict1["key 1"])



