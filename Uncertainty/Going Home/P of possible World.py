import torch
from Going_Home import Going_Home

week_values = ['week-off', 'working']
mood_values = ['happy', 'sad', 'just okay']
reason_values = ['important', 'festival', 'moody']
permission_values = ['granted', 'denied']
final_decision_values = ['going', 'stay']

nodes = [week_values, mood_values, reason_values, permission_values, final_decision_values]
# Finding probability for following problem
possible_world = ['week-off', 'happy', 'festival', 'granted', 'going']

baking_data = [[]]

'''probability = rain_train.probability(
    torch.as_tensor(
        [
            [
                rain_values.index("none"),
                maintenance_values.index("no"),
                train_values.index("on time"),
                appoinment_values.index("attend"),
            ]
        ]
    )
)'''

for i in range(len(nodes)) : baking_data[0].append(nodes[i].index(possible_world[i]))

baking_data = torch.as_tensor(baking_data)

probability_of_possible_world = Going_Home.probability(baking_data)
print(probability_of_possible_world)
