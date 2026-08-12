import random

# The 10x10 neural matrix
# The value of a fully functional neuron is 1
neurons = [
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10,
    [1]*10
]

fail_probability = 0.15 # Base probability of neuron failure each year
signal_strength = 100 # Signal strength starts at 100

# The similation runs over 5 years
for year in range(1,6):
    print(f"\n\n---------Year {year}---------\n")

    # Random neuron degredation
    row = random.randint(0,9)
    col = random.randint(0,9)
    neurons[col][row] = round(random.uniform(0.05, 0.15), 2)
    neurons[col][row] = max(neurons[col][row], 0)

    print(f"The neuron in (row {row}, column {col}) has failed.\n")
    print(f"Current brain state after random failures is: \n")

    for c in range(10):
        print(neurons[c])

    # Reset the signal position and state
    signal_row = 0
    signal_col = 0
    memory_successful = True

    # Each neuron has a chance to fail based on increasing failure probability
    for col in range(10):
        for row in range(10):
            chance = random.random()
            if chance < fail_probability:
                neurons[col][row] = 0

    # Probability of failure increases by 1% each year
    fail_probability += 0.01
    
    print(f"\n\nThe neuron in (row {row}, column {col}) has failed.")
    print(f"\nCurrent brain state after probability failures is: \n")
    
    for c in range(10
        print(neurons[c])

    # Number of failed neurons is tallied for each year the sim runs
    failed_neurons = 0
    for col in range(10):
        for row in range(10):
            if neurons[col][row] == 0:
                failed_neurons += 1  
    
    print(f"\nThe number of nuerons that have failed is {failed_neurons}")
    
    # The signal moves forward through the neural matrix
    while signal_row < 10:
        if neurons[signal_col][signal_row] == 1:
            
            # The signal weakens as it moves through each neuron
            signal_strength -= (1 - neurons[signal_col][signal_row]) * 5

            # The memory retrieval fails if the signals strength reaches zero
            if signal_strength <= 0:
                print(f"\nSignal strength has reached zero. Memory retrieval failed.")
                memory_successful = False
                break     
            signal_row += 1
            
        else:
            # If path is blocked, attempt rerouting
            switched = False

            # The signal attempts to move sideways to find a functional neuron, if the path forward is blocked
            for new_col in range(10):
                if neurons[new_col][signal_row] == 1:
                    signal_strength -= (1 - neurons[signal_col][signal_row]) * 5
                    signal_col = new_col
                    switched = True
                    print(f"\nThe signal switched to column {new_col} at row {signal_row}")
                    break
            signal_row += 1
                  
            if not switched:
                # The signal attempts to move diagonally to find a functional neuron, if the path forward or sideways is blocked
                new_row = signal_row + 1
                
                if new_row < 10:
                    # Check diagonal left
                    if signal_col - 1 >= 0 and neurons[signal_col - 1][new_row] == 1:
                        signal_strength -= (1 - neurons[signal_col][signal_row]) * 5
                        signal_col -= 1
                        signal_row = new_row
                        switched = True
                        print(f"The signal switched diagonally left to column {signal_col} at row {signal_row}")

                    # Check diagonally right
                    elif signal_col + 1 < 5 and neurons[signal_col + 1][new_row] == 1:
                        signal_strength -= (1 - neurons[signal_col][signal_row]) * 5
                        signal_col += 1
                        signal_row = new_row
                        switched = True
                        print(f"The signal switched diagonally right to column {signal_col} at row {signal_row}")  

                # If the signal cannot reroute, memory retrieval has failed
                if not switched:
                    print(f"\nSignal blocked at row {signal_row}. Memory retrieval failed")
                    memory_successful = False
                    break
                    

    # Final outcome for each year if signal has reached last neuron in any column
    if memory_successful == True:
        print(f"\n------Memory functioning correctly------")