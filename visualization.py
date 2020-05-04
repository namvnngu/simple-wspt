import matplotlib.pyplot as plt
import warnings
import numpy as np

table = [
    ["1", 5, 3],
    ["2", 6, 1],
    ["3", 3, 2],
    ["4", 8, 4],
    ["5", 2, 4]
]
# Key - Value: Job ID - W/P
jobs_dict = {}
for row in table:
    jobs_dict[row[0]] = row[2] / row[1]
# print("JobID - WP",jobs_dict)

# One-line solution
sorted_dict = {k: v for k, v in sorted(
    jobs_dict.items(), key=lambda item: item[1], reverse=True)}
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
print("Min CjWj =", min_sum)

# Processing Time
p = [ele[1] for ele in sorted_table]

# Data Preparation
p_gantt = []
temp = 0
temp_gantt = []
for p_ele in p:
    temp += p_ele
    temp_gantt.append(temp)

i = 0
while(i < len(temp_gantt) - 1):
    p_gantt.append((temp_gantt[i], p[i+1]))
    i += 1

p_gantt = [(0, p[0])] + p_gantt
print(p_gantt)

# Draw graph
fig, ax = plt.subplots(figsize=(15, 2))

# Colors
cmap = plt.get_cmap("Paired", len(p_gantt))
colors = [cmap(i) for i in range(len(p_gantt))]

# Labels
labels = [row[0] for row in sorted_table]

# Plot Gantt Graph
ax.broken_barh(p_gantt, (0, 5), facecolors=set(colors))
ax.get_yaxis().set_visible(False)
ax.set_xticks([0] + temp_gantt)
ax.tick_params(axis="x", labelsize=14)

for pair, label in zip(p_gantt, labels):
    ax.text(pair[0] + pair[1] / 2, 2.5,
            label, ha='center',
            va='center',
            color='r',
            fontsize=20)
plt.show(block=True)
