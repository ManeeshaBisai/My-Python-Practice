"""Set = Set is the collection of the unordered items.
   Each element in the set must be unique & immutable."""

collection = {1,2,3,4,5,"mani","bisai"}
print(collection)
print(type(collection))
print(len(collection))

#repeated elements stored only once,so it resolved to {1,2,5,"mani","bisai"}
collection = {1,2,2,2,5,"mani","mani","bisai"}
print(collection)
print(type(collection))
print(len(collection))