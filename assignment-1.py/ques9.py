string=input('enter a string:')
substring=input('enter a substring:')
index=string.find(substring)
if index !=-1:
     print(f"'{substring}' is present in '{string}'")
else:
        print(f"'{substring}' is not present in '{string}'")