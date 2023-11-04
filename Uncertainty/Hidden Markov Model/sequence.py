from Umbrella import model
import numpy as np

sequence = 'UUNUUUUNNUNUNUNUNUNNNNNNNNUUUUUUUNUNUNUNUNUNUNUNUNUNUN' 
X = np.array(
    [
        [
            [['U', 'N'].index(char)] for char in sequence
        ]
    ])

y_hat = model.predict(X)

print("sequence: {}".format(''.join(sequence)))
print("hmm pred: {}".format(''.join([str(y.item()) for y in y_hat[0]])))