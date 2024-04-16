import datetime


#def my_current_time():
#    print(datetime.datetime.now().strftime("%H:%M"))


def stars(myFunction):
     def simpleWrapper():
         print("*****************************")
         myFunction()
         print("*****************************")


     return simpleWrapper


#current_time = stars(my_current_time)
#current_time()

@stars
def my_current_time():
    print(datetime.datetime.now().strftime("%H:%M"))

my_current_time()
