import requests
import json
import math
from tabulate import tabulate
import numpy as np

# Requesting data
race_id = 24071
split_id = 0
print("Requesting race #" + str(race_id))
r = requests.get('https://api2.lowfuelmotorsport.com/api/race/' + str(race_id))
print("Done")
try:
    data = r.json()
except:
    print("No valid data.")
else:
#Writing data to file for later use
    with open('test_race.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.close()

"""
#Use file for data to avoid new request from the API
with open('test_race.json', 'r') as infile:
    data = json.load(infile)
    infile.close()
"""
split_id = 0
k = 6
delta_rating = []
ratings = []
rating_changes = []
expected_result = []
table = []
positions = []

sum_rating_changes = 0
sum_delta_rating = 0

# Get result for first split
result = data["race_results_splits"][split_id]

for driver_result in result["GT3"]["OVERALL"]:
    ratings.append(driver_result["rating"])
    rating_changes.append(driver_result["ratingGain"])
    expected_result.append(0)


print("Using K factor: " + str(k))
for i in range(len(ratings)):
    positions.append(i + 1)
    for j in range(len(ratings)):
        if i != j:    
            expected_result[i] += 1.0 - 1.0 / (1.0 + 10.0 ** ((float(ratings[i]) - float(ratings[j])) / 400.0) )
    delta_rating.append(math.ceil(k * (len(ratings) - i - 1 - expected_result[i])))
    sum_rating_changes += rating_changes[i]
    sum_delta_rating += delta_rating[i]

sum_rating_changes = np.sum(rating_changes)
sum_delta_rating = np.sum(delta_rating)

# Making sure that the total Elo rating change among the drivers is zero
while sum_delta_rating != 0:
    if sum_delta_rating > 0:
        for i in range(len(ratings) - 1, 2, -1):
            sum_delta_rating -= 1
            delta_rating[i] -= 1
            if sum_delta_rating == 0:
                break
    elif sum_delta_rating < 0:
        for i in range(0, len(ratings) - 3):
            sum_delta_rating += 1
            delta_rating[i] += 1
            if sum_delta_rating == 0:
                break

print("Results:")
print(tabulate({"Position": positions, "Rating": ratings, "Current LMF Rating Change": rating_changes, "Proposed Rating Change": delta_rating} , headers="keys", tablefmt="github"))
