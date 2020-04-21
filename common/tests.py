from django.test import TestCase
from common.utils import compare_version


class UserScoreTestCase(TestCase):
    def setUp(self):
        self.expected_data = [
            ["0.1", "1.1", -1],
            ["1.0.1", "1", 1],
            ["7.5.2.4", "7.5.3", -1],
            ["1.01", "1.001", 0],
            ["1.0", "1.0.0", 0]

        ]

    def test_version_compare(self):
        for expected in self.expected_data:
            v1 = expected[0]
            v2 = expected[1]
            result = expected[2]
            print(v1, v2, result)
            self.assertEqual(compare_version(v1, v2), result, msg="v1:{} v2:{} expected:{}".format(v1, v2, result))
