thisdict = {
  "brand": ["Ford", "Chevy", "Dodge",],
#   "electric": False,
#   "year": 1964,
  "colors": ["red", "white", "blue"]
}

# thisdict["colors"].append("green")
# print("{} comes in {}".format(thisdict["brand"],thisdict["colors"][0]))

for k,v in thisdict:
    print(k[0])
    print(v[0])
    # for i in range(0,len(v)):
    #     print("{}: {}").format(k,v[i])

# print(thisdict)