import numpy
import torch
from rain_train import rain_train


rain_values = ["none", "light", "heavy"]
maintenance_values = ["yes", "no"]
train_values = ["on time", "delayed"]
appoinment_values = ["attend", "miss"]


probability = rain_train.probability(
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
)

print(type(probability))
print(probability)