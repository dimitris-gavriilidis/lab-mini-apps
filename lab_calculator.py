# lab_calculator.py

def add_numbers():
    print("🔹 Welcome to the Mini Lab Calculator 🔹")

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        c = float(input("Enter third number: "))

        result = a + b + c
        print(f"\n✅ The total is: {result}")

    except ValueError:
        print("⚠️ Please enter valid numbers!")

if __name__ == "__main__":
    add_numbers()
