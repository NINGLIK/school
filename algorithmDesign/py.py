import numpy as np

# Assume this is your cost matrix (fill with your actual data)
cost_matrix = np.array([
    [30, 45, 48, 10, 35],
    [25, 60, 70, 35, 50],
    [28, 15, 25, 32, 10],
    [45, 30, 20, 24, 12],
    [58, 12, 25, 60, 30],
    [65, 30, 15, 57, 33]
])

# Facility locations
facility_locations = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']

# Desired number of facilities to select
num_facilities = 3

# Initialize all facilities as selected
selected_facilities = set(range(len(facility_locations)))

def total_cost(selected_indices, matrix):
    # Calculate the total cost for the selected facilities
    return sum(min(matrix[i][j] for i in selected_indices) for j in range(matrix.shape[1]))

# Greedy heuristic algorithm
while len(selected_facilities) > num_facilities:
    # Find the facility whose removal results in the smallest increase in total cost
    facility_to_remove = min(selected_facilities, key=lambda x: total_cost(selected_facilities - {x}, cost_matrix) - total_cost(selected_facilities, cost_matrix))
    selected_facilities.remove(facility_to_remove)

# Convert indices back to facility names
selected_facility_names = [facility_locations[i] for i in selected_facilities]
final_cost = total_cost(selected_facilities, cost_matrix)

print(f"Selected facilities: {selected_facility_names}")
print(f"Total cost: {final_cost}")
