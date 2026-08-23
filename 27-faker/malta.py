"""A Faker provider for Maltese names, addresses and phone numbers.

Faker ships an `mt_MT` locale, but the only provider implemented for it is
`vat_id()` -- names, addresses and phone numbers all fall back to `en_US`.
This provider fills that gap.
"""

from faker.providers import BaseProvider

#Constant as tuples

FIRST_NAMES_MALE = (
    'Joseph', 'Paul', 'Carmel', 'John', 'Emanuel', 'Anthony', 'Charles',
    'Alfred', 'Michael', 'Matthew', 'Luke', 'Karl', 'Kurt', 'Ryan',
    'Clayton', 'Mario', 'Christopher', 'Gabriel', 'Andrew', 'Daniel',
)

FIRST_NAMES_FEMALE = (
    'Maria', 'Carmela', 'Josephine', 'Doris', 'Rita', 'Antoinette',
    'Rebecca', 'Nicole', 'Sarah', 'Martina', 'Claire', 'Roberta',
    'Francesca', 'Simone', 'Marthese', 'Graziella', 'Elena', 'Julia',
)

SURNAMES = (
    'Borg', 'Camilleri', 'Vella', 'Farrugia', 'Zammit', 'Galea', 'Micallef',
    'Grech', 'Attard', 'Spiteri', 'Azzopardi', 'Sammut', 'Cassar', 'Fenech',
    'Gauci', 'Mifsud', 'Muscat', 'Caruana', 'Bugeja', 'Schembri', 'Abela',
    'Debono', 'Bonnici', 'Calleja', 'Aquilina', 'Pace', 'Agius', 'Scicluna',
    'Cutajar', 'Falzon', 'Xuereb', 'Buttigieg', 'Ellul', 'Portelli', 'Said',
    'Tabone', 'Bartolo', 'Magri', 'Mallia', 'Cauchi', 'Curmi', 'Dalli',
)

# Maltese houses are named rather than numbered, mixing Maltese, Italian,
# English and devotional names.
HOUSE_NAMES = (
    'Dar il-Ħena', 'Il-Ġawhra', 'Ta\' Rżejjen', 'Dar il-Kalma', 'Il-Bebbuxu',
    'Villa Rosa', 'Casa Mia', 'Bellavista', 'Villa Carmen', 'Casa Bianca',
    'St Rita', 'Santa Marija', 'Lourdes', 'Nazareth', 'Fatima', 'San Ġużepp',
    'Sunny Side', 'Sea Breeze', 'The Nest', 'Hillcrest', 'Rose Cottage',
    'Serenity', 'Mariposa', 'Buena Vista', 'Shalom', 'Sunrise',
)

# Real street names, kept as literals: the Maltese definite article assimilates
# to the following consonant (il-/ir-/is-/it-/id-/in-/iz-/ix-), so composing
# them from parts would produce wrong forms.
STREETS = (
    'Triq il-Kbira', 'Triq ir-Repubblika', 'Triq il-Knisja', 'Triq il-Wied',
    'Triq id-Dejqa', 'Triq il-Baħar', 'Triq il-Ġnien', 'Triq il-Mitħna',
    'Triq il-Fjuri', 'Triq il-Kappillan', 'Triq il-Karmnu', 'Triq il-Vitorja',
    'Triq San Pawl', 'Triq San Ġużepp', 'Triq Sant\' Antnin', 'Triq Santa Luċija',
    'Triq San Ġwann', 'Triq il-Mediterran', 'Triq il-Qaliet', 'Triq l-Imdina',
    'Vjal ir-Riżorġiment', 'Vjal l-Indipendenza', 'Sqaq il-Ħorr', 'Triq il-Kastell',
)

# The 68 localities of Malta and Gozo.
LOCALITIES = (
    'Attard', 'Balzan', 'Birgu', 'Birkirkara', 'Birżebbuġa', 'Bormla',
    'Dingli', 'Fgura', 'Floriana', 'Fontana', 'Għajnsielem', 'Għarb',
    'Għargħur', 'Għasri', 'Għaxaq', 'Gudja', 'Gżira', 'Ħamrun', 'Iklin',
    'Kalkara', 'Kerċem', 'Kirkop', 'Lija', 'Luqa', 'Marsa', 'Marsaskala',
    'Marsaxlokk', 'Mdina', 'Mellieħa', 'Mġarr', 'Mosta', 'Mqabba', 'Msida',
    'Mtarfa', 'Munxar', 'Nadur', 'Naxxar', 'Paola', 'Pembroke', 'Pietà',
    'Qala', 'Qormi', 'Qrendi', 'Rabat', 'Safi', 'San Ġiljan', 'San Ġwann',
    'San Lawrenz', 'San Pawl il-Baħar', 'Sannat', 'Santa Luċija',
    'Santa Venera', 'Senglea', 'Siġġiewi', 'Sliema', 'Swieqi', 'Ta\' Xbiex',
    'Tarxien', 'Valletta', 'Victoria', 'Xagħra', 'Xewkija', 'Xgħajra',
    'Żabbar', 'Żebbuġ', 'Żejtun', 'Żurrieq',
)

MOBILE_PREFIXES = ('77', '79', '98', '99')
LANDLINE_PREFIXES = ('21', '22', '23', '25', '27')


class MaltaProvider(BaseProvider):
    """Maltese person and address details."""

    def first_name(self) -> str:
        return self.random_element(FIRST_NAMES_MALE + FIRST_NAMES_FEMALE)

    def first_name_male(self) -> str:
        return self.random_element(FIRST_NAMES_MALE)

    def first_name_female(self) -> str:
        return self.random_element(FIRST_NAMES_FEMALE)

    def last_name(self) -> str:
        return self.random_element(SURNAMES)

    def house_name(self) -> str:
        return self.random_element(HOUSE_NAMES)

    def flat(self) -> str:
        """A flat within a named block, e.g. 'Flat 4, Sunrise Court'."""
        return f'Flat {self.random_int(1, 12)}, {self.random_element(HOUSE_NAMES)}'

    def street_name(self) -> str:
        return self.random_element(STREETS)

    def city(self) -> str:
        return self.random_element(LOCALITIES)

    def mobile_number(self) -> str:
        return f'+356 {self.random_element(MOBILE_PREFIXES)}{self.numerify("## ####")}'

    def landline_number(self) -> str:
        return f'+356 {self.random_element(LANDLINE_PREFIXES)}{self.numerify("## ####")}'

    def phone_number(self) -> str:
        """Mobile roughly three times out of four, as in the real register."""
        if self.random_int(1, 4) == 1:
            return self.landline_number()

        return self.mobile_number()
