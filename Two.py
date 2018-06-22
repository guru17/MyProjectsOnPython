import one

one.func()

print("Top level print in two.py")

if __name__ == "__main__":
    print("Two.py is beeing running directly")
else:
    print("Two.py has been imported")
