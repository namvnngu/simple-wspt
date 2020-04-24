# List - 2D Array
table = []
records = int(input("The number of works: "))

for i in range(records):
	row = []
	print(f"Job {i+1}")

	job_ID = input("Enter job ID: ")
	row.append(job_ID)

	p = float(input("Enter P: "))
	row.append(p)

	w = float(input("Enter W: "))
	row.append(w)

	table.append(row)
	print("\n")

print("Table:",table)

# Key - Value: Job ID - W/P   
jobs_dict = {}
for row in table:
	jobs_dict[row[0]] = row[2] / row[1]
# print("JobID - WP",jobs_dict)

# One-line solution
sorted_dict = {k: v for k, v in sorted(jobs_dict.items(), key=lambda item: item[1], reverse=True)}
# print("Sorted P/W with one line solution",sorted_dict)

# Multi-line solution
P_W = list(jobs_dict.values())
P_W.sort(reverse=True)
sorted_dict = {}
for pw in P_W:
	for key, value in jobs_dict.items():
		if(pw == value):
			sorted_dict[key] = pw
# print("sorted P/W with on line soulution",sorted_dict)

# Finding row corresponding to JobID
sorted_jobID = list(sorted_dict.keys())
sorted_table = []
for job_id in sorted_jobID:
	for row in table:
		if(job_id == row[0]):
			sorted_table.append(row)
# print(sorted_jobID, sorted_table)

# Min
min_sum = 0
c = 0
for i in range(len(sorted_table)):
	c += sorted_table[i][1]
	w = sorted_table[i][2]
	min_sum += w * c
print ("Min CjWj =", min_sum)