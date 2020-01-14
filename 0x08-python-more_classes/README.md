# 0x08. Python - More Classes and Objects

Project giving us more practice on Python classes and objects

### 0-rectangle.py
Contains an empty class `Rectangle`

### 1-rectangle.py
Contains a class `Rectangle` (based on `0-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self)`: to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
     		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`

### 2-rectangle.py
Contains a class `Rectangle` (based on `1-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
        property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter is equal to `0`

### 3-rectangle.py
Contains a class `Rectangle` (based on `2-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
     		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
	  if `width` or `height` is equal to `0`, return an empty string

### 4-rectangle.py
Contains a class `Rectangle` (based on `3-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
	  if `width` or `height` is equal to `0`, return an empty string
`repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

### 5-rectangle.py
Contains a class `Rectangle` (based on `4-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
	  if `width` or `height` is equal to `0`, return an empty string
`repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

### 6-rectangle.py
Contains a class `Rectangle` (based on `5-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public class attribute `number_of_instances`:
        Initialized to `0`
        Incremented during each new instance instantiation
        Decremented during each instance deletion
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
	if `width` or `height` is equal to `0`, return an empty string
`repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
     Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

### 7-rectangle.py
Contains a class `Rectangle` (based on `6-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public class attribute `number_of_instances`:
        Initialized to `0`
        Incremented during each new instance instantiation
        Decremented during each instance deletion
Public class attribute `print_symbol`:
        Initialized to `#`
        Used as symbol for string representation
        Can be any type
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
	if `width` or `height` is equal to `0`, return an empty string
`repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted

### 8-rectangle.py
Contains a class `Rectangle` (based on `7-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public class attribute `number_of_instances`:
        Initialized to `0`
     	Incremented during each new instance instantiation
     	Decremented during each instance deletion
Public class attribute `print_symbol`:
        Initialized to `#`
	Used as symbol for string representation
	Can be any type
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
	if `width` or `height` is equal to `0`, return an empty string
`repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
        `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
     	`rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
     	Returns `rect_1` if both have the same area value

### 9-rectangle.py
Contains a class `Rectangle` (based on `8-rectangle.py`)

#### Defined by:
Private instance attribute: `width`:
	property `def width(self):` to retrieve it
     	property setter `def width(self, value):` to set it:
     		 `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
     		 if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
Private instance attribute: `height`:
	property `def height(self):` to retrieve it
     	property setter `def height(self, value):` to set it:
		 `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
     		 if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
Public class attribute `number_of_instances`:
        Initialized to `0`
     	Incremented during each new instance instantiation
     	Decremented during each instance deletion
Public class attribute `print_symbol`:
	Initialized to `#`
	Used as symbol for string representation
	Can be any type
Public instance method: `def area(self):` that returns the rectangle area
Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
        if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
`print()` and `str()` should print the rectangle with the character `#`: (see example below)
     	if `width` or `height` is equal to `0`, return an empty string
`repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
        `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
     	`rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
     	Returns `rect_1` if both have the same area value
Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
