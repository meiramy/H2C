def exception_test(index):
    try:
        if index is 0:
            1000 / 0
        elif index is 1:
            float("pi")
        elif index is 2:
            exception_test(1, 2, 3, 4)
        elif index is 3:
            exception_test(3)
        else:
            raise IndexError("invalid index")
        
    except ZeroDivisionError:
            print("* Zero division error captured.")
    except ValueError:
        print("* Value error captured.")
    except TypeError:
        print("* Type error captured.")
    except RecursionError:
        print("* Recursion error captured.")
    except IndexError:
        print("* Index error captured.")

for index in range(5):
    print("Trying to run: exception_test(", index, ")", sep="")
    exception_test(index)
