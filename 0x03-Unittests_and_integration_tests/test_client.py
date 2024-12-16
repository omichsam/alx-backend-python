#!/usr/bin/env python3
""" client testing module
"""

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock, PropertyMock, Mock
from requests import HTTPError
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str,
                 expct_result: Dict, magic_mock: MagicMock) -> None:
        """Tests the `org` method."""

        magic_mock.return_value = MagicMock(return_value=expct_result)
        org_client = GithubOrgClient(org)

        result = org_client.org()

        magic_mock.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org))

        self.assertEqual(result, expct_result)

    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            org_client = GithubOrgClient("google")

            self.assertEqual(
                org_client._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 1,
                    "name": "Hamza",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/hamza",
                    "html_url": "https://github.com/google/hamza",
                    "created_at": "2024-01-10T00:00:00Z",
                    "updated_at": "2024-02-10T00:00:00Z",
                    "has_issues": True,
                    "forks": 10,
                    "default_branch": "master",
                },
                {
                    "id": 2,
                    "name": "abc",
                    "private": False,
                    "owner": {
                        "login": "abc",
                        "id": 2,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/abc",
                    "html_url": "https://github.com/google/abc",
                    "created_at": "2024-01-10T00:00:00Z",
                    "updated_at": "2024-02-10T00:00:00Z",
                    "has_issues": True,
                    "forks": 10,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            result = GithubOrgClient("google").public_repos()
            self.assertEqual(result, ["Hamza", "abc"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expct_result) -> None:
        """Tests the `has_license` method."""
        org_client = GithubOrgClient("google")
        result = org_client.has_license(repo, license_key)
        self.assertEqual(result, expct_result)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the `GithubOrgClient` class."""

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up the class fixtures."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for mocking requests.get"""
            route_payload = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload,
            }
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return Mock(**{'json.return_value': {}})

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        """Tears down the class fixtures."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
            )
