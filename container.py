from enum import Enum
from shapes import Sphere, Parallelepiped, Cylinder

class ComparisonOp(Enum):
    EQUAL = 1
    GREATER = 2
    LESS = 3

class ShapeContainer:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def print_all(self):
        print("=== СОДЕРЖИМОЕ КОНТЕЙНЕРА ===")
        print(f"Всего объектов: {len(self.shapes)}")
        if len(self.shapes) == 0:
            print("КОНТЕЙНЕР ПУСТ")
            return
        
        for i in range(len(self.shapes)):
            print(f"[{i+1}] ", end="")
            self.shapes[i].print_info()

    def _parse_operator(self, op_str):
        if op_str == ">": return ComparisonOp.GREATER
        if op_str == "<": return ComparisonOp.LESS
        if op_str in ("==", "="): return ComparisonOp.EQUAL
        return None

    def _matches_condition(self, shape, field, op, value):
        if field in ("density", "плотность"):
            try:
                val_float = float(value)
                if op == ComparisonOp.GREATER: return shape.density > val_float
                if op == ComparisonOp.LESS: return shape.density < val_float
                if op == ComparisonOp.EQUAL: return shape.density == val_float
            except ValueError:
                return False

        elif field in ("owner", "владелец"):
            if op == ComparisonOp.EQUAL: return shape.owner == value

        elif field == "type":
            if op == ComparisonOp.EQUAL: return shape.get_type() == value

        return False

    def remove_shape(self, condition):
        parts = condition.strip().split()
        if len(parts) != 3:
            return

        field = parts[0]
        op_str = parts[1]
        value = parts[2].replace('"', '').replace("'", "")
        
        op = self._parse_operator(op_str)
        if op is None:
            return

        new_shapes = []
        for s in self.shapes:
            if not self._matches_condition(s, field, op, value):
                new_shapes.append(s)

        self.shapes = new_shapes
        print(f"После удаления осталось: {len(self.shapes)}")

    def process_command(self, line, line_num):
        line = line.strip()
        if line == "": return
        print(f"\n[строка {line_num}] {line}")

        parts = line.split()
        cmd = parts[0]

        if cmd == "ADD":
            try:
                type_str = parts[1]
                density = float(parts[2])
                owner = parts[3]

                if type_str == "Sphere":
                    radius = int(parts[4])
                    self.add_shape(Sphere(density, owner, radius))
                elif type_str == "Parallelepiped":
                    length, width, height = int(parts[4]), int(parts[5]), int(parts[6])
                    self.add_shape(Parallelepiped(density, owner, length, width, height))
                elif type_str == "Cylinder":
                    x, y, r, h = float(parts[4]), float(parts[5]), float(parts[6]), float(parts[7])
                    self.add_shape(Cylinder(density, owner, x, y, r, h))
                print(f"[ADD] Объект успешно добавлен. Всего: {len(self.shapes)}")
            except (ValueError, IndexError):
                print("[ОШИБКА] Неверный формат данных команды ADD.")

        elif cmd == "REM":
            condition = line.replace("REM", "").strip()
            self.remove_shape(condition)

        elif cmd == "PRINT":
            self.print_all()
