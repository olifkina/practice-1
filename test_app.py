import unittest
import math
from shapes import Sphere, Parallelepiped, Cylinder
from container import ShapeContainer

class TestShapes(unittest.TestCase):
    def test_sphere_calculations(self):
        s = Sphere(5.0, "Власова", 10)
        self.assertAlmostEqual(s.get_volume(), (4/3) * math.pi * 1000)
        self.assertAlmostEqual(s.get_surface_area(), 4 * math.pi * 100)
        self.assertEqual(s.get_type(), "Sphere")

    def test_parallelepiped_calculations(self):
        p = Parallelepiped(2.0, "Иванов", 2, 3, 4)
        self.assertEqual(p.get_volume(), 24)
        self.assertEqual(p.get_surface_area(), 52)
        self.assertEqual(p.get_type(), "Parallelepiped")

    def test_cylinder_calculations(self):
        c = Cylinder(1.5, "Андреев", 0.0, 0.0, 5.0, 10.0)
        self.assertAlmostEqual(c.get_volume(), math.pi * 25 * 10)
        self.assertAlmostEqual(c.get_surface_area(), 2 * math.pi * 5 * (5 + 10))
        self.assertEqual(c.get_type(), "Cylinder")


class TestContainer(unittest.TestCase):
    def setUp(self):
        self.container = ShapeContainer()

    def test_add_shapes(self):
        self.container.process_command("ADD Sphere 7.8 Власова 10", 1)
        self.assertEqual(len(self.container.shapes), 1)
        self.assertEqual(self.container.shapes[0].owner, "Власова")

    def test_remove_by_density(self):
        self.container.process_command("ADD Sphere 7.8 Власова 10", 1)
        self.container.process_command("ADD Parallelepiped 2.5 Андреев 5 10 15", 2)
        self.container.process_command("REM плотность > 5.0", 3)
        # Шар должен удалиться, параллелепипед остаться
        self.assertEqual(len(self.container.shapes), 1)
        self.assertEqual(self.container.shapes[0].get_type(), "Parallelepiped")

    def test_remove_by_owner(self):
        self.container.process_command("ADD Sphere 7.8 Власова 10", 1)
        self.container.process_command("ADD Cylinder 1.2 Иванов 0 0 5 10", 2)
        self.container.process_command("REM owner == Иванов", 3)
        self.assertEqual(len(self.container.shapes), 1)
        self.assertEqual(self.container.shapes[0].owner, "Власова")

    def test_remove_nonexistent(self):
        self.container.process_command("ADD Sphere 7.8 Власова 10", 1)
        self.container.process_command("REM владелец == Петров", 2)
        # Никто не удалится
        self.assertEqual(len(self.container.shapes), 1)


class TestExceptions(unittest.TestCase):
    def setUp(self):
        self.container = ShapeContainer()

    def test_invalid_add_command(self):
        # Передаем строку 'ОШИБКА' вместо плотности (числа)
        self.container.process_command("ADD Sphere ОШИБКА Власова 10", 1)
        # Программа не должна упасть, но фигура не добавится
        self.assertEqual(len(self.container.shapes), 0)

    def test_invalid_rem_condition(self):
        self.container.process_command("ADD Sphere 7.8 Власова 10", 1)
        # Передаем текст вместо числа для плотности
        self.container.process_command("REM плотность > НЕЧИСЛО", 2)
        # Программа перехватит ValueError и ничего не удалит
        self.assertEqual(len(self.container.shapes), 1)

    def test_empty_command(self):
        # Пустая команда не должна вызывать ошибок
        self.container.process_command("", 1)
        self.assertEqual(len(self.container.shapes), 0)

if __name__ == '__main__':
    unittest.main()
