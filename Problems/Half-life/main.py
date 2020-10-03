initial_atoms = int(input())
final_atoms = int(input())
half_life_counter = 0
while initial_atoms > final_atoms:
    initial_atoms /= 2
    half_life_counter += 1
print(half_life_counter * 12)