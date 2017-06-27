from unittest import TestCase
from TankTeamFacts import TankTeamFacts

VALID_CHARACTERISTICS = ['Name',
                         'Mobility',
                         'Front',
                         'Side',
                         'Top',
                         'Weapon',
                         'Range',
                         'ROF',
                         'AT',
                         'Firepower']
VALID_VALUES = ['Panzer IV H',
                'Standard Tank',
                6,
                3,
                1,
                '7.5cm KwK40 gun',
                32,
                2,
                11,
                3]
EXPECTED = dict(zip(VALID_CHARACTERISTICS, VALID_VALUES))

class TestTankTeamFacts(TestCase):

    def setUp(self):
        print('\n***** executing {}'.format(self._testMethodName))

    def test_characteristics_pass(self):
        '''Characteristics should be valid.'''
        facts = TankTeamFacts('Panzer IV H')
        self.assertTrue(facts.characteristics is not None)

    def test_characteristics_fail(self):
        '''Characteristics should be invalid since key does not exist.'''
        facts = TankTeamFacts('Panzer IIII')
        self.assertTrue(facts.characteristics is None)

    def test_get_fact_valid(self):
        '''Actual results should equal expected unless some doofus like me changed the database.'''
        facts = TankTeamFacts('Panzer IV H')
        for name in VALID_CHARACTERISTICS:
            actual = facts.get_fact(name)
            self.assertEqual(actual, EXPECTED[name])

    def test_get_fact_not_exist(self):
        '''The key does not exist, so actual result should be None.'''
        facts = TankTeamFacts('Panzer IV H')
        name = 'arglebargle'
        actual = facts.get_fact(name)
        self.assertTrue(actual is None)

    def test_get_fact_not_equal(self):
        '''Check an incorrect comapred result.'''
        facts = TankTeamFacts('Panzer IV H')
        name = 'Firepower'
        actual = facts.get_fact(name)
        self.assertTrue(actual is not None)
        self.assertNotEqual(actual, EXPECTED[name]-1)

    def test_characteristics_query_fail(self):
        '''Characteristics is invalid, so get_fact should return None.'''
        facts = TankTeamFacts('Panzer IIII')
        name = 'Firepower'
        actual = facts.get_fact(name)
        self.assertTrue(actual is None)
