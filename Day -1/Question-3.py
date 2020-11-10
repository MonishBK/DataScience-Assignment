cp=int(input("cost price:\t"))
sp=int(input("selling price:\t"))

if cp < sp:
    print("Profit")
elif cp > sp:
    print("Loss")
else:
    print("Neither")