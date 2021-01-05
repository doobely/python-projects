
number=int(input("parakalu doste ton arithmo :"))
if number <2:
         print("o arithmos sas den einai protos")
#i = 0
for i in range(2,number):
    mod = number % i
    if mod == 0 :
        print("den einai protos")
        break
else:
    print("einai protos")
