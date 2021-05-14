Right triangle

A right triangle is a triangle in which one angle is a right angle (90-degree angle). The side opposite to the right angle is called a hypotenuse and the other two sides are called legs (or catheti).

The Pythagorean theorem holds for right triangles with integer lengths of all sides:

c2=a2+b2, where c is the length of the hypotenuse, and a and b are the lengths of the legs.

Here's a class RightTriangle with the class constructor. The constructor is missing the area attribute. Calculate the area S according to this formula:

S=12ab.

Three numbers ( input_c, input_a, and input_b) have already been read from the input. They represent a triangle: the first number is the length of the supposed hypotenuse, the other two are the legs. If the triangle with these sides is right, create an instance of the class RightTriangle and print its area (with one decimal). If the triangle is not right, print "Not right".


Sample Input:
5 3 4

Sample Output:
6.0


Sample Input:
4 3 2

Sample Output:
Not right


Sample Input:
13 12 5

Sample Output:
30.0
