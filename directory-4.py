from database import Simpledb

def commandUser():
    print()
    command= input("To add a name and number to the directory; press the key 'a' \nTo find a name in the directory; press the key 'f' \nTo delete a name and number from the directory; press the key 'd' \nTo update a number in the directory; press the key 'u' \nTo quit the program; press the key 'q': ")
    print()
    command= command.lower()
    #print (command)

    return command

while True:
    command = commandUser()
    c= str(command)

    
    if (c == 'a'):
        key = input("Enter a name: ")
        key= key.lower()
        value = input("Enter the phone number(only enter digits): ")
        value = int(value)
        Simpledb.add("data.txt",key,value)
    

    elif (c =='f'):
        key = input("Enter the name you would like to search for: ")
        key= key.lower()
        Simpledb.find("data.txt", key)
    

    elif (c == 'd'):
        key = input("Enter the name you would like to delete: ")
        key= key.lower()
        Simpledb.delete("data.txt", key)
    

    elif (c == 'u'):
        key = input("Enter the name you would like to search for: ")
        key= key.lower()
        Simpledb.update("data.txt", key)
    
    elif (c == 'q'):
       break

    else:
        print ("Please enter a valid option.")

    

