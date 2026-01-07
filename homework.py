#ex1
import random

number = random.randint(1, 10)
result = 1
temp = number

while temp > 0:
    result *= temp
    temp -= 1

print(f"num = {number}")
print(f"result = {result}")

#ex2
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n_terms = 9
print(f"Input: {n_terms}")
for i in range(n_terms + 1):
    print(fibonacci(i), end=", ")

    #ex3
    # -------- Car Class --------
class Car:
    def __init__(self, position, speed):
        self.position = position
        self.speed = speed
        self.steering_angle = 0.0

    def steer(self, value):
        self.steering_angle = value

    def update_position(self):
        self.position += self.steering_angle * self.speed
        print(f"Step Position -> {self.position:.3f}")


class LaneSensor:
    def get_lane_offset(self, current_position):
        return current_position


class Controller:
    def decide(self, offset):
        correction_strength = 0.15
        if offset > 0:
            return -correction_strength
        elif offset < 0:
            return correction_strength
        return 0.0


vehicle = Car(position=6.5, speed=0.8)
sensor = LaneSensor()
controller = Controller()

print("Starting Lane Correction Simulation\n")

for step in range(1, 21):
    deviation = sensor.get_lane_offset(vehicle.position)
    steering_command = controller.decide(deviation)

    vehicle.steer(steering_command)
    vehicle.update_position()

