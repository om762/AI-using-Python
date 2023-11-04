from Umbrella import model
import numpy as np

# Observation Data
observation = [
    "umbrella",
    "umbrella",
    "no umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "umbrella",
    "no umbrella",
    "no umbrella"
]

X = np.array(
    [
        [
            [["umbrella", "no umbrella"].index(char)] for char in observation
        ]
    ]
)

print(X)
y_hat = model.predict(X)

print("sequence: {}".format(''.join(observation)))
print("hmm pred: {}".format(''.join([str(y.item()) for y in y_hat[0]])))