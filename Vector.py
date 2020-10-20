class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        '''
        Магический метод, вызываемый при отображении информации об объекте
        Должен вернуть строку
        '''
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        '''
        Метод, определяющий равенство объектов

        >>> Vector(1, 2) == Vector(1, 2)
        True

        >>> Vector(1, 2) == Vector(2, 1)
        False
        '''
        return self.x == other.x and self.y == other.y


    def __add__(self, other):
        '''
        Магический метод, вызываемый при использовании оператора +
        
        >>> Vector(1, 2) + Vector(1, 5)
        Vector(2, 7)

        >>> Vector(1, 2) + 5
        Vector(6, 7)
        '''
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError(
                f'cannot add {other.__class__.__name__} to Vector'
            )

    def __sub__(self, other):
        '''
        Магический метод, вызываемый при использовании оператора -
        
        >>> Vector(3, 7) - Vector(1, 5)
        Vector(2, 2)

        >>> Vector(1, 2) - 1
        Vector(0, 1)
        '''
        pass

    def __mul__(self, other):
        '''
        Магический метод, вызываемый при использовании оператора *
        
        >>> Vector(1, 2) * 5
        Vector(5, 10)
        '''
        pass

    def __truediv__(self, other):
        '''
        Магический метод, вызываемый при использовании оператора /
        
        >>> Vector(1, 2) / 5
        Vector(0.2, 0.4)
        '''
        pass

    def __neg__(self):
        '''
        Унарное отрицание:
        >>> -Vector(1, 2, 3)
        Vector(-1, -2, -3)
        >>> -Vector(0, 0, 0)
        Vector(0, 0, 0)
        '''
        pass

    def __abs__(self):
        '''
        Возвращает длину вектора (неявно вызывается встроенной функцией abs):
        >>> abs(Vector(1, 2, 3))
        3.7416573867739413
        >>> abs(Vector(3, 4, 0))
        5.0
        '''
        pass


a = Vector(2, 3)
b = Vector(1, 5)
print(a + b)
print(a + 2)
print(a + 'Hello') # TypeError
