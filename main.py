#!/usr/bin/python

from drawable import Line, Point

from graphics import Window

if __name__ == "__main__":
    win = Window(800, 600)
    win.draw_line(Line(Point(200, 200), Point(600,400)), "black")
    win.draw_line(Line(Point(600,200), Point(200,400)), "red")
    win.wait_for_close()
