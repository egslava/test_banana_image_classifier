import unittest
from model import Model


class OnnxTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = Model()

    def test_all(self):
        cases = (
            (0, 'tests/n01440764_tench.jpeg'),
            (35, 'tests/n01667114_mud_turtle.JPEG')
        )

        for target, path in cases:
            with self.subTest(path):
                pred = self.model.predict(path)
                self.assertEqual(target, pred)
