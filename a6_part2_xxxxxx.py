class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    
    def __init__(self, bottomLeft : Point, topRight : Point, color : str = "black") -> None:
        """Initializes the Rectangle

        Args:
            bottomLeft (Point): the bottom left of the rectangle
            topRight (Point): The top right of the rectangle
            color (str): The color of the rectangle's outline, the default value is black

        Raises:
            ValueError: If the width or the height is a negative value
        """
        self.bottomLeft = bottomLeft
        self.topRight = topRight
        self.color = color.lower()
        self.width = self.topRight.x - self.bottomLeft.x
        self.height = self.topRight.y - self.bottomLeft.x
        if self.width <= 0 or self.height <= 0:
            raise ValueError
    
    @staticmethod
    def NULL() -> 'Rectangle':
        """WARNING DEPRECATED : use the Null rectangle class insteaad
        Return the Null rectangle

        Returns:
            Rectangle: A rectangle considered null
        """
        return Rectangle(Point(0.000000001,0.0000001), Point(0.000001,0.000001), "Null")
    def reset_color(self, color : str) -> None:
        """Updates the color to a new color

        Args:
            color (str): The new color of the rectangle's outline
        """
        self.color = color.lower()
    
    def get_bottom_left(self) -> Point:
        """Returns the bottom left of the rectangle

        Returns:
            Point: The coordinate of the bottom left
        """
        return self.bottomLeft
    
    def get_top_right(self) -> Point:
        """Returns the top right of the rectangle

        Returns:
            Point: The coordinate of the top rigt
        """
        return self.topRight
    
    def get_color(self) -> str:
        """Returns the color of the rectangle's outline

        Returns:
            str: the color as a string
        """
        return self.color
    def get_perimeter(self) -> int | float:
        """Returns the perimeter of a given rectangle

        Returns:
            int | float: The perimeter of the rectangle
        """
        return 2(self.width+self.height)
    def get_area(self) -> int | float:
        """Get the area of the rectangle

        Returns:
            int | float: Its area
        """
        return self.height*self.width
    def move(self, deltaX : int | float, deltaY : int | float) -> None:
        """Moves the rectangle by a given movement vector

        Args:
            deltaX (int | float): The x component of that vector
            deltaY (int | float): The y component of that vector
        """
        self.bottomLeft.move(deltaX, deltaY)
        self.topRight.move(deltaX, deltaY)
    def intersects(self, other : 'Rectangle') -> bool:
        """Verify if the calling rectangle intersects the passed rectangle

        Args:
            other (Rectangle): The rctangle that might intersect

        Returns:
            bool: True if they do intersect, false otherwise
        """
        return (self.bottomLeft.x < other.topRight.x) & (self.bottomLeft.y < other.topRight.y) & (self.topRight.x > other.bottomLeft.x) & (self.topRight.y > other.bottomLeft.y)
    def intersection(self, other : 'Rectangle') -> 'Rectangle':
        """Gives the are of the rectangles that intersects (overlap)

        Args:
            other (Rectangle): The passed rectangle

        Returns:
            Rectangle: A null rectangle if the intersection is an illegal rectangle, the interseciton otherwise
        """
        try:
            return Rectangle(Point(max(self.bottomLeft.x, other.bottomLeft.x), max(self.bottomLeft.y, other.bottomLeft.y), Point(min(self.topRight.x, other.topRight.x), min(self.topRight.y, other.topRight.y))))
        except ValueError as e:
            return NullRectangle()
    def contains(self, X : int | float, Y : int | float) -> bool:
        """Tells you if the rectangle contains a given point

        Args:
            X (int | float): The x coordinate
            Y (int | float): The Y coordinate

        Returns:
            bool: True if the rectangle contains that point, False otherwise
        """
        return (self.bottomLeft.x <= X <= self.topRight.x) & (self.bottomLeft.y <= Y <= self.topRight.y)

    def __repr__(self) -> str:
        """Techncal representation

        Returns:
            str: representation
        """
        # return f"Rectangle[width : {self.width}, height : {self.height}]"
        return f"Rectangle({self.bottomLeft},{self.topRight},{repr(self.color)})"
    def __str__(self) -> str:
        """User representation

        Returns:
            str: representation
        """
        return f"I am a red rectangle with bottom left corner at ({self.bottomLeft.x}, {self.bottomLeft.y}) and top right corner at ({self.topRight.x}, {self.topRight.y})."
    def __eq__(self, other: 'Rectangle') -> bool:
        """Returns wether or not the rectangles are the same

        Args:
            other (Rectangle): The other one

        Returns:
            bool: True if every attribute is the same EDIT: if the repr is the same
        """
        # return self.bottomLeft == other.bottomLeft and self.topRight == other.topRight and self.color == other.color
        return repr(self) == (repr(other) if other.type() != str else other)
class NullRectangle(Rectangle):
    def __init__(self) -> None:
        """Create a NullRectangle, a rectangle that is not valid"""
        self.bottomLeft = None
        self.topRight = None
        self.color = None
        self.width = None
        self.height = None

class Canvas:
    
    def __init__(self) -> None:
        """Initialize an empty canvas

        The canvas is empty, so there are no rectangles and the total perimeter is 0.
        The minimum bottom left and maximum top right coordinates are set to a default Point.
        The list of rectangles is empty.
        """
        self.minBottomLeft : Point 
        self.maxTopRight : Point 
        self.lenght : int = 0
        self.totalPerimeter : int | float= 0
        self.Rectangles : list[Rectangle] = []
    def addFirstRectangle(self, rectangle : Rectangle) -> None:
        """Does the necessary setup for adding the first rectangle : setting the min enclosing points initial coordinates

        Args:
            rectangle (Rectangle): The rectangle to add
        """
        self.length += 1
        self.totalPerimeter += rectangle.get_perimeter()
        self.minBottomLeft = rectangle.bottomLeft
        self.maxTopRight = rectangle.topRight
        self.Rectangles.append(rectangle)
    def add_one_rectangle(self, rectangle : Rectangle) -> None:
        """Adds a new rectangle to the canvas, delegates if it is the first one

        Args:
            rectangle (Rectangle): The rectangle to be added
        """
        if self.lenght == 0:
            self.addFirstRectangle(rectangle)
        else:
            self.length += 1
            self.totalPerimeter += rectangle.get_perimeter()
            if self.minBottomLeft.x > rectangle.bottomLeft.x: self.minBottomLeft.x = rectangle.bottomLeft.x
            if self.minBottomLeft.y > rectangle.bottomLeft.y: self.minBottomLeft.y = rectangle.bottomLeft.y
            if self.maxTopRight.x < rectangle.topRight.x: self.maxTopRight.x = rectangle.topRight.x
            if self.maxTopRight.y < rectangle.topRight.y: self.maxTopRight.y = rectangle.topRight.y
            self.Rectangles.append(rectangle)
    def count_same_color(self, color : str) -> int:
        """Returns the number of rectangles of a given color in thw canva

        Args:
            color (str): The color

        Returns:
            int: The number of rects of given color
        """
        count = 0
        for rectangle in self.Rectangles: count += (1 if rectangle.color == color else 0)
    
    def total_perimeter(self) -> int | float:
        """Returns the total perimeter of all rectangles in the canvas

        Returns:
            int | float: The total perimeter
        """
        return self.total_perimeter

    def min_enclosing_rectangle(self):
        if self.lenght == 0: return NullRectangle()
        else: return Rectangle(self.minBottomLeft, self.maxTopRight, "black")
    
    def common_point(self):
        """Returns True if all rectangles in the canvas intersect in a point

        Returns:
            bool: True if all rectangles intersect in a point, False otherwise
        """
        if self.lenght == 0 : return False
        intersection : Rectangle = self.Rectangles[0]
        for rectangle in self.Rectangles[1:]:
            intersection = intersection.intersection(rectangle)
            if intersection == NullRectangle():
                return False
        return True



    def __len__(self) -> int:
        return self.lenght