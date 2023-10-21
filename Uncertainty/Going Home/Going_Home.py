from pomegranate.distributions import Categorical, ConditionalCategorical
from pomegranate.bayesian_network import BayesianNetwork

week = Categorical(
    [
        [0.5, 0.5]
    ]
)

mood = ConditionalCategorical(
    [
        [
            [0.3, 0.5, 0.2],
            [0.4, 0.3, 0.3]
        ]
    ]
)

reason = ConditionalCategorical(
    [
        [
            [0.4, 0.4, 0.2],
            [0.1, 0.3, 0.6]
        ]
    ]
)

permission = ConditionalCategorical(
    [
        [
            [0.9, 0.1],
            [0.8, 0.2],
            [0.5, 0.5]
        ]
    ]
)

final_decision = ConditionalCategorical(
    [
        [
            [
                [0.9, 0.1],
                [0.1, 0.9],
            ],
            [
                [0.8, 0.2],
                [0.3, 0.7]
            ],
            [
                [0.6, 0.4],
                [0.4, 0.6]
            ]
        ]
    ]
)

# Lets Create an Bayesian Network of these Nodes
Going_Home = BayesianNetwork()
Going_Home.add_distributions([week, mood, reason, permission, final_decision])

# Now Add Edge to it
Going_Home.add_edges([(week, mood), (week, reason), (permission, final_decision), (reason, permission), (mood, final_decision)])