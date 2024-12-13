#!/usr/bin/env python3
"""utilities for github org client.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """test_access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception, expected_message):
        """test_access_nested_map_exception"""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """ Test case for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Test get_json with mocked requests.get"""
        mock_requests_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """ memoize decorator test case """

    def test_memoize(self):
        """Test the memoize decorator"""
        class TestClass:
            """Test class with a_method and a_property"""

            def a_method(self):
                """A simple method"""
                return 42

            @memoize
            def a_property(self):
                """A property decorated with memoize"""
                return self.a_method()

        test_instance = TestClass()

        with patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42

            custom_result_1 = test_instance.a_property
            custom_result_2 = test_instance.a_property

            self.assertEqual(custom_result_1, 42)
            self.assertEqual(custom_result_2, 42)
            mock_method.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ memoize decorator test case """

    def test_memoize(self):
        """Test the memoize decorator"""
        class TestClass:
            """Test class with a_method and a_property"""

            def a_method(self):
                """A simple method"""
                return 42

            @memoize
            def a_property(self):
                """A property decorated with memoize"""
                return self.a_method()

        self.test_instance = TestClass()

        with patch.object(self.test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42

            custom_result_1 = self.test_instance.a_property
            custom_result_2 = self.test_instance.a_property

            self.assertEqual(custom_result_1, 42)
            self.assertEqual(custom_result_2, 42)
            mock_method.assert_called_once()
