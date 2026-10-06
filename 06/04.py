from collections import defaultdict


defdict = defaultdict(lambda: "000-000-0000")
defdict.update({"name": "Alice", "age": 30, "city": "New York"})
print(defdict)
print(defdict["name"])
print(defdict["phone"])
print(defdict)
