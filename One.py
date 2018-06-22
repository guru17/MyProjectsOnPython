def func():
    print("Func() in one.py")

print('Top level Print() in one.py')

if __name__ == "__main__":
    print("One.py is being running directly")
else:
    print("One.py has been imported")
