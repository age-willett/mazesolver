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

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._win = None
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bottom_right.x
        self._y2 = bottom_right.y

    def draw(self, canvas: Canvas, fill_color):
        self._win = canvas
        if self.has_left_wall:
            Line(Point(self._x1, self._y1), Point(self._x1, self._y2)).draw(canvas, fill_color)
        if self.has_right_wall:
            Line(Point(self._x2, self._y1), Point(self._x2, self._y2)).draw(canvas, fill_color)
        if self.has_top_wall:
            Line(Point(self._x1, self._y1), Point(self._x2, self._y1)).draw(canvas, fill_color)
        if self.has_bottom_wall:
            Line(Point(self._x1, self._y2), Point(self._x2, self._y2)).draw(canvas, fill_color)
