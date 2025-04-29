import unittest
import importlib

class TestAssignmentOne(unittest.TestCase):
    def test_01(self):
        self.assertFalse(answers.answer_01)
    def test_02(self):
        self.assertEqual(answers.answer_02, 4)
    def test_03(self):
        self.assertEqual(answers.answer_03, 2)
    def test_04(self):
        self.assertEqual(answers.answer_04, 1)
    def test_05(self):
        answer_05 = answers.answer_05()
        self.assertIsInstance(answer_05, str)
        self.assertEqual(answer_05, "Hello, world!")

chapter_name = "簡介"
answers = importlib.import_module("answers")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print(f"您在「{chapter_name}」章節的 {number_of_test_runs} 道練習題中答對了 {number_of_successes} 題。")