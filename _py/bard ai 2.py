def train_network(network, data):
  for example in data:
    prediction = network.predict(example[0])
    loss = calculate_loss(prediction, example[1])
    network.update(example[0], example[1], loss)

def calculate_loss(prediction, target):
  return np.mean((prediction - target)**2)
