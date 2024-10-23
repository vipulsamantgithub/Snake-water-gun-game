# Reason on how the optimised_main.py code is faster than the main.py code:
# Number of Conditions:

The second code uses fewer conditions. You are evaluating two expressions (computer - user == -1) and (computer == 2), which is simpler.
The first block, on the other hand, uses three different sets of and conditions, each with multiple comparisons. This requires more operations for each comparison.

# Short-Circuiting:

In the second code, since you're using or, Python will short-circuit after the first condition evaluates to True. This means if (computer - user) == -1 is True, the second condition computer == 2 will not be checked, making it potentially faster.
In the first block, all comparisons need to be evaluated before deciding the outcome.

# Efficiency of Arithmetic Operation:

The second condition involves simple arithmetic subtraction (computer - user), which is typically faster than checking multiple conditions with and.
