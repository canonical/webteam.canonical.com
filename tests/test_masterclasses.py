import unittest
from webapp.masterclasses import _has_row_value


class TestMasterclassesApp(unittest.TestCase):
    def test_has_row_value_return_true(self):
        row = {
            "values": [
                {
                    "userEnteredValue": {
                        "stringValue": "Redis",
                    },
                    "effectiveValue": {
                        "stringValue": "Redis",
                    },
                    "formattedValue": "Redis",
                }
            ]
        }
        self.assertTrue(_has_row_value(row))

    def test_has_row_value_return_false(self):
        row = {
            "userEnteredFormat": {"hyperlinkDisplayType": "LINKED"},
        }
        self.assertFalse(_has_row_value(row))
