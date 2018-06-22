def new_dec_func(original_func):

    def wraper():
        print("Wraper func 1")

        original_func()

        print("Wraper func 2")

    return wraper

@new_dec_func
def display_func():
    print("I am display  func()")
