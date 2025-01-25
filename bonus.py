def foo(temperature):
    if temperature > 25:
        return "Hot"
    elif 15 <= temperature <= 25:
        return "Warm"
    elif temperature < 15:
        return "Cold"

print(foo(15))