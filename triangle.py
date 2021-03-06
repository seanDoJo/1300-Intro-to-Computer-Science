from graphics import *

def main():
	win = GraphWin("Triangular!")
	win.setCoords(0.0,0.0,10.0,10.0)
	message = Text(Point(5, 0.5), "Click three points")
	message.draw(win)

	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)
	p3 = win.getMouse()
	p3.draw(win)

	triangle = Polygon(p1, p2, p3)
	triangle.setFill("red")
	triangle.setOutline("cyan")
	triangle.draw(win)

	message.setText("Click to quit")
	win.getMouse()
	
	win.close()
	exit(0)
main()
