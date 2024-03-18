import unittest
from unittest.mock import patch, mock_open
from io import StringIO
from json_helper import *


class JsonHelperTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_read_json(self, mock_stdout):
        file_name = "data/super_smash_bros/link.json"

        expected = {
            "name": "Link",
            "neutral_special": "Bow and Arrows",
            "side_special": " Boomerang",
            "up_special": " Spin Attack",
            "down_special": "Remote Bomb",
            "final_smash": "Ancient Bow and Arrow"
        }
        actual = read_json(file_name)
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_read_all_json(self, mock_stdout):
        folder_name = "data/super_smash_bros/"

        expected = [{'down_special': 'F.L.U.D.D.',
          'final_smash': 'Mario Finale',
          'name': 'Mario',
          'neutral_special': 'Fireball',
          'side_special': 'Cape',
          'up_special': 'Super Jump Punch'
        },

         {'down_special': 'Remote Bomb',
          'final_smash': 'Ancient Bow and Arrow',
          'name': 'Link',
          'neutral_special': 'Bow and Arrows',
          'side_special': ' Boomerang',
          'up_special': ' Spin Attack'
        }]
        actual = read_all_json_files(folder_name)
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_pickle_barrel(self, mock_stdout):
        expected = {
            "name": "Link",
            "neutral_special": "Bow and Arrows",
            "side_special": " Boomerang",
            "up_special": " Spin Attack",
            "down_special": "Remote Bomb",
            "final_smash": "Ancient Bow and Arrow"
        }
        data_test_pickle = "data/tests/link.pickle"

        write_pickle(expected, data_test_pickle)
        actual = load_pickle(data_test_pickle)

        self.assertEqual(actual, expected)
