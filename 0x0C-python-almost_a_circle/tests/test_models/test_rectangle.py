"""Unit test for the class Rectangle
"""
import unittest
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """TestRectangleClass resume

    Args:
        unittest (): Propertys for unit testing
    """
    def setUp(self):
        """Return to 0 class attributes"""
        Base._Base__nb_objects = 0

    def test_empty(self):
        """Test the base class without params
        """
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 1)

    def test_2_params(self):
        """Test with 2 params
        """
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_4_params(self):
        """Test with 4 params
        """
        r2 = Rectangle(2, 4, 3, 1)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 1)

    def test_5_params(self):
        """Test with 5 params
        """
        r3 = Rectangle(2, 4, 3, 1, 50)
        self.assertEqual(r3.id, 50)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 1)

    def test_type_errors(self):
        """Test with not int input
        """
        self.assertRaises(TypeError, Rectangle, "2", 2)
        self.assertRaises(TypeError, Rectangle, 2, "2")
        self.assertRaises(TypeError, Rectangle, [2], [2])
        self.assertRaises(TypeError, Rectangle, (2,), 2)
        self.assertRaises(TypeError, Rectangle, 2.0, 2.5)
        self.assertRaises(TypeError, Rectangle, 2, 2, [2], 2)
        self.assertRaises(TypeError, Rectangle, 2, 2, 2, [2])
        self.assertRaises(TypeError, Rectangle, 2, 2, 2, [2], 2)

    def test_value_errors(self):
        """Test with 0 and negative inputs
        """
        self.assertRaises(ValueError, Rectangle, 0, 0)
        self.assertRaises(ValueError, Rectangle, -2, 2)
        self.assertRaises(ValueError, Rectangle, -2, -2)
        self.assertRaises(ValueError, Rectangle, 2, 2, 0, -2)
        self.assertRaises(ValueError, Rectangle, 2, 2, 2, -2)
        self.assertRaises(ValueError, Rectangle, 2, 2, -2, 2, 2)

    def test_area(self):
        """Test area response
        """
        r_area = Rectangle(2, 4)
        self.assertEqual(r_area.area(), 8)
        r_area = Rectangle(5, 5, 5, 5)
        self.assertEqual(r_area.area(), 25)

    def test_display_nocoords(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2)
            r1.display()
            self.assertEqual(fake_out.getvalue(), "##\n##\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2 = Rectangle(1, 1)
            r2.display()
            self.assertEqual(fake_out.getvalue(), "#\n")

    def test_str_response(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (1) 0/0 - 2/2\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 2, 1, 12)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (12) 2/1 - 4/6\n")

    def test_display_coords(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(2, 2, 1, 1)
            r1.display()
            self.assertEqual(fake_out.getvalue(), "\n ##\n ##\n")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2 = Rectangle(1, 1, 4, 4)
            r2.display()
            self.assertEqual(fake_out.getvalue(), "\n\n\n\n    #\n")

    def test_update_1_value(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 10/10\n")

    def test_update_2_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/10\n")

    def test_update_3_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20, 5)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/5\n")

    def test_update_4_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20, 5, 1)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/10 - 20/5\n")

    def test_update_5_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(4, 20, 5, 1, 6)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/6 - 20/5\n")

    def test_update_empty(self):
        """Test update empty
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update()
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (1) 10/10 - 10/10\n")

    def test_update_typerrors(self):
        """Test update empty
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertRaises(TypeError, r1.update, 1, [1])
        self.assertRaises(TypeError, r1.update, 1, 2, "4")
        self.assertRaises(TypeError, r1.update, 1, 2, 3, "4")
        self.assertRaises(TypeError, r1.update, 1, 2, 3, 4, "5")

    def test_update_valerrors(self):
        """Test update bad inputs
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertRaises(ValueError, r1.update, 1, 0)
        self.assertRaises(ValueError, r1.update, 1, 0)
        self.assertRaises(ValueError, r1.update, 1, 1, -1)
        self.assertRaises(ValueError, r1.update, 1, 1, 1, -1)

    def test_update_k1_value(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 10/10\n")

    def test_update_k2_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/10\n")

    def test_update_k3_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20, height=5)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 10/10 - 20/5\n")

    def test_update_k4_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20, height=5, x=1)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/10 - 20/5\n")

    def test_update_k5_values(self):
        """Test display without coords
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(id=4, width=20, height=5, x=1, y=6)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (4) 1/6 - 20/5\n")

    def test_update_args_prio(self):
        """Test updates
        """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(10, 10, 10, 10)
            r1.update(5, id=4, width=20, height=5, x=1, y=6)
            print(r1)
            self.assertEqual(fake_out.getvalue(),
                             "[Rectangle] (5) 10/10 - 10/10\n")

    def test_cmp_dict(self):
        """Test compare dict return value
        """
        r1 = Rectangle(10, 10, 10, 10, 10)
        good_answer = {"id": 10, "width": 10, "height": 10, "x": 10, "y": 10}
        self.assertEqual(r1.to_dictionary(), good_answer)

    def test_cmp_dict2(self):
        """Test compare dict return value
        """
        r1 = Rectangle(10, 10, 0, 0, 5)
        good_answer = {"id": 5, "width": 10, "height": 10, "x": 0, "y": 0}
        self.assertEqual(r1.to_dictionary(), good_answer)

    def test_create(self):
        """Creates an instance with a dict
        """
        base = Rectangle(1, 1)
        first_ins = {'id': 89, 'width': 10, 'height': 4, "x": 1, "y": 1}
        my_rect = base.create(**first_ins)
        self.assertEqual(my_rect.id, 89)
        self.assertEqual(my_rect.width, 10)
        self.assertEqual(my_rect.height, 4)
        self.assertEqual(my_rect.x, 1)
        self.assertEqual(my_rect.y, 1)

if __name__ == '__main__':
    unittest.main()