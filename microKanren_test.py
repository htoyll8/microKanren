#!/usr/bin/env python
import unittest
from microKanren_test_programs import *

EMPTY_STATE = State([], 0)

class TestMicroKanren(unittest.TestCase):
    # second-set t1
    def test_t1(self):
        self.assertEqual(car(call_fresh(lambda q: eq(q, 5))(EMPTY_STATE)), ([(Variable(0), 5)], 1))

    # second-set t2
    def test_t2(self):
        self.assertEqual(cdr(call_fresh(lambda q: eq(q, 5))(EMPTY_STATE)), [])

    # second-set t
    def test_t3(self):
        self.assertEqual(car(a_and_b(EMPTY_STATE)), ([(Variable(1), 5), (Variable(0), 7)], 2))

    # second-set t3, take
    def test_t3_take(self):
        self.assertEqual(take(1, a_and_b(EMPTY_STATE)), (([(Variable(1), 5), (Variable(0), 7)], 2), []))

    # second-set t4
    def test_t4(self):
        self.assertEqual(car(cdr(a_and_b(EMPTY_STATE))), ([(Variable(1), 6), (Variable(0), 7)], 2))

    # second-set t5
    def test_t5(self):
        self.assertEqual(cdr(cdr(a_and_b(EMPTY_STATE))), [])

    # who cards
    def test_who_cards(self):
        self.assertEqual(take(1, call_fresh(lambda q: fives(q))(EMPTY_STATE)), (([(Variable(0), 5)], 1), []))

    # take 2 a-and-b stream
    def test_take_two_streams(self):
        self.assertEqual(take(2, a_and_b(EMPTY_STATE)), (([(Variable(1), 5), (Variable(0), 7)], 2), (([(Variable(1), 6), (Variable(0), 7)], 2), [])))

    # take-all a-and-b stream
    def test_take_all_streams(self):
        self.assertEqual(a_and_b(EMPTY_STATE), (([(Variable(1), 5), (Variable(0), 7)], 2), (([(Variable(1), 6), (Variable(0), 7)], 2), [])))

    # ground appendo
    def test_ground_appendo(self):
        pass

    # ground appendo2
    def test_ground_appendo2(self):
        pass

    def test_many_non_ans(self):
        self.assertEqual(take(1, many_non_ans(EMPTY_STATE)), (([(Variable(0), 3)], 1), []))

if __name__ == '__main__':
    unittest.main()

