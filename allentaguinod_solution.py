def studentname(myName, myEmail, myBBUsername) :
    myName = "Taguinod Allen Craig Mariazeta"
    myEmail = "allen@taguinod.net"
    myBBUsername = "775peshf" 
    return myName, myEmail, myBBUsername

def calAverage() :
    number_list = input("Enter integer list separated by space: ")
    integer_sum = sum(map(int,number_list.split(' ')))
    print(integer_sum)
    result = integer_sum / len(number_list.split(' '))
    rounded_result = round(result, 2)
    print('List of integers: {}'.format(number_list))
    print('Average of all integers: {}'.format(rounded_result))

def countCharacter() : 
    all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    all_capletters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    sentence = str(input('Enter sentence: '))
    total_numbers = 0
    total_lowletters = 0
    total_capletters = 0
    total_specialchar = 0
    
    for s in sentence:
        if s in all_letters:
            total_lowletters += 1
        elif s in all_capletters:
            total_capletters += 1
        elif s in all_numbers:
            total_numbers += 1
        else:
            total_specialchar += 1
    total_letters = total_lowletters + total_capletters
    result = [total_letters, total_lowletters, total_capletters, total_numbers, total_specialchar]
    print(result)

def excludeItem() :
    list1 = input("Enter list 1 separated by space: ")
    list2 = input("Enter list 2 separated by space: ") 
    split_list1 = list1.split(' ')
    split_list2 = list2.split(' ')
    list1_as_set = set(split_list1)
    common_items = list1_as_set.intersection(split_list2)
    common_list = list(common_items)
    print(common_list) 

def secondLarge() : 
    string_input = input("Enter integer list separated by space: ")
    number_list = []
    mixed_character = False;
    input_list = string_input.split()
    for a in input_list:
        if str.isdigit(a):
            number_list.append(a)
        else: 
            mixed_character = True;
    
    if mixed_character == True:
        print("-999")   
    else:
        if len(number_list) == 1 :
            print(number_list)
        else:
            list_set = set(number_list)
            unique_list = (list(list_set))
            unique_list.sort()
            print(unique_list[-2])    

def isValidPassword() :
    all_special = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', ';', ':', ',', '<', '.', '>', '?', ' ']
    l, u, d, s = 0, 0, 0, 0
    password = input("Enter password: ") 
    if (len(password) >= 10): 
        for i in password:
            if (i.islower()):
                l+=1
            if (i.isupper()): 
                u+=1
            if (i.isdigit()):
                d+=1 
            if i in all_special:
                s+=1 
    
    if (l>=1 and u>=1 and d>=3 and s>=2) : 
        print(True)
    else: 
        print(False) 