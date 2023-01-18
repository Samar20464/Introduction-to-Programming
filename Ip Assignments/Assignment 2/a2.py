# Assignment - 2
# Name -  Samar Preet
# Roll No - 2020464

import json





def read_data_from_file(file_path="data.json"):
	with open(file_path, 'r') as data:
		records = json.load(data)

	return records


def filter_by_first_name(records, first_name):
	id_list = []
	for i in range(len(records)):
		try:
			if records[i]["first_name"].lower()==first_name.lower():
				id_list.append(records[i]["id"])
		except:
			pass
	return id_list


def filter_by_last_name(records,last_name):

	id_list = []
	for i in range(len(records)):
		try:
			if records[i]["last_name"].lower() == last_name.lower():
				id_list.append(records[i]["id"])
		except:
			pass
	return id_list


def filter_by_full_name(records, full_name):

	id_list = []
	for i in range(len(records)):
		try:
			ith_full_name = records[i]["first_name"] + " " + records[i]["last_name"]
			if ith_full_name.lower()==full_name.lower():
				id_list.append(records[i]["id"])
		except:
			pass
	return id_list


def filter_by_age_range(records, min_age, max_age):

	id_list = []
	for i in range(len(records)):
		try:
			ith_age = records[i]["age"]
			if ith_age <=max_age and ith_age>=min_age:
				id_list.append(i)
		except:
			pass
	return id_list



def count_by_gender(records):

	gend_count = {"male":0,"female":0}
	for i in range(len(records)):
		try:
			if records[i]['gender'] == "male":
				gend_count["male"]+=1
			else:
				gend_count["female"]+=1
		except:
			pass
	return gend_count


def filter_by_address(records, address):
	add_list = []
	if (len(address)==0):
		for i in range(len(records)):
			add_list.append({"first_name": records[i]['first_name'], "last_name":records[i]['last_name']})
	else:
		key_list = list(address)
		for i in range(len(key_list)):
			if(len(str(address[key_list[i]]))) == 0:
				del (address[key_list[i]])
		key_list = list(address)
		for i in range(len(records)):
			for j in key_list:
				if records[i]['address'][j] ==address[j]:
					pass
				else:
					break
				if j == key_list[-1]:
					add_list.append({"first_name": records[i]['first_name'], "last_name": records[i]['last_name']})
	return add_list

def find_alumni(records, institute_name):
	alum_list = []
	for i in range(len(records)):
		try:
			for j in range(len(records[i]["education"])):
				if records[i]["education"][j]['institute'].lower() == institute_name.lower()  and  records[i]['education'][j]['ongoing'] == False:
					alum_list.append({'first_name':records[i]['first_name'], 'last_name': records[i]['last_name'],'percentage':records[i][j]['percentage']})
		except:
			pass
	return alum_list


def find_topper_of_each_institute(records):
	topper_dict = {}
	inst_list = {}
	for i in range(len(records)):
		for j in range(len(records[i]['education'])):
			inst_list.append(records[i]['education'][j]['institute'])
	inst_list_new = list(set(inst_list))
	for i in inst_list_new:
		best_percent = 0
		best_id = 0
		for j in range(len(records)):
			for k in range(len(records[j]['education'])):
				if records[j]['education'][k]['percentage'] >=best_percent:
					best_percent = records[j]['education'][k]['percentage']
					best_id = j
		topper_dict[i] =best_id
	return topper_dict


def find_blood_donors(records, receiver_person_id):
	doner_list = []
	receiver_blood_group = records[receiver_person_id]['blood_group']
	if receiver_blood_group == 'A':
		for i in range(len(records)):
			try:
				if records[i]['blood_group'] =="A" or records[i]['blood_group'] == 0:
					doner_list.append({i: records[i]['contacts']})
			except:
				pass
	elif receiver_blood_group == 'B':
		for i in range(len(records)):
			try:
				if records[i]['blood_group'] =="B" or records[i]['blood_group'] == 0:
					doner_list.append({i: records[i]['contacts']})
			except:
				pass
	elif receiver_blood_group == 'AB':
		for i in range(len(records)):
			try:
				if records[i]['blood_group'] == "A" or records[i]['blood_group'] == "B" or records[i]['blood_group'] == "AB" or records[i]['blood_group'] == "O":
					doner_list.append({i: records[i]['contacts']})
			except:
				pass
	else:
		for i in range(len(records)):
			try:
				if records[i]['blood_doner'] == 0:
					doner_list.append({i:records[i]['contacts']})
			except:
				pass





def get_common_friends(records, list_of_ids):
	id_list = []
	for i in range(len(records)):
		try:
			for j in range(len(list_of_ids)):
				if list_of_ids[j] in records[i]['friend_ids']:
					pass
				else:
					break
				if j == len(list_of_ids) -1:
					id_list.append(j)
		except:
			pass
	return id_list




def is_related(records, person_id_1, person_id_2):
	return person_id_2 in records[person_id_1]['friend_ids']


def delete_by_id(records, person_id):
	del (records[person_id])
	for i in range(200):
		try:
			if person_id in records[i]['friends_id']:
				records[i]['friends_id'].remove(person_id)
		except:
			pass
	return records


def add_friend(records, person_id, friend_id):
	records[person_id]['friend_ids'].append(friend_id)
	records[person_id]['friend_ids'].sort()
	records[person_id]['friend_ids'].append(person_id)
	records[person_id]['friend_ids'].sort()





def remove_friend(records, person_id, friend_id):
	records[person_id]['friend_ids'].remove(person_id)
	records[person_id]['friend_ids'].remove(friend_id)




def add_education(records, person_id, institute_name, ongoing, percentage):
	if ongoing == False:
		records[person_id]['education'].append({'institute':institute_name,'ongoing':ongoing,'percentage':percentage})
	else:
		records[person_id]['education'].append({'institute':institute_name,'ongoing':ongoing})
	return records


