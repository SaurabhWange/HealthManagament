harry = 1
rohan = 2
exercise = "E"
Diet = "D"
print( "Would u like to insert or retrive data" )
arg= input( )
print("Enter the client Id")
client_id = int(input())
print("what would u like to lock exercise 'E' or diet 'D' ")
Requirement = input()

def getDate():

            import datetime
            return datetime.datetime.now()

def Health_Management():

            print("Enter the data you want to insert ")
            Data_to_insert = input()
            if client_id == 1 and Requirement == "D":
                with open( "Harry_diet.txt" , "a") as op:
                    op.write( str( getDate() ) + Data_to_insert+ "\n")
                print("Data Inserted Successfully")

            elif client_id == 1 and Requirement == "E" :
                with open( "Harry_exr.txt" , "a" )as ex:
                    ex.write( str( getDate() ) + Data_to_insert+ "\n" )
                    print("Data Inserted Successfully")

            elif client_id == 2 and Requirement == "D":
                with open( "Rohan_diet.txt" , "a" )as Rd:
                    Rd.write( str( getDate() ) + Data_to_insert+ "\n" )
                    print("Data Inserted Successfully")

            elif client_id == 2 and Requirement == "E" :
                with open( "Rohan_exr.txt" , "a" )as Re:
                    Re.write( str( getDate() ) + Data_to_insert+ "\n" )
                    print( "Data Inserted Successfully" )

def Retrieve_Data():

        if client_id == 1 and Requirement == "D" :
            with open( "Harry_diet.txt" )as Hd:
                for data in Hd :
                    print( data , end="" )
            print( "Data Retrived Successfully" )

        elif client_id == 1 and Requirement == 'E':
            with open( "Harry_exr.txt" ) as He:
                for i in He:
                    print( i , end="")
            print("Data Retrived Successfully")

        elif client_id == 2 and Requirement== "D":
            with open( "Rohan_diet.txt" )as Rd:
                for i  in Rd:
                    print( i , end="")
            print("Data Retrived Successfully")

        elif client_id == 2 and Requirement== "E":
            with open( "Rohan_exr.txt" ) as Re:
                for i  in Re:
                    print( i , end="" )
            print("Data Retrived Successfully")


if arg == "insert":
    Health_Management()
elif arg == "retrive":
    Retrieve_Data()
else:
    print( "Please Enter Valid Data" )