def hello(text,n):
    flen = 2
    if flen < len(text):
       flen = len(text)
    substr = text[:flen]
    result = ""
    for i in range(n):
          result=result+substr
    return result
print(hello("acb",2))
print(hello(" b",5))
