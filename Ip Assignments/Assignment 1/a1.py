
#here the dictonary with list in it
d =  {
	  0:["Tshirts","Apparels",500],
      1:["Trousers","Apparels",600],
      2:["Scarf","Apparels",250],
      3:["Smartphone","Electronics",20000],
      4:["iPad","Electronics",30000],
	  5:["Laptop", "Electronics", 50000],
	  6:["Eggs", "Eatables", 5],
	  7:["Chocolate", "Eatables", 10],
      8:["Juice", "Eatables", 100],
	  9:["Milk", "Eatables", 45],
}
# now we convert from dictionary to list for regular or bulk inputs
def covert_d_to_List(order_d):
    order_list=[0]*10
    for i in order_d:
        order_list[i]+=sum(order_d[i])
    return order_list
def show_menu():
	print("""
=================================================
                   MY BAZAAR
=================================================
Hello! Welcome to my grocery store!
Following are the products available in the shop:

-------------------------------------------------
CODE | DESCRIPTION |   CATEGORY   | COST (Rs)
-------------------------------------------------
  0  | Tshirt      | Apparels     | 500
  1  | Trousers    | Apparels     | 600
  2  | Scarf       | Apparels     | 250
  3  | Smartphone  | Electronics  | 20,000
  4  | iPad        | Electronics  | 30,000
  5  | Laptop      | Electronics  | 50,000
  6  | Eggs        | Eatables     | 5
  7  | Chocolate   | Eatables     | 10
  8  | Juice       | Eatables     | 100
  9  | Milk        | Eatables     | 45
------------------------------------------------

Would you like to buy in bulk? (y or Y / n or N):
	
	
	
	
	
	
	     """)


def get_regular_input():
    se = list(map(int, input("enter the items").split(" ")))
    it = []
    for i in se:
        it.append(i)
    order_d={}
	#we are making dict
    for i in it:
        if i not in order_d:
            order_d[i]=[1]
        else:
            order_d[i].append(1)
    return order_d



def get_bulk_input():
	order_d={}
	while True:
		#we have used this tuple for getting bulk input again and again
		#until blank is entered
		x = tuple(input("enter the code and quantity or leave a blank to stop").split())
		if (len(x)==0):
			print("Your order has been finalised")
			break
		elif (len(x)==2):
			dcode = int(x[0])
			dqty = int(x[1])
			if (int(x[0]) not in d):
				print("Invalid Code")
				continue
			if (int(x[1]) <= 0):
				print("Invalid Code")
				continue
			item = d[int(x[0])]
			#d is dictionary that declared in global
			# here items as values as 0,0 from dictionary like that
			print("You have added",x[1]," ",item[0])

			if dcode in order_d:
				order_d[dcode].append(dqty)
			else:
				order_d[dcode]= [dqty]
	return order_d





def print_order_details(order_d):

	sno = 1
	for i in order_d:
		print(sno,d[i][0],"x", sum(order_d[i]),"=",d[i][2],"*",sum(order_d[i]),"= Rs",sum(order_d[i]) * d[i][2])

		sno+=1




def category_wise_cost(ol):
    s1,s2,s3=0,0,0
	#here we have we got input from regular or bulk after converting
	# to list here it will check wheather it will belong to
	# apparels, electronics or eatables
    for i in range(len(ol)):
        if d[i][1]=="Apparels":
            s1=s1+ol[i]*d[i][2]
        elif d[i][1]=="Electronics":
            s2+=ol[i]*d[i][2]
        elif d[i][1]=="Eatables":
            s3+=ol[i]*d[i][2]
    t=(s1,s2,s3)
	#now we have converted to tuple
    print("Apparels = ",t[0])
    print("Electronics = ",t[1])
    print("Eatables = ",t[2])
    return t



def get_discount(cost, discount_rate):

	return int(cost * discount)


def calculated_discounted_price(t):
	dis1, dis2, dis3 = 0, 0, 0
	if t[0] >= 2000:
		dis1 = t[0] * .10
	if t[1] >= 25000:
		dis2 = t[1] * .10
	if t[2] >= 500:
		dis3 = t[2] * .10
	t1 = (dis1, dis2, dis3)

	print("[Apparels] Rs ", t[0], " - Rs ", t1[0], "= Rs ", (t[0] - t1[0]))
	print("[Electronics] Rs ", t[1], " - Rs ", t1[1], "= Rs ", (t[1] - t1[1]))
	print("[Eatables] Rs ", t[2], " - Rs ", t1[2], "= Rs ", (t[2] - t1[2]))
	return t1


def get_tax(cost, tax):

	return int(cost * tax)


def calculate_tax(ol):
	s1, s2, s3 = 0, 0, 0
	for i in range(len(ol)):
		if d[i][1] == "Apparels":
			s1 = s1 + ol[i] * d[i][2]
		elif d[i][1] == "Electronics":
			s2 += ol[i] * d[i][2]
		elif d[i][1] == "Eatables":
			s3 += ol[i] * d[i][2]
	t = (s1, s2, s3)
	print("Apparels tax is =",t[0] *0.10)
	print("Electronics tax is =",t[1] *0.15)
	print("Eastable tax is =",t[2] *0.05)
	print("Total tax is =",t[0] *0.10+t[1] *0.15+t[2] *0.05)
	print("Total Cost =",t[0]+t[1]+t[2])








def apply_coupon_code(ol):
	s1, s2, s3 = 0, 0, 0
	for i in range(len(ol)):
		if d[i][1] == "Apparels":
			s1 = s1 + ol[i] * d[i][2]
		elif d[i][1] == "Electronics":
			s2 += ol[i] * d[i][2]
		elif d[i][1] == "Eatables":
			s3 += ol[i] * d[i][2]
	t = (s1, s2, s3)
	lt = t[0]+t[1]+t[2] + t[0] *0.10+t[1] *0.15+t[2] *0.05
	ost = input("Enter the coupon code")
	while True:
		ost = input("Enter the coupon code")

		if ost=='HELLE25':
			if lt>= 25000:
				print("Your Discounted price is = ",lt * 0.25)
				print("Your Cost Now is = ",lt - (lt - 0.25))
				break
		elif ost=='CHILL50':
			if lt>=50000:
				print("Your Discounted price is = ", lt * 0.50)
				print("Your Cost Now is = ", lt - (lt - 0.50))
				break
		else:
			print("Invalid Code")
			break



def main():
	show_menu()
	while True:
		l = input("enter the y/n for bulk  or press space to stop")
		#for asking again and again until user inputs in a correct way
		if l =='y' or l =='Y':
			o = get_bulk_input()
			# here t represents that it has all inputs of bulk output
			# this is done because so that the user don't have to input again and again
			print_order_details(o)
			ol2 = covert_d_to_List(o)
			#this is done so that we can get in a list way
			category_wise_cost(ol2)
			calculated_discounted_price(ol2)
			calculate_tax(ol2)
			apply_coupon_code(ol2)

		elif l=='n' or l =='N':
			t = get_regular_input()
			#here t represents that it has all inputs of regular output
			#this is done because so that the user don't have to input again and again
			print_order_details(t)
			ol1 = covert_d_to_List(t)
			#this is done so that we can get in a list way
			category_wise_cost(ol1)
			calculated_discounted_price(ol1)
			calculate_tax(ol1)
			apply_coupon_code(ol1)
		elif l==" ":
			break


	else:
		print("not a valid output")


if __name__ == '__main__':
	main()
