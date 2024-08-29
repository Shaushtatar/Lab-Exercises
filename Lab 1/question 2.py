#Question 2
# Meet George 😺. 
# He's a very superstitious cat who suffers from triskaidekaphobia and heptadecaphobia. 
# That means he's scared of the numbers 13 and 17 and everything divisble by them! 
# Unfortunately, George LOVES to count. 
# Build a program for George that counts from 0 to 100 but takes out all the pesky numbers that can be divided by 13 or 17. 
# Store them in a list so he's free to count as often as he likes!
list_for_george = []
for i in range(1,101):
    if i%13 != 0 and i%17 != 0:
#divisible by 13 and 17 will mean modulo 13 or modulo 17 is zero
        list_for_george.append(i)
print(list_for_george)