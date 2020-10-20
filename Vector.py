class Vector:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = None
        for arg in args:
            self.z = arg
        if self.z is None:
            self.three_dim = False
        else:
            self.three_dim = True

    def __repr__(self):
        """
        Магический метод, вызываемый при отображении информации об объекте
        Должен вернуть строку
        """
        if not self.three_dim:
            return f'Vector({self.x}, {self.y})'
        else:
            return f'Vector({self.x}, {self.y}, {self.z})'

    def __eq__(self, other):
        """
        Метод, определяющий равенство объектов

        >>> Vector(1, 2) == Vector(1, 2)
        True

        >>> Vector(1, 2) == Vector(2, 1)
        False
        """
        if self.three_dim:
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        """
        Магический метод, вызываемый при использовании оператора +

        >>> Vector(1, 2) + Vector(1, 5)
        Vector(2, 7)

        >>> Vector(1, 2) + 5
        Vector(6, 7)
        """
        if isinstance(other, Vector):
            if self.three_dim and other.three_dim:
                return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
            elif not self.three_dim and not other.three_dim:
                return Vector(self.x + other.x, self.y + other.y)
            else:
                raise TypeError(
                    f'cannot add 3d Vector to 2d'
                )
        elif isinstance(other, (int, float)):
            if self.three_dim:
                return Vector(self.x + other, self.y + other, self.z + other)
            else:
                return Vector(self.x + other, self.y + other)
        else:
            raise TypeError(
                f'cannot add {other.__class__.__name__} to Vector'
            )

    def __sub__(self, other):
        """
        Магический метод, вызываемый при использовании оператора -

        >>> Vector(3, 7) - Vector(1, 5)
        Vector(2, 2)

        >>> Vector(1, 2) - 1
        Vector(0, 1)
        """
        if isinstance(other, Vector):
            if self.three_dim and other.three_dim:
                return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
            elif not self.three_dim and not other.three_dim:
                return Vector(self.x - other.x, self.y - other.y)
            else:
                raise TypeError(
                    f'cannot substitute 3d Vector from 2d'
                )
        elif isinstance(other, (int, float)):
            if self.three_dim:
                return Vector(self.x - other, self.y - other, self.z - other)
            else:
                return Vector(self.x - other, self.y - other)
        else:
            raise TypeError(
                f'cannot substitute {other.__class__.__name__} from Vector'
            )

    def __mul__(self, other):
        """
        Магический метод, вызываемый при использовании оператора *

        >>> Vector(1, 2) * 5
        Vector(5, 10)
        """
        if isinstance(other, Vector):
            if self.three_dim and other.three_dim:
                return self.x * other.x + self.y * other.y + self.z * other.z
            elif not self.three_dim and other.three_dim:
                return self.x * other.x + self.y * other.y
            else:
                raise TypeError(
                    f'cannot multiply 3d Vector by 2d'
                )
        elif isinstance(other, (int, float)):
            if self.three_dim:
                return Vector(self.x * other, self.y * other, self.z * other)
            else:
                return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(
                f'cannot multiply Vector by {other.__class__.__name__}'
            )

    def __truediv__(self, other):
        """
        Магический метод, вызываемый при использовании оператора /

        >>> Vector(1, 2) / 5
        Vector(0.2, 0.4)
        """
        if isinstance(other, (int, float)):
            if self.three_dim:
                return Vector(self.x / other, self.y / other, self.z / other)
            else:
                return Vector(self.x / other, self.y / other)
        else:
            raise TypeError(
                f'cannot divide Vector by {other.__class__.__name__}'
            )

    def __neg__(self):
        """
        Унарное отрицание:
        >>> -Vector(1, 2)
        Vector(-1, -2)
        >>> -Vector(0, 0)
        Vector(0, 0)
        """
        if self.three_dim:
            return Vector(-self.x, -self.y, -self.z)
        else:
            return Vector(-self.x, -self.y)

    def __abs__(self):
        """
        Возвращает длину вектора (неявно вызывается встроенной функцией abs):
        >>> abs(Vector(1, 2))
        2.23607
        >>> abs(Vector(3, 4))
        5.0
        """
        if self.three_dim:
            return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        else:
            return (self.x ** 2 + self.y ** 2) ** 0.5

    def __matmul__(self, other):
        """
        Метод реализует векторное произведение двух векторов в трёхмерном пространстве
        :return: Векторное произведение двух векторов
        """
        if isinstance(other, Vector):
            if self.three_dim and other.three_dim:
                tx = self.y * other.z - self.z * other.y
                ty = -self.x * other.z + self.z * other.x
                tz = self.x * other.y - self.y * other.x
                return Vector(tx, ty, tz)
            else:
                raise TypeError(
                    'Inappropriate input data'
                )
        else:
            raise TypeError(
                'Inappropriate input data'
            )


def area(first, other_1, *args):
    """
    Функция считает площадь параллелограмма, натянутого на пару векторов
    """
    other_2 = None
    for arg in args:
        other_2 = arg
    if not (other_2 is None):
        raise TypeError(
            'cannot calculate area of 3 and more Vectors'
        )
    else:
        if isinstance(other_1, Vector):
            if first.three_dim and other_1.three_dim:
                return abs(first @ other_1)
            elif not first.three_dim and not other_1.three_dim:
                return abs(first.x * other_1.y - other_1.x * first.y)
            else:
                raise TypeError(
                    'cannot calculate area of Vectors from different dimensions'
                )
        else:
            raise TypeError(
                f'cannot calculate area of {other_1.__class__.__name__} and Vector'
            )


def volume(first, other_1, other_2, *args):
    other_3 = None
    for arg in args:
        other_3 = arg
    if not (other_3 is None):
        raise TypeError(
            'cannot calculate volume of 4 and more Vectors'
        )
    else:
        if isinstance(other_1, Vector) and isinstance(other_2, Vector):
            return abs(first.x * (other_1.y * other_2.z - other_1.z * other_2.y) + \
                       first.y * (-other_1.x * other_2.z + other_1.z * other_2.x) + \
                       first.z * (other_1.x * other_2.y - other_1.y * other_2.x))
        else:
            raise TypeError(
                f'cannot calculate volume of {other_1.__class__.__name__}, {other_2.__class__.__name__} and Vector'
            )


if __name__ == '__main__':
    a = Vector(2, 3, 1)
    b = Vector(5, 3, 2)
    c = Vector(1, 2, 3)
    d = Vector(0, 1)
    e = Vector(1, 0)
    f = Vector(0, -1)
    print(a @ b)
    print(abs(a))
    print(volume(a, b, c))
    print(area(d, e))
    print(area(d, f))
