# Name - Samar
# Roll No - 2020464



# Write the code here for creating an interactive program.
import a2

def show_menu():
    print("-"*108)
    print("| CODE| DESCRIPTION|")
    print("-"*108)
    l = ["read_data_from_file", "filter_by_first_name", "filter_by_last_name",
         "filter_by_full_name", "filter_by_age_range", "count_by_gender",
         "filter_by_address", "find_alumni", "find_topper_of_each_institute",
         "find_blood_donors", "get_common_friends", "is_related",
         "delete_by_id", "add_friend", "remove_friend", "add_education"]

    print("""
    
    
    Enter what do you to insert:
          1. read_data_from_file
          2. filter_by_first_name
          3. filter_by_last_name
          4. filter_by_full_name
          5. filter_by_age_range
          6. count_by_gender
          7. find_blood_doners
          8. get_common_friend
          9. is_related
          10. delete_by_id
          11. add_friend
          12. remove_friend
          13. add_education
    
    
    """)

def collect_address():
    address = {}
    house_no = input("Enter the house no (or leave a blank to skip)")
    if house_no:
        house_no = int(house_no)
        block = input("Enter the block")
        town = input(" Enter the town")
        city = input("Enter the City")
        state = input("Enter the state")
        pincode = input(" Enter the pincode")
        if pincode:
            pincode = int(pincode)
            address['house_no'] = house_no
            address['block'] = block
            address['town'] = town
            address['city'] = city
            address['state'] = state
            address['pincode'] = pincode
    return  address

records = a2.read_data_from_file("data.json")
show_menu()
while True:
     choices = int(input("Enter the choices or -1 to exit"))
     if choices == -1:
         break
     else:
         if choices== 1:
             records =a2.read_data_from_file(input("Enter the json file path"))
         elif choices==2:
             print(a2.filter_by_first_name(records, input(" Enter the first name: ")))
         elif choices==3:
             print(a2.filter_by_last_name(records, input(" Enter the last name: ")))
         elif choices==4:
             print(a2.filter_by_full_name(records, input(" Enter the full name(Space Seperated String): ")))
         elif choices==5:
             print(a2.filter_by_age_range(records, int(input("Enter the minimum age: ")),int(input("Enter the maximum age: "))))
         elif choices==6:
             print(a2.count_by_gender(records))
         elif choices==7:
             address = collect_address()
             print(a2.filter_by_address(records,address))
         elif choices==8:
             print(a2.find_alumni(records, input("Enter Institute Name: ")))
         elif choices==9:
             print(a2.find_topper_of_each_institute(records))
         elif choices==10:
             print(a2.find_blood_donors(records, input("Enter the id of the reciever: ")))
         elif choices==11:
             print(a2.get_common_friends(records, list(map(int, input("Enter space seperated values of friend list: ")))))
         elif choices==12:
             print(a2.is_related(records,int(input("Enter the first person id"))),int(input("Enter the second person id")))
         elif choices ==13:
             records = a2.delete_by_id(records,int(input("Enter the id of person to be deleted")))
             print("Successfully deleted")
         elif choices==14:
             records = a2.add_friend(records, int(input("1st id: ")), int(input("2nd id: ")))
             print("Now they will marry each other")

         elif choices == 15:
             records = a2.remove_friend(records, int(input("Person Id: ")), int(input("Friend id: ")))
             print("Removed sucessfully")
         elif choices ==0:
             percentage = 0
             person_id = int(input("Add the id of person"))
             institute_name = int(input("Enter the institute name"))
             ongoing = input("Enter TRUE or FALSE for ongoing institute")
             if ongoing == True:
                 pass
             else:
                 percentage = float(input("Enter the percentage"))
             records = a2.add_education(records,person_id,institute_name,ongoing,percentage)














