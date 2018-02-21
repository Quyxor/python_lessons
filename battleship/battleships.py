# coding: utf-8

from random import randrange
import os


class Ship(object):
    """Корабль"""

    def __init__(self, tp, x=-1, y=-1, rotation=0):
        """
        Конструктор.

        Args:
            tp (int): тип (длина) корабля.
            x  (int): координата X начала корабля.
            y  (int): координата Y начала корабля.
            rotation (int): ориентация (0 - горизонтально, 1 - вертикально)
        """
        self.__x = None
        self.__y = None
        self.__rotation = None
        self.field = None

        self.__type = tp
        self.__health = tp

        self.update_pos(x, y, rotation)

    def __contains__(self, coord):
        x, y = coord
        x1, y1 = self.first_coord
        x2, y2 = self.last_coord
        return x1 <= x <= x2 and y1 <= y <= y2

    def in_halo(self, x, y):
        x1, y1 = self.first_halo_coord
        x2, y2 = self.last_halo_coord
        return x1 <= x <= x2 and y1 <= y <= y2

    @property
    def type(self):
        return self.__type

    @property
    def first_coord(self):
        """Возвращает координату начала корабля"""
        return self.__x, self.__y

    @property
    def last_coord(self):
        """Возвращает координату конца корабля"""
        r = self.__rotation
        i = self.__type - 1
        return self.__x + i * r, self.__y + i * (1 - r)

    @property
    def first_halo_coord(self):
        x, y = self.first_coord
        return x - 1, y - 1

    @property
    def last_halo_coord(self):
        x, y = self.last_coord
        return x + 1, y + 1

    def attack(self):
        """Выполняет атаку на корабль, уменьшая его здоровье на единицу."""
        if not self.is_killed():
            self.__health -= 1

    def coords(self):
        """Возвращает генератор со списком координат (кортежей), которые занимает корабль."""
        x1, y1 = self.first_coord
        x2, y2 = self.last_coord
        return ((x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))

    def halo(self):
        """Возвращает генератор со списком координат (кортежей) ореола вокруг корабля."""
        x1, y1 = self.first_halo_coord
        x2, y2 = self.last_halo_coord

        return ((x, y)
                for x in range(x1, x2 + 1)
                for y in range(y1, y2 + 1)
                if (x, y) not in self and (x, y) in self.field)

    def is_killed(self):
        """
        Проверяет состояние корабля.

        Returns:
             bool: возвращает True, если корабль убит, в противом случаи False.
        """
        return not self.__health

    def update_pos(self, x, y, r):
        """Устанавливает новую координату начала корабля"""
        self.__x = x
        self.__y = y
        self.__rotation = r


class Field(object):
    """
    Игровое поле.
    Корабли размещаются в поле. Атака идет на поле. Поле ведет учет выстрелов.
    """
    SHOT_MISSED = 1  # промах
    SHOT_INJURED = 2 # ранен
    SHOT_KILLED = 3  # убит
    SHOT_HALO = 4    # ореол

    def __init__(self, rows=10, cols=10):
        """
        Конструктор.

        Arguments:
            rows (int): высота поля.
            cols (int): ширина поля.
        """
        self.__rows = rows
        self.__cols = cols
        self.__ships = []
        self.__shots = {}

    def __contains__(self, coord):
        """Возвращает True, если ячейка с указанными координатами существует, в противном случаи False."""
        x, y = coord
        return 0 <= x < self.rows and 0 <= y < self.cols

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    def add_ship(self, ship):
        """
        Добавляет корабль в поле с проверкой.

        Arguments:
            ship (Ship): корабль.

        Returns:
            bool: возвращает True, если корабль удалось добавить в поле или False, если свободного места не оказалось.
        """
        if not isinstance(ship, Ship):
            return False

        if not self.check_pos(ship):
            return False

        ship.field = self
        self.__ships.append(ship)

        return True

    def check_pos(self, ship):
        """
        Проверяет, можно ли корабль с текущими координатами разместить в поле.
        Другими словами он берет координаты из корабля и проверяет ячейки поля на пустоту.

        Arguments:
            ship (Ship): корабль.

        Returns:
            bool: возвращает True, если все координаты корабля - свободные ячейки в поле.
        """
        if ship.first_coord not in self or ship.last_coord not in self:
            return False

        for x, y in ship.coords():
            if self.get_ship_by_point(x, y, include_halo=True):
                return False

        return True

    def attack(self, x, y):
        """
        Выполняет атаку в указанные координаты и возвращает ее результат.

        Arguments:
            x (int): координата X
            y (int): координата Y

        Returns:
             int:  результат выстрела (промах, ранил, убил)
             dict: точки поля, которые были затронуты (изменили свое состояние) после выстрела.
        """
        if (x, y) in self.__shots:
            return

        ship = self.get_ship_by_point(x, y)

        if ship:
            ship.attack()
            state = Field.SHOT_KILLED if ship.is_killed() else Field.SHOT_INJURED
        else:
            state = Field.SHOT_MISSED

        points = {}

        if ship and ship.is_killed():
            for point in ship.coords():
                self.__shots[point] = points[point] = Field.SHOT_KILLED

            for point in ship.halo():
                if point not in self.__shots:
                    self.__shots[point] = points[point] = Field.SHOT_HALO

        self.__shots[x, y] = points[x, y] = state

        return state, points

    def get_ship_by_point(self, x, y, include_halo=False):
        """
        Выполняет поиск корабля в поле в заданных координатах.
        Если указан флаг include_halo, то при поиске учитывается ореол корабля.

        Arguments:
            x (int): координата X.
            y (int): координата Y.
            include_halo (bool): учитывать ореол корабля.

        Returns:
             Ship|None: возвращает корабль или None, если не найден.
        """
        for ship in self.__ships:
            if (x, y) in ship:
                return ship

            if include_halo and ship.in_halo(x, y):
                return ship

    @property
    def ships_afloat(self):
        """
        Returns:
             int: возвращает количество кораблей на плаву.
        """
        return sum(1 for ship in self.__ships if not ship.is_killed())


class Game(object):
    def __init__(self):
        self.enemy_field = None
        self.enemy_view = None
        self.started = False

    def start(self):
        self.enemy_field = Field()
        self.random_strategy(self.enemy_field)

        # self.enemyView = FieldView(self.enemy_field.rows, self.enemy_field.cols)
        self.enemyView = AsciiFieldView(self.enemy_field.rows, self.enemy_field.cols)
        self.enemyView.render()

        self.started = True

        while self.started:
            x, y = self.ask_point()
            result = self.enemy_field.attack(x, y)

            if result is None:
                print('Вы уже стреляли в эту точку!')
            else:
                state, points = result
                self.enemyView.update(points)

                if state == Field.SHOT_KILLED and self.enemy_field.ships_afloat == 0:
                    self.finish()

    def ask_point(self):
        msg = 'Введите координаты выстрела в формате x,y: '

        while True:
            try:
                x, y = [int(i) for i in input(msg).split(',', 1)]
                return x, y
            except ValueError:
                print('Не корректный ввод')

    def finish(self):
        self.started = False
        self.enemy_field = None
        self.enemy_view = None

    @staticmethod
    def random_strategy(field):
        """Стратегия случайной расстановки кораблей"""
        ship_types = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        ship_types.sort(reverse=True)

        for tp in ship_types:
            ship = Ship(tp)
            ok = False

            while not ok:
                ship.update_pos(randrange(field.cols),
                                randrange(field.rows),
                                randrange(2) if ship.type > 1 else 0)
                ok = field.add_ship(ship)


class FieldView(object):
    CELL_EMPTY = '.'   # пустая клетка
    CELL_SHIP = '@'    # корабль
    CELL_MISSED = '0'  # промах
    CELL_INJURED = '*' # ранен
    CELL_KILLED = 'X'  # убит
    CELL_HALO = '#'    # ореол

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [self.CELL_EMPTY] * self.cols * self.rows

    def __do_update(self, state, points):
        for point in points:
            index = self._point2index(*point)

            if index < len(self.matrix):
                self.matrix[index] = state

    def _point2index(self, x, y):
        """
        Arguments:
            x (int): координата X.
            y (int): координата Y.

        Returns:
             int: возвращает индекс в списке, переведенный из координаты.
        """
        return x * self.cols + y

    def _render_row(self, *args):
        """
        Отрисовывает одну строчку поля.

        Arguments:
            args (list): данные, отображаемые в строке.
        """
        print(self._row_pattern().format(*args))

    def _row_pattern(self):
        """
        Returns:
             str: возвращает шаблон строчки, пригодный для использования методом .format()
        """
        size = len(str(max(self.rows, self.cols) - 1)) + 2
        pattern = '{{:^{size}}}'.format(size=size)
        return pattern * (self.cols + 1)

    def render(self):
        """Отрисовывает поле целиком."""
        os.system('clear')
        
        self._render_row('', *range(self.cols))

        for i in range(self.rows):
            start = self._point2index(i, 0)
            to = self._point2index(i, self.cols)
            self._render_row(i, *self.matrix[start:to])

    def render_ships(self, points):
        """
        Добавляет в поле информацию о расположении кораблей и перерисовывает его целиком.

        Arguments:
            points (list): список координат кораблей.
        """
        self.__do_update(self.CELL_SHIP, points)
        self.render()

    def update(self, points):
        """
        Обновляет состояния клеток поля и перерисовывает его целиком.

        Arguments:
            points (dict): состояния клеток
        """
        chars = {
            Field.SHOT_MISSED: self.CELL_MISSED,
            Field.SHOT_INJURED: self.CELL_INJURED,
            Field.SHOT_KILLED: self.CELL_KILLED,
            Field.SHOT_HALO: self.CELL_HALO
        }

        data = {}

        for point, state in points.items():
            if state in chars:
                data.setdefault(chars[state], []).append(point)

        for s, p in data.items():
            self.__do_update(s, p)

        self.render()


class AsciiFieldView(FieldView):
    CELL_EMPTY = ''

    def _row_pattern(self):
        """
        Returns:
             str: возвращает шаблон строчки, пригодный для использования методом .format()
        """
        size = len(str(max(self.rows, self.cols) - 1)) + 2
        pattern = '{{:^{size}}}│'.format(size=size)
        line = '─' * size + '┼'
        return '{}\n{}'.format(pattern * (self.cols + 1), line * (self.cols + 1))
