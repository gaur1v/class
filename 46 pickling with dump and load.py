import pickle

l=[12,34,56,78,90]
file=open('46 pickling with dump and load.py.txt',"wb")

pickle.dump(l,file)
file.close()

print(l)