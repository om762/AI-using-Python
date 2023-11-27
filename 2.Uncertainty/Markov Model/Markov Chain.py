from pomegranate.markov_chain import *
from torch import tensor

start = Categorical(
    [
        [0.5, 0.5]
    ]
)

transition = ConditionalCategorical(
    [
        [
            [0.8, 0.2],
            [0.3, 0.7]
        ]
    ]
)

model = MarkovChain([start, transition])

chain = model.sample(5)
for i in chain:
    for j in i:
        for k in j:
            if k == tensor([0]):
                print('sunny->', end='')
            else:
                print('rainy->', end='')