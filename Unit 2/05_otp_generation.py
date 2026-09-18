# Random OTP Generator

import random

n = int(input("Enter the number of digits for OTP (4 or 6): "))

if n == 4 or n == 6:
    otp = random.randint(10 ** (n - 1), (10 ** n) - 1)
    print("Generated OTP:", otp)
else:
    print("Invalid choice. Please enter either 4 or 6.")