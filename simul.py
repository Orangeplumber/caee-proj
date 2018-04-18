from graphics import *

def main():
	win = GraphWin("My Circle", 1000, 1000)
	message = Text(Point(3,4), "Hello!")
	message.draw(win)
	c = Circle(Point(50,50), 10)
	win.plot(35, 35, "blue")
	c.draw(win)
	win.getMouse() # pause for click in window
	# win.close()

main()

# def euler():
