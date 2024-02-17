# Tests file
from unittest import TestCase, main
from main import add_message


class CalculatorTest(TestCase):
    def test_1(self):
        self.assertEqual(add_message(50000, 15, 2.5), 72414.92)

    def test_2(self):
        self.assertEqual(add_message(50000, 51, 2.5), 50000)

    def test_3(self):
        self.assertEqual(add_message(50000, 51, 101.0), 50000)

    def test_4(self):
        self.assertEqual(add_message(100000001, 51, 101.0), 100000001)

    def test_5(self):
        self.assertEqual(add_message(100000001, 51, 101.0), 100000001)

    def test_6(self):
        self.assertEqual(add_message(1000000, 30, "Some Text"), 0)

    def test_7(self):
        self.assertEqual(add_message(1000000, "Some Text", 99), 0)

    def test_8(self):
        self.assertEqual(add_message("Some Text", 30, 99), 0)


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200


def test_add_message(app, client):
    res = client.get('/add_number')
    assert res.status_code == 405


def test_error(app, client):
    res = client.get('/error')
    assert res.status_code == 404


if __name__ == '__main__':
    main()
