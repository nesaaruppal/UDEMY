from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def extend(self):
        self.add_segment(self.segments[-1].position())

        # starting_positions = [(0, 0), (-20, 0), (-40, 0)

        #segments = []
        # for position in starting_positions:
        #    new_segment = Turtle("square")
        #    new_segment.color("white")
        #    new_segment.penup()
        #    new_segment.goto(position)
        #    segments.append(new_segment

        # for seg_num in range(len(segments) - 1, 0, -1):
        #    new_x = segments[seg_num - 1].xcor()
        #    new_y = segments[seg_num - 1].ycor()
        # segments[seg_num].goto(new_x, new_y

        # segment_1 = Turtle("square")
        # segment_1.color("white")

        # segment_2 = Turtle("square")
        # segment_2.color("white")
        # segment_2.penup()
        # segment_2.goto(-20, 0)

        # segment_3 = Turtle("square")
        # segment_3.color("white")
        # segment_3.penup()
        # segment_3.goto(-40, 0)
