import numpy as np
import tensorflow as tf

def attack_simulation(building, troops):
    wall_health = building["health"]
    attacks = np.array([troop["attack"] for troop in troops])
    num_troops = len(troops)
    time_spent = 0

    while wall_health > 0 and num_troops > 0:
        total_attack = np.sum(attacks)
        wall_health -= total_attack
        time_spent += 1
        num_troops = np.sum(wall_health > 0)

    return time_spent


def generate_training_data(num_simulations=10000):
    # Simulate and generate training data
    # Assuming you have some ranges for building and troop features
    building_healths = np.random.randint(50, 300, size=num_simulations)
    troop_attacks = np.random.randint(10, 50, size=num_simulations)
    train_features = np.column_stack((building_healths, troop_attacks))

    # Simulate attack times using your attack_simulation function
    train_labels = []
    for i in range(num_simulations):
        time_spent = attack_simulation({"health": building_healths[i]}, [{"attack": troop_attacks[i]}])
        train_labels.append(time_spent)

    train_labels = np.array(train_labels)

    return train_features, train_labels

# Sample data for demonstration
train_features, train_labels = generate_training_data()

# Build the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(2,)),  # Input shape (2,) for building and troop features
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Output is the predicted attack time
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(train_features, train_labels, epochs=100, batch_size=32)

# Now you can use the trained model to predict attack times for different troops and buildings
def predict_attack_time(building, troop):
    # Convert building and troop data into a format suitable for the model
    input_data = np.array([[building["health"], troop["attack"]]])  # Combine building and troop data into a single input array
    attack_time = model.predict(input_data)[0][0]
    return attack_time