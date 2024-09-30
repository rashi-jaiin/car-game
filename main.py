from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=800, height=500)
y_positions = [-200, -100, 0, 100]
cars = []
names = ['red', 'green', 'blue', 'black']

user_choice = screen.textinput('Enter Your choice', 'Enter your choice from (red, green, blue, black):')

for i in range(4):
    image_path = f'images/car{i+1}.gif'
    screen.addshape(image_path)
    new_car = Turtle()
    new_car.name = names[i]
    new_car.penup()
    new_car.shape(image_path)
    new_car.goto(-350, y_positions[i])
    cars.append(new_car)
    


while True:

    car = random.choice(cars)
    if car.xcor() >= 400:
        print('Winner: ', car.name)
        if user_choice == car.name:
            print('You Won!')
        else:
            print('You Lost!')
        break
    car.forward(10)

















screen.exitonclick()