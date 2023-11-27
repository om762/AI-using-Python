import torch
from Going_Home import Going_Home

X = torch.tensor(
    [
        [
            -1,
            -1,
            -1,
            -1,
            1  # Anyhow final Decision is going
        ]
    ]
)

X_masked = torch.masked.MaskedTensor(X, mask=(X != -1))

states = (
    ('week', ['week-off', 'working']),
    ('mood', ['happy', 'sad', 'just okay']),
    ('reason', ['important', 'festival', 'moody']),
    ('permission', ['granted', 'denied']),
    ('final_decision', ['going', 'stay'])
)

# Calculate probability of final decision is going
predictions = Going_Home.predict_proba(X_masked)

# Print prediction for each node

for (node_name, values), prediction in zip(states, predictions):
    if isinstance(prediction, str):
        print(f"{node_name}: {prediction}")
    else:
        print(f"{node_name}")
        for value, probability in zip(values, prediction[0]):
            print(f"    {value}: {probability:.4f}")