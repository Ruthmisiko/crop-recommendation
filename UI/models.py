import numpy as np

# Define characteristics
characteristics = {
    'temperature': {'mean': 25.616243851779544, 'std': 5.063748599958843, 'min': 8.825674745, 'max': 43.67549305},
    'humidity': {'mean': 71.48177921778637, 'std': 22.263811589761083, 'min': 14.25803981, 'max': 99.98187601},
    'rainfall': {'mean': 103.46365541576817, 'std': 54.95838852487813, 'min': 20.21126747, 'max': 298.5601175}
}

# Generate random numbers
def generate_number(feature):
    mean = characteristics[feature]['mean']
    std = characteristics[feature]['std']
    min_val = characteristics[feature]['min']
    max_val = characteristics[feature]['max']
    
    # Generate random number within 3 standard deviations to ensure it's within a reasonable range
    while True:
        num = np.random.normal(mean, std)
        if min_val <= num <= max_val:
            return num

# Function to generate a set of random numbers
def generate(input_data):
    random_data = {}
    for feature in characteristics:
        random_data[feature] = generate_number(feature)

    return  np.array(list(random_data.values()))

# Example usage:
input_data = [23, 4, 6]
random_sample = generate(input_data)
print(random_sample)