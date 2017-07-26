from math import sqrt, acos, degrees, pi
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector.'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        new_coordinates = []
        n = len(self.coordinates)
        for i in range(n):
            new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        return Vector(new_coordinates)

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(self, c):
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1. / magnitude)
        except ZeroDivisionError:
            raise Exception(CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot(self, v):
        return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])

    def angle_with(self, v, in_degrees=False):
        try:
            u1 = self.normalize()
            u2 = v.normalize()
            angle_in_radians = acos(round(u1.dot(u2), 10))

            if in_degrees:
                degrees_per_radian = 180. / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance

    def is_parallel_to(self, v):
        return ( self.is_zero() or
            v.is_zero() or
            self.angle_with(v) == 0
            or self.angle_with(v) == pi )

    def is_zero(self, tolerance=1e-10):
        return self.magnitude() < tolerance





#### QUIZ PROBLEMS #######
my_vector = Vector([1, 2, 3])
print my_vector # => Vector: (1, 2, 3)
my_vector2 = Vector([1, 2, 3])
my_vector3 = Vector([-1, 2, 3])
print my_vector == my_vector2 # true
print my_vector == my_vector3 # false

# Plus, Minus and Scalar Multiply
print Vector([8.218, -9.341]).plus(Vector([-1.129, 2.111]))
print Vector([7.119, 8.215]).minus(Vector([-8.223, 0.878]))
print Vector([1.671, -1.012, -0.318]).times_scalar(7.41)

# Magnitude and Direction
print Vector([-0.221, 7.437]).magnitude()
print Vector([8.813, -1.331, -6.247]).magnitude()
print Vector([5.581, -2.136]).normalize()
print Vector([1.996, 3.108, -4.554]).normalize()

# Dot Product and Angle
print Vector([7.887, 4.138]).dot(Vector([-8.802, 6.776]))
print Vector([-5.955, -4.904, -1.874]).dot(Vector([-4.496, -8.755, 7.103]))
# print Vector([3.183, -7.627]).get_angle_radian(Vector([-2.668, 5.319]))
# print Vector([7.35, 0.221, 5.188]).get_angle_degree(Vector([2.751, 8.259, 3.985]))
print Vector([3.183, -7.627]).angle_with(Vector([-2.668, 5.319]))
print Vector([7.35, 0.221, 5.188]).angle_with(Vector([2.751, 8.259, 3.985]))

# Parallel and Orthogonal Vectors
# TODO fix Problem - math domain error
v = Vector([-7.579, -7.88])
w = Vector([22.737, 23.64])
print v.is_orthogonal_to(w)
print v.is_parallel_to(w)

v = Vector([-2.029, 9.97, 4.172])
w = Vector([-9.231, -6.639, -7.245])
print v.is_orthogonal_to(w)
print v.is_parallel_to(w)

v = Vector([-2.328, -7.284, -1.214])
w = Vector([-1.821, 1.072, -2.94])
print v.is_orthogonal_to(w)
print v.is_parallel_to(w)

v = Vector([2.118, 4.827])
w = Vector([0, 0])
print v.is_orthogonal_to(w)
print v.is_parallel_to(w)

# Projecting Vectors

# Orthogonality - tool for decomposing objects into combinations of simpler objects in a structured way
# b constant vector - standing for the word basis, emanating from the origin
# line l contains the arrow
# projecting v onto b
# measure the apparent magnitude of arrow v from this point of view - v will look shorter - projection of v onto b
# right triangle: hypotenuse is arrow v, leg is perpindicular to l and orthogonal to be

# vector v = the sum of v parallel to b and v orthogonal to b

# computing project of v onto the basis vector b
# assumption angle between b and v is at most 90 degrees



































