#I want you to take some system that exists in real life and try to approximate it in a very simplified version. 
# Make sure to package this inside a function.

#I'm using the password example for this.
i = 0
numbers = ["0","1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","^","&","*",]
while i == 0:
    password = input("Passwords must have one uppercase and lowercase letter, one number, and one other symbol (!,@,#,$,%,^,&,*).\n\n Enter your desired password here:")
    #Instructions for password creation
    
    if password.lower() != password and password.upper != password:
        for x in numbers:
            if x in password:
                for s in symbols:
                    if s in password: 
                        i = 1
    #This if-for chain just goes through the different standards one-by-one. 
    #First it checks for uppercase and lowercase by making sure it isn't fully uppercase or fully lowercase
    #Second it checks for a number
    #third it checks for a symbol
    if i == 1:
        print(f"Your new password is {password}")
    else:
        print("Please create a password which follows our standards for password security.")
