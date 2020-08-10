"""
This is a lloyd-max quantizer for a function with: 
Bins = 3
f(x) = 1
"""

def lloyd_max(N, y1, y2, y3):

    # STEP 1 : INITIALIZATION
    b0, b3 = -0.5, 0.5

    for i in range(N):

        # STEP 2 : Get BOUNDARIES
        b1 = (y2 + y1) / 2
        b2 = (y3 + y2) / 2

        print(f"Iteration {i} :  Y values: {y1}, {y2}, {y3}")

        # STEP 3 : Conditional Expectation
        y1 = ((b1**2 / 2) - (b0**2 / 2)) / (b1 - b0) 
        y2 = ((b2**2 / 2) - (b1**2 / 2)) / (b2 - b1) 
        y3 = ((b3**2 / 2) - (b2**2 / 2)) / (b3 - b2)

    print(f"Y Values final: {y1}, {y2}, {y3}")


if __name__ == "__main__":
    N = int(input("Enter the number of iterations, the N value (ex. 3): "))
    y1 = float(input("Enter the y1 value (ex. -0.5): "))
    y2 = float(input("Enter the y2 value (ex. 0): "))
    y3 = float(input("Enter the y3 value (ex. 0.5): "))

    lloyd_max(N, y1, y2, y3)
