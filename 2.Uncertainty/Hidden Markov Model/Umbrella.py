from pomegranate.hmm import *
from pomegranate.distributions import *
import numpy

# Observation model for each state
sun = Categorical(
    [
        [
            0.2, # Brings Umbrella on sunny day
            0.8  # Not Brings Umbrella on sunny day
        ]
    ]
)
rain = Categorical(
    [
        [
            0.9, # Brings Umbrella on rainy day
            0.1  # Not Brings Umbrella on rainy day
        ]
    ]
)
states = [sun, rain]

# Create the model
model = DenseHMM()
model.add_distributions(states)

# Starting probability: That the probability of first day to raining or sunny
model.add_edge(model.start, rain, 0.5)
model.add_edge(model.start, sun, 0.5)

# Transitional Model
model.add_edge(sun, sun, 0.9)  # If today is sunny day then probability of tommorow will be sunny
model.add_edge(sun, rain, 0.1) # If today is sunny day then probability of tommorow will be not sunny i.e. Rainny
model.add_edge(rain, rain, 0.3) # If today is raining then probability of tommorow will be raining too
model.add_edge(rain, sun, 0.7) # If today is raining then probability of tommorow will be not raining
