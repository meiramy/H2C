number = float(input("For what number is the inverse calculcated? "))
try:             
    inverse = (1/number)
    print("The inverse of the number ",number," is ",inverse)

except ZeroDivisionError:
    print("There is no inverse for zero.")

finally:
    print("Thank you and goodbye.")
