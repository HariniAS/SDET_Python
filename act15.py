try:
    print (x)
except(NameError):
    print("Encountered name error")
except:
    print("A different error")
else:
    print("No error")
finally:
    print("End of code")
