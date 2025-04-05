from KonstantsAPI import *

# Create some constants
PI = create(3.1415)
GRAVITY = create(9.81)

Physics = create_group(PI=PI, GRAVITY=GRAVITY, show_group=False)

PrintG(Physics)
