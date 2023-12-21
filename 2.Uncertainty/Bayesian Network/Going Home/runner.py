import torch
from Going_Home import Going_Home

X = torch.masked.MaskedTensor(torch.tensor([-1, -1, -1, -1, 1]), mask=(torch.tensor([-1, -1, -1, -1, 1]) != -1))

states = (
    ('week', ['week-off', 'working']),
    ('mood', ['happy', 'sad', 'just okay']),
    ('reason', ['important', 'festival', 'moody']),
    ('permission', ['granted', 'denied']),
    ('final_decision', ['going', 'stay'])
)

# Calculate probabitlity of final decision is going
predictions = Going_Home.predict_proba(X)

# Print prediction for each node

for (node_name, values), prediction in zip(states, predictions):
    if isinstance(prediction, str):
        print(f"{node_name} : {prediction}")
    else:
        print(f"{node_name}")
        for value, probability in zip(values, prediction[0]):
            print(f"   {value}: {probability:.4f}")
