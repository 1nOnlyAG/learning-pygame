# a = 42
# print("a")
import sys
a = ["Hello World😂", 1, 3, 4, "foo", 42]

index = 0
while not a[index] == 42:
    print(a[index])
    index = index + 1

sys.exit()
def time_of_day_greeting(time_of_day):
    tod_to_word = {
        "evening": "night",
        "morning": "morning",
        "midday": "afternoon"
    }
    print("Have a good " + tod_to_word[time_of_day])

def greet(name, time_of_day):
    print("Hello, " + name) 
    print("Hope youre having a good day :)")
    time_of_day_greeting(time_of_day)

print("YO")
greet("AG", "morning")

# print(42 == 44)
