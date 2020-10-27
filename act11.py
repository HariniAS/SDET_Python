fruits = {"apple":"20",
        "pear":"30",
        "manog":"20",
        "banana":"15",
        "kiwi":"5"}
userInput = input("Enter the fruit you want: ").lower()
for x in fruits:
    if (x==userInput):
        print("User selected fruit ",userInput," available in the list at price ", fruits[x])
    else:
        print("User sleected fruit ",userInput," not available in the list")