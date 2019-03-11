def func():
   print("function running in fileone.py")

print("Top level print inside fileone.py")

if __name__=="__main__":
    print("fileone.py is being run Directly")
else:
    print("file one ins being imported as a module and running")