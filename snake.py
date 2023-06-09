from turtle import Turtle

# Declaring Constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    # Creating snakes when initiating the game.
    def create_snake(self):
        self.snake_head()
        for position in STARTING_POSITIONS[1:]:
            self.add_segment(position)

    def snake_head(self):
        snake_head = Turtle("circle")
        snake_head.color("orange")
        snake_head.penup()
        snake_head.goto(STARTING_POSITIONS[0])
        self.snake_segments.append(snake_head)

    # Adds segment to the snake.
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    # Increase the length of the snake.
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    # Moving the snake by moving the last snake to second last snake position
    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # Changing the direction of the snake with keyboard interaction.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
