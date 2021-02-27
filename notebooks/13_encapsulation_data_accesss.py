#!/usr/bin/python3

class Phone:
    username = "Kate"                # public variable
    __serial_number = "11.22.33"     # private variable
    __how_many_times_turned_on = 0   # private variable

    def call(self):                  # public method
        # self.__turn_on()
        print( "Ring-ring!" )

    def __turn_on(self):             # private method
        self.__how_many_times_turned_on += 1 
        print( "Times was turned on: ", self.__how_many_times_turned_on )

my_phone = Phone()

my_phone.call()
# print( "The username is ", my_phone.username )
# my_phone.turn_on()
# my_phone.__turn_on()
# print( “Turned on: “, my_phone.__how_many_times_turned_on)
# print( “Turned on: “, my_phone.how_many_times_turned_on)
# will produce an error

# однако, в Python есть способ доступа к таким данным
# my_phone._Phone__turn_on()
# my_phone._Phone__serial_number = "44.55.66"
# print( "New serial number is ", my_phone._Phone__serial_number )
# input( "Press Enter to exit" )