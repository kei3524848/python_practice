def scope_test():
    def do_local():
        spam = "local name"
        print("this is local, not used global", spam)

    def do_nonlocal():
        nonlocal spam  # not working in python 2
        spam = "nonlocal spam"  # parent spam

    def do_global():
        global spam  # declare new variable
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assingment:", spam)
    do_nonlocal()
    print("After nonlocal assingment:", spam)
    do_global()
    print("After global assingment:", spam)


scope_test()
print("In global scope:", spam)
