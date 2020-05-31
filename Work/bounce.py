# bounce.py
#
# Exercise 1.5

"""
A rubber ball is dropped from a height of 100 meters
and each time it hits the ground, it bounces back up
to 3/5 the height it fell. Write a program bounce.py
that prints a table showing the height of the first
10 bounces.
"""

init_height = 100.0  # (m)
bounce_limit = 10
debounce_const = 0.6

_current_height = init_height

for i in range(1, bounce_limit + 1):
    _current_height = _current_height * debounce_const
    print(f"{i}\t{round(_current_height, 4)}")
