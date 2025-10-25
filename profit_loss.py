costp = float(input("enter your cost : "))
salep = float(input("enter your sale : "))

if costp > salep:
    loss = salep-costp
    print("loss is : ",loss)
else:
    profit = costp-salep
    print("Profit is : ",profit)