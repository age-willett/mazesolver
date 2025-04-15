from tkinter import Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.__point_a = point_a
        self.__point_b = point_b

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.__point_a.x,
            self.__point_a.y,
            self.__point_b.x,
            self.__point_b.y,
            fill=fill_color,
            width=2,
        )
