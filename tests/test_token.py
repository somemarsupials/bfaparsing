# -*- coding: utf-8 -*-

from unittest import TestCase
from bnfparsing.token import Token

NUM = 5
MASTER = 'master'
CHILD = 'child'

class TokenTestSuite(TestCase):

    def test_token_creation(self):
        """ Test the __init__ method. """
        token = Token(token_type=MASTER, text=MASTER)
        self.assertEqual(token.token_type, MASTER, 
            msg='token_type not intialised properly'
            )
        self.assertEqual(token.text, MASTER, 
            msg='text not initialised properly'
            )

    def test_child_addition(self):
        """ Test addition of children and links between the two. """
        master = Token(MASTER)
        child = Token(CHILD)
        master.add(child)
        self.assertEqual(master.children[0], child,
            msg='child not properly added to master'
            )
        self.assertEqual(child.parent, master, 
            msg='master not added as parent'
            )

    def test_value_literal(self):
        """ Test the value method of literals. """
        token = Token(text=MASTER)
        self.assertEqual(token.value(), MASTER,
            msg='value method failed for literal'
            )

    def test_value_master(self):
        """ Test the value method of tokens with children. """
        master = Token(MASTER)
        string = ''
        for index in range(NUM):
            master.add(Token(text=str(index)))
            string += str(index)
        self.assertEqual(master.value(), string,
            msg='value method failed for token with children'
            )

    def test_len(self):
        """ Test the __len__ method of tokens. """
        master = Token(text=MASTER)
        self.assertEqual(len(master), len(MASTER),
            msg='__len__ method failed'
            )

    def test_iteration_value(self):
        """ Test the __iter__ method, iterating over value. """
        master = Token(text=MASTER)
        string = ''.join(c for c in master)
        self.assertEqual(string, master.value(),
            msg='iteration did not produce the correct result'
            )

    def test_iteration_children(self):
        """ Test the iter_under method, iterating over children. """
        master = Token()
        for index in range(NUM):
            master.add(Token(index, str(index)))
        index = 0
        for child in master.iter_under():
            self.assertEqual(child.text, str(index),
                msg='iteration over children failed'
                )
            index += 1
    
    def test_bool(self):
        """ Test __bool__ method. """
        token = Token()
        self.assertFalse(token, msg='__bool__ failed for empty token')
        token = Token(MASTER)
        self.assertTrue(token, msg='__bool__ failed for token with type')
        token = Token(text=MASTER)
        self.assertTrue(token, msg='__bool__ failed for token with text')

