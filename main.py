#!/usr/bin/python

from drawable import Cell, Point

from graphics import Window

if __name__ == "__main__":
    win = Window(800, 600)
    win.draw_cell(Cell(Point(100,100), Point(160,160)))
    win.draw_cell(Cell(Point(160,100), Point(220,160)), "red")
    win.draw_cell(Cell(Point(220,100), Point(280,160)), "green")
    win.draw_cell(Cell(Point(280,100), Point(340,160)), "blue")
    win.wait_for_close()

