from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork

rain = Categorical(
    [
        [0.7, 0.2, 0.1],
    ]
)

maintenance = ConditionalCategorical(
    [
        [
            [0.4, 0.6],
            [0.2, 0.8],
            [0.1, 0.9],
        ],
    ]
)

train = ConditionalCategorical(
    [
        [
            [
                [0.8, 0.2],
                [0.9, 0.1],
            ],
            [
                [0.6, 0.4],
                [0.7, 0.3],
            ],
            [
                [0.4, 0.6],
                [0.5, 0.5],
            ],
        ]
    ]
)


appointment = ConditionalCategorical(
    [
        [
            [0.9, 0.1],
            [0.6, 0.4],
        ],
    ]
)


# Create a Bayesian Network and add states
rain_train = BayesianNetwork()
rain_train.add_distributions([rain, maintenance, train, appointment])

# Add edges connecting nodes
rain_train.add_edge(rain, maintenance)
rain_train.add_edge(rain, train)
rain_train.add_edge(maintenance, train)
rain_train.add_edge(train, appointment)