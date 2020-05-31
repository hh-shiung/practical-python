"""
One morning, you go out and place a dollar bill on the sidewalk
by the Sears tower in Chicago. Each day thereafter, you go out
double the number of bills. How long does it take for the stack
of bills to exceed the height of the tower?
"""

bill_thickness = 0.11 * 0.001  # Thickness (0.11mm)
sears_height = 442  # Height (m)
num_bills = 0
day = 0
current_thickness = 0.0

while current_thickness < sears_height:
    day += 1
    if (num_bills == 0):
        num_bills += 1
    else:
        num_bills *= 2
    current_thickness = num_bills * bill_thickness

    print(
        f"Day: {day} | " +
        f"Bills: {num_bills} | " +
        f"Stack height: {round(current_thickness, 2)} m")
