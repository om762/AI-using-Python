from Stocks import model
from numpy import array

# Observation Data
# Assuming a hypothetical daily price change data (increased from 20 to 30 days)
price_changes = [0.5, 0.8, -0.3, -0.6, 0.4, 0.3, -0.5, 0.7, -0.2, -0.1, 0.6, 0.2, -0.4, -0.2, 0.5, 0.1, 0.6, -0.3, -0.7, 0.5, 0.2, -0.4, 0.3, 0.9, -0.5, -0.1, 0.7, -0.3, 0.6, 0.4]

movement_sequence = []

for change in price_changes:
    if change >= 0:
        movement_sequence.append('bullish')
    else:
        movement_sequence.append('bearish')

# movement_sequence = str(movement_sequence)
# movement_sequence = movement_sequence.replace('[', '')
# movement_sequence = movement_sequence.replace(']', '')
# movement_sequence = movement_sequence.replace(', ', ',\n')
# count = movement_sequence.count('bullish') + movement_sequence.count('bearish')
print(movement_sequence)
# # print(count)

X = array(
    [
        [
            [['bullish', 'bearish'].index(char)] for char in movement_sequence
        ]
    ]
)

# print(X)
y_hat = model.predict(X)

print(y_hat)