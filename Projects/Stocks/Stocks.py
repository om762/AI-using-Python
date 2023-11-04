from pomegranate.distributions import *
from pomegranate.hmm import *
from numpy import array

# Observation of market based on bullish or bearish

market_up = Categorical(
    [
        [
            0.75, # Prob of market will up if its bullish
            0.25  # Prob of market will up if its bearish 
        ]
    ]
)

market_down = Categorical(
    [
        [
            0.2, # Prob of market will down if its bullish
            0.8  # Prob of market will down if its bearish
        ]
    ]
)

states = [market_up, market_down]

# Create the model
model = DenseHMM()
model.add_distributions(states)

# Starting probability: That the probability of first day to market up or market down
model.add_edge(model.start, market_up, 0.6)
model.add_edge(model.start, market_down, 0.4)

# Transitional Model
model.add_edge(market_up, market_up, 0.9)  # If today's market is up then probability of tommorow market will up
model.add_edge(market_up, market_down, 0.1) # If today's market is up then probability of tommorow will be go down
model.add_edge(market_down, market_down, 0.1) # If today is market is down then probability of tommorow will be market go down too
model.add_edge(market_down, market_up, 0.9) # If today is market is down then probability of tommorow will not go down i.e. it will go up

# Just play around probability of Transitional Model