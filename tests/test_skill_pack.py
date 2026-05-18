import unittest

from scripts.validate_skill_pack import validate_all


class SkillPackValidationTest(unittest.TestCase):
    def test_skill_pack_contract(self):
        failures = validate_all()
        self.assertEqual([], failures)


if __name__ == "__main__":
    unittest.main()
