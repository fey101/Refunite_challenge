import csv
import collections


def get_avg_town(town_input):
	assert type(town_input) is list
	males,females = [], []
	for values in town_input:
		if values[1] =="1-Female":
			females.append(int(values[2]))
		elif values[1] =="1-Male":
			males.append(int(values[2]))
			
	total_females = len(females)
	total_males = len (males)
	if total_females > 0:
		avg_female = sum (females)/total_females
	elif total_females == 0:
		avg_female = 0
	if total_males > 0:
		avg_male = sum (males)/total_males
	elif total_males == 0:
		avg_male = 0
		
	max_age = max(avg_male,avg_female)	
	return (max_age,values[0])
	
if __name__ == '__main__':
	with open('ebola_data_public.csv','r') as filename:
		filereader = csv.reader(filename)
		req_fields =[]
		towns=[] 
		for record in filereader:
			town = record [2]
			gender = record [6] 
			age = record[7]
			req_fields.append((town,gender,age))
			towns.append(town)
	
		#print '{}, {}, {}'.format(town, gender, age)
		sorted_codes = sorted(towns)
		sorted_towns = sorted(req_fields)
		frequency_per_town = collections.Counter(towns)
		sorted_frequency,max_town_avg = [], []
		x=0
		for key in sorted(frequency_per_town):
			sorted_frequency.append((key,frequency_per_town[key]))
			town_freq =frequency_per_town[key] 
			town_values = sorted_towns[x:(x+town_freq)]
			#print town_values
			max_town_avg.append(get_avg_town(town_values))
			x += town_freq

		   
		avg_age,town_code = max(max_town_avg)
		answer = town_code + str(avg_age)
		print answer


 
