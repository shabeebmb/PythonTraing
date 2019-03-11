import fileone

print("Top livel filetwo.py")

fileone.func()

if __name__=="__main__":
    print("Filetwo.py is being executed directly")
else:
    print("filetwo ins being imported as a module and running")
