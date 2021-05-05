from datetime import datetime

class Login:
    def __init__(self, id,time,Time, km,rate,price,userParsedDate,userInputDateTime,percentage,gst,password,check,display,getdetails,choice,micro,mini,prime):
        self.id = "1112"
        self.password = "1211"
        self.micro = "1"
        self.mini = "2"
        self.prime = "3"
        self.rate = rate
        self.Distance = km
        self.price = price
        self.userInputDateTime = userInputDateTime
        self.userParsedDate = userParsedDate
        self.time = time
    def getdetails(self):
        self.log_userID = input("Enter your userID: ")
        self.log_password = input("Enter password: ")
        Login.check(self)
    def check(self):

        if(self.id == self.log_userID and self.password == self.log_password):
            print("Login successful")
            Login.display(self)
        else:
            print("Invalid Credentials")
            Login.getdetails(self)

    def display(self):
        print("micro")
        print("mini")
        print("prime")
        self.choice = input("Enter choice: ")
        Login.choice(self)
    def choice(self):
        if(self.micro == self.choice):
            print("The selected car is micro and the price per km is 10")
            self.rate = 10
            self.Price = " "
            Login.priceCalculation(self)

        elif(self.mini == self.choice):
            print("The selected car is mini and the price per km is 15")
            self.rate = 15
            self.Price = " "
            Login.priceCalculation(self)

        elif(self.prime == self.choice):
            print("The selected car is prime and the price per km is 20")
            self.rate = 20
            self.price = " "
            Login.priceCalculation(self)

    def priceCalculation(self):
        self.km = int(input("Enter the km to travel: "))
        self.price = self.rate * self.km
        self.percentage = (self.price * 7)/100
        self.gst = self.percentage + self.price
        print(" Total Amount including GST 7% : " + str(self.gst))
        Login.journeyDetails(self)
    def journeyDetails(self):
        self.userInputDateTime = input("Enter the date and time to Travel in DD/MM/YYYY HH:MM:SS:")
        self.userParsedDate = datetime.strptime(self.userInputDateTime,"%d/%m/%Y %H:%M:%S")
        self.time = self.userParsedDate.time()
        now = datetime.now()
        if self.userParsedDate < now:
            print("The date and time is invalid Please enter the future value")
            Login.journeyDetails(self)
        else:
            print("The date and time you selected is available")
            Login.finalAmount(self)
    def finalAmount(self):
        if self.time.hour > 5:
            if self.time.hour < 7:
                self.percentage = (self.gst * 1.25) / 100
                self.finalAmount = (self.gst+self.percentage)
                print("The Final Amount is :",str(self.finalAmount))
                self.age = input("Enter Your Age: ")
                if self.age >= str(60):
                    self.discountAmount = self.finalAmount / 2
                    print("You are eligible for 50% discount your travel amount is: ",str(self.discountAmount))
                else:
                    print("You are not eligible for 50% discount your travel amount is: ", str(self.finalAmount))
            else:
                print(" Total Final Amount is : ", str(self.gst))
                self.age = input("Enter Your Age: ")
                if self.age >= str(60):
                    self.discountAmount = self.gst / 2
                    print("You are eligible for 50% discount your travel amount is: ", str(self.discountAmount))
                else:
                    print("You are not eligible for 50% discount your travel amount is: ", str(self.gst))



log = Login("id","Time","password","time","check","userParsedDate","getdetails","userInputDateTime","micro","mini","prime","display","choice","rate","km","price","perecentage","gst")
log_userID = "id"
log_password = "password"
log.getdetails()
log_choice = "choice"
log_Distance = " Distance "
log_rate = "rate"
log_price = "price"
log_userParsedDate = "userParsedDate"
log_Time = "Time"




