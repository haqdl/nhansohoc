import gettext
import logging
import math
import datetime
from collections import Counter
from operator import truediv
from typing import Dict, Optional, Tuple, List

from .common import Functions as fct
from .interpretations import Interpretations

default_lang = "en"
# try:
#    locale_lang, encoding = locale.getlocale()
#    lang = locale_lang.split("_")[0] if locale_lang else default_lang
#except:
#    # If unable to get the locale language, use English
#    lang = default_lang
#try:
#    language = gettext.translation('numerology', localedir='locale', languages=[lang])
#except:
#    # If the current language does not have a translation, the default laguage (English) will be used English
#    language = gettext.translation('numerology', localedir='locale', languages=[default_lang])
#language.install()
#_ = language.gettext


class Numerology:
    """Numerology is the science of numbers. It is the study of the numerical value of the letters in words, names, dates, and ideas.

    Pythagoras, the Greek mathematician and philosopher who lived from 569–470 B.C.,
    began his theory of numbers by discovering the numerical relationship between numbers and musical notes.

    Then he studied numerology from Egytians priests and is now known as the father of Western numerology.

    This class is mainly based on the calculation methods from the book "ABC de la Numérologie" of Jean-Daniel FERMIER.
    """

    alphabet = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 1,
        "k": 2,
        "l": 3,
        "m": 4,
        "n": 5,
        "o": 6,
        "p": 7,
        "q": 8,
        "r": 9,
        "s": 1,
        "t": 2,
        "u": 3,
        "v": 4,
        "w": 5,
        "x": 6,
        "y": 7,
        "z": 8,
    }

    vowels = ("a", "e", "i", "o", "u")

    consonants = (
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "z",
    )

    _key_figures = {}

    first_name: str
    last_name: str
    birthdate: str

    first_name_num: str
    last_name_num: str
    birthdate_num: str

    first_name_is_valid: bool = False
    last_name_is_valid: bool = False
    birthdate_is_valid: bool = False
    names_are_valid: bool = False

    verbose = True

    def __init__(
        self,
        first_name: str,
        last_name: str,
        birthdate: Optional[str] = None,
        verbose: bool = True,
    ):
        self.first_name = first_name.strip()
        self.last_name = last_name.strip()
        self.birthdate = birthdate
        self.verbose = verbose

        self.check_parameters()
        if self.names_are_valid:
            self.init_inner_variables()
            self.set_key_figures()
            self._interpretations = Interpretations(key_figures=self.key_figures)

        if self.verbose and self.names_are_valid:
            print("KEY FIGURES:")
            fct.print_beautiful_dict(dictionary=self.key_figures)
            print("INTERPRETATIONS:")
            fct.print_beautiful_dict(dictionary=self.interpretations)

    # CLASSMETHODS

    @classmethod
    def get_numerology_sum(
        cls, tuple_obj: Tuple[int], upper_bound: int = 9, master_number: bool = True
    ) -> int:
        """Make the numerology sum of the itarable (here, tuples) in parameter.
        The numerology sum is the sum of every digit in a number.
        The result is sum again if it is greater than 9 unless it's a multiple of 11.

        Args:
            tuple_obj (Tuple[int]): Tuple to sum up
            upper_bound (int, optional): Upper bound of the recursivess. Defaults to 9.
            master_number (bool, optional): If `master_number` is False, the multiple of 11 are not taken into account. Defaults to True.

        Returns:
            int: [description]
        """
        sum = math.fsum(tuple_obj)

        if master_number:
            while not (sum <= upper_bound or (sum % 11) == 0):
                sum = math.fsum(tuple(int(num) for num in str(int(sum))))
        else:
            while not (sum <= upper_bound):
                sum = math.fsum(tuple(int(num) for num in str(int(sum))))

        return int(sum)

    # INIT METHODS

    def is_vowel(self, pos: int) -> bool:        
        """Van dang con tranh cai."""
        y_is_consonant = False
        full_name = self.first_name + " " + self.last_name
        
        letter = full_name[pos]
        if letter == "y" and len(full_name) > 1:
            if pos == len(full_name) - 1 and full_name[pos-1] in self.vowels:                
                y_is_consonant = True
            if pos == 0 and full_name[pos+1] in self.vowels:
                y_is_consonant = True
            if (0 < pos < len(full_name) -2) and (full_name[pos-1] in self.vowels or full_name[pos+1] in self.vowels):
                y_is_consonant = True
        
        return full_name[pos] in self.vowels or not y_is_consonant


    def check_parameters(self):
        self.check_first_name()
        self.check_last_name()

        if self.first_name_is_valid and self.last_name_is_valid:
            self.names_are_valid = True
            self.check_birthdate()
        else:
            logging.warning("Invalid names supplied.")
            print("Invalid names supplied.")

    def check_first_name(self):
        """Check if the first name supplied contains at least one letter of the alphabet."""
        if fct.keep_valid_letters(self.first_name, self.alphabet):
            self.first_name_is_valid = True

    def check_last_name(self):
        """Check if the last name supplied contains at least one letter of the alphabet."""
        if fct.keep_valid_letters(self.last_name, self.alphabet):
            self.last_name_is_valid = True

    def check_birthdate(self):
        """Check if the birthdate supplied is a valid date."""
        if self.birthdate and fct.is_valid_date(self.birthdate):
            self.birthdate_is_valid = True

    def init_inner_variables(self):
        """Initializes the inner variables of the class as cleaned version of names, etc."""
        # first_name is the first name as supplied by the user.
        # first_name_cleaned is the clean version of the first_name : lower case, accents removed, only alphabet letters kept.
        # first_name_num is the matching numbers of first_name_cleaned.
        # Same for last_name.

        # Initialize the variables - Set the names and birthdate and their matching numbers.
        self.first_name_cleaned = fct.keep_valid_letters(self.first_name, self.alphabet)
        self.last_name_cleaned = fct.keep_valid_letters(self.last_name, self.alphabet)

        self.first_name_num = fct.match_numbers_to_letters(
            self.first_name_cleaned, self.alphabet
        )
        self.last_name_num = fct.match_numbers_to_letters(
            self.last_name_cleaned, self.alphabet
        )

        if self.birthdate_is_valid:
            self.birthdate_year = int(self.birthdate.split("-")[0])
            self.birthdate_month = int(self.birthdate.split("-")[1])
            self.birthdate_day = int(self.birthdate.split("-")[2])

    def set_key_figures(self):
        """Initializes the key figures dictionnary."""

        # First name and last name elements
        if self.names_are_valid:
            # Setting the key figures
            self._key_figures["first_name"] = self.first_name
            self._key_figures["last_name"] = self.last_name
            # Hearth Desire Number (vowels) = Nombre intime (voyelles)
            self._key_figures["hearth_desire_number"] = self.hearth_desire_number
            # Personality Number (consonants) = Nombre de réalisation (consonnes)
            self._key_figures["personality_number"] = self.personality_number
            # Destiny Number (full name) = Nombre d'expression (nom complet)
            self._key_figures["destiny_number"] = self.destiny_number
            self._key_figures["expression_number"] = self.destiny_number
            # Active Number (first name) = Nombre actif (prénom)
            self._key_figures["active_number"] = self.active_number
            # Legacy Number (last name) = Nombre héréditaire (nom de famille)
            self._key_figures["legacy_number"] = self.legacy_number
            self._key_figures["full_name_numbers"] = self.full_name_numbers
            self._key_figures[
                "full_name_missing_numbers"
            ] = list(self.full_name_missing_numbers)
            self._key_figures["passion_numbers"] = list(self.passion_numbers)


        # Birthdate elements (as birthdate is optional)
        if self.birthdate_is_valid:
            self._key_figures["birthdate"] = self.birthdate
            self._key_figures["birthdate_day"] = self.birthdate_day
            self._key_figures["birthdate_month"] = self.birthdate_month
            self._key_figures["birthdate_year"] = self.birthdate_year

            self._key_figures["life_path_number"] = self.life_path_number
            self._key_figures[
                "life_path_number_alternative"
            ] = self.life_path_number_alternative
            self._key_figures["birthdate_day_num"] = self.birthdate_day_num
            self._key_figures["birthdate_day_num_alt"] = self.birthdate_day_num_alt
            self._key_figures["birthdate_month_num"] = self.birthdate_month_num
            self._key_figures["birthdate_month_num_alt"] = self.birthdate_month_num_alt
            self._key_figures["birthdate_year_num"] = self.birthdate_year_num
            self._key_figures["birthdate_year_num_alt"] = self.birthdate_year_num_alt
            self._key_figures[
                "birthdate_year_num_alternative"
            ] = self.birthdate_year_num_alternative
            self._key_figures["power_number"] = self.power_number
            self._key_figures[
                "power_number_alternative"
            ] = self.power_number_alternative
            self._key_figures["attitude_number"] = self.attitude_number
            self._key_figures["challenge_numbers"] = list(self.challenge_numbers)
            self._key_figures["pyramid_numbers"] = list(self.pyramid_numbers)
            self._key_figures["pyramid_ages"] = list(self.pyramid_ages)
            self._key_figures["fortune_curr_year_number"] = self.fortune_curr_year_number
            self._key_figures["fortune_next_1_year_number"] = self.fortune_next_1_year_number
            self._key_figures["fortune_next_2_year_number"] = self.fortune_next_2_year_number 
            self._key_figures["fortune_next_3_year_number"] = self.fortune_next_3_year_number 


    # PROPERTIES
    @property
    def key_figures(self) -> Dict[str, int]:
        """Returns the keys figures in a dictionnary."""
        return self._key_figures

    @property
    def interpretations(self) -> Dict:
        return self._interpretations.meanings

    @property
    def life_path_number(self) -> int:
        """Returns the Life Path Number.

        The life path number is the most important one in a numerology chart.
        It describes the direction of your life journey.
        It offers insight into the skills and traits you may possess and the kinds of challenges you can expect to face in your life.
        It is calculated from the birth date.

        This method sums-reduces to one digit the date, month, and year before summing-reducing their total.
        The alternative method `life_path_number_alternative` sums-reduces to one digit the total of day, month, and year from the birthdate.

        Returns:
            int: Life Path Number (Initial method).
        """
        if self.birthdate:
            return self.get_numerology_sum(
                        (self.birthdate_day_num, self.birthdate_month_num, self.birthdate_year_num), 
                        master_number=True
                    )

    @property
    def life_path_number_alternative(self) -> int:
        """Returns the Life Path Number (alternative method).

        The life path number is the most important one in a numerology chart.
        It describes the direction of your life journey.
        It offers insight into the skills and traits you may possess and the kinds of challenges you can expect to face in your life.
        It is calculated from the birth date.

        The initial method sums-reduces to one digit the date, month, and year before summing-reducing their total.
        This alternative method `life_path_number_alternative` sums-reduces to one digit the total of day, month, and year from the birthdate.

        Returns:
            int: Life Path Number (Alternative method)
        """
        sum = self.birthdate_day + self.birthdate_month + self.birthdate_year
        return self.get_numerology_sum(fct.int_to_tuple(sum), master_number=True)

    @property
    def destiny_number(self) -> int:
        """Returns the Destiny Number.

        Sometimes called Expression Number or Lucky Number, it indicates the personal interest, unique capabilities and talents.
        ***NOTES: current method have some different with standard method
        Returns:
            int: Destiny number.
        """
        # active_number = self.get_numerology_sum(
        #     self.first_name_num, master_number=True
        # )
        # legacy_number = self.get_numerology_sum(self.last_name_num, master_number=True)
        # return self.get_numerology_sum(
        #     (active_number, legacy_number), master_number=True
        # )
        full_name_destiny = self.first_name.strip() + ' ' + self.last_name.strip()
        full_name_arr = full_name_destiny.split()
        name_num_arr = []
        for word in full_name_arr:
            clean_word = fct.keep_valid_letters(word, self.alphabet)
            word_num = self.get_numerology_sum(
                            fct.match_numbers_to_letters(clean_word, self.alphabet),
                            master_number=True
                        )
            name_num_arr.append(word_num)

        return self.get_numerology_sum(tuple(name_num_arr), master_number=True)


    @property
    def power_number(self) -> int:
        """Returns the Power Number

        The power number is obtained by adding together the life path number and destiny number. Then reduce the number to a single digit.

        Returns:
            int: [description]
        """
        return self.get_numerology_sum(
            (self.life_path_number, self.destiny_number),
            master_number=True,
        )

    @property
    def power_number_alternative(self) -> int:
        """Returns the Power Number (Alternative)

        The power number is obtained by adding together the life path number (alternative) and destiny number. Then reduce the number to a single digit.

        Returns:
            int: [description]
        """
        return self.get_numerology_sum(
            (self.life_path_number_alternative, self.destiny_number),
            master_number=False,
        )

    @property
    def personality_number(self) -> int:
        """Returns the Personality Number.

        Sometimes called the Inner Dream Number, the Personnality Number indicates our external personality.
        It is calculated from the consonants in the full name.

        Returns:
            int: Inner Dream Number.
        """
        consonants_in_name = [
                letter
                for letter in (self.first_name_cleaned + self.last_name_cleaned)
                if letter in self.consonants
        ]
        full_name = self.first_name + " " + self.last_name
        for idx, letter in enumerate(full_name):            
            if letter == "y" and not self.is_vowel(idx):
                consonants_in_name.append(letter)
            
        consonants_in_name_num = fct.match_numbers_to_letters(consonants_in_name, self.alphabet)
        # consonants_in_name_num = fct.match_numbers_to_letters(
        #     (
        #         letter
        #         for letter in (self.first_name_cleaned + self.last_name_cleaned)
        #         if letter in self.consonants
        #     ),
        #     self.alphabet,
        # )
        ret_num = self.get_numerology_sum(consonants_in_name_num)         
        return ret_num if ret_num <= 22 else self.get_numerology_sum(fct.int_to_tuple(ret_num)) 

    @property
    def hearth_desire_number(self) -> int:
        """Returns the Hearth Desire Number.

        Sometimes called the Soul Urge Number, the Hearth Desire Number describes the inner ressources.
        It is calculated from the vowels in the full name.

        Returns:
            int: Hearth Desire Number.
        """
       
        vowels_in_name = [
                letter
                for letter in (self.first_name_cleaned + self.last_name_cleaned)
                if letter in self.vowels
        ]
        full_name = self.first_name + " " + self.last_name
        for idx, letter in enumerate(full_name):            
            if letter == "y" and self.is_vowel(idx):
                 vowels_in_name.append(letter)

        vowels_in_name_num = fct.match_numbers_to_letters(vowels_in_name, self.alphabet)

        # vowels_in_name_num = fct.match_numbers_to_letters(
        #     (
        #         letter
        #         for letter in (self.first_name_cleaned + self.last_name_cleaned)
        #         if letter in self.vowels
        #     ),
        #     self.alphabet,
        # )
        ret_num = self.get_numerology_sum(vowels_in_name_num)        
        return ret_num if ret_num <= 22 else self.get_numerology_sum(fct.int_to_tuple(ret_num)) 


    @property
    def active_number(self) -> int:
        """Returns the Active Number.

        The number from your first name.

        Returns:
            int: The Active Number
        """
        ret_num = self.get_numerology_sum(self.first_name_num, master_number=True)
        return ret_num if ret_num <= 22 else self.get_numerology_sum(fct.int_to_tuple(ret_num)) 


    @property
    def legacy_number(self) -> int:
        """Returns the Legacy Number.

        The number from your last name.

        Returns:
            int: The legacy number
        """
        ret_num = self.get_numerology_sum(self.last_name_num, master_number=True)
        return ret_num if ret_num <= 22 else self.get_numerology_sum(fct.int_to_tuple(ret_num)) 


    @property
    def full_name_numbers(self) -> Dict[int, int]:
        """Returns the numbers from the full name as a dict(Counter).

        The dict contains the numbers and their occurrences."""
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = fct.match_numbers_to_letters(full_name, self.alphabet)
        full_name_counter = Counter(full_name_num).most_common()
        full_name_counter_dict = dict(full_name_counter)
        return full_name_counter_dict


    @property
    def passion_numbers(self) -> Tuple:
        """Returns the most count numbers from the full name as a dict(Counter).

        The dict contains the numbers and their occurrences."""
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = fct.match_numbers_to_letters(full_name, self.alphabet)
        full_name_counter = Counter(full_name_num).most_common()
        full_name_counter_dict = dict(full_name_counter)
        most_common_num = max([val for val in full_name_counter_dict.values()])
        most_common_dict = [int(key) for key, val in full_name_counter_dict.items() if val == most_common_num]
        return tuple(most_common_dict)

    @property
    def full_name_missing_numbers(self) -> Tuple:
        """Returns the missing numbers from the name as a tuple."""
        full_name = self.first_name_cleaned + self.last_name_cleaned
        full_name_num = fct.match_numbers_to_letters(full_name, self.alphabet)
        return tuple([number for number in range(1, 10) if number not in full_name_num])

    @property
    def birthdate_day_num(self) -> int:
        """Returns the numerology sum of the birthday day.

        Example: The 27 in 1986-03-27 will give 9."""
        return self.get_numerology_sum(
            (0, self.birthdate_day), master_number=True
        )

    @property
    def birthdate_day_num_alt(self) -> int:
        """Returns the numerology sum-reduce of the birthday day.

        Example: The 27 in 1986-03-27 will give 9."""
        return self.get_numerology_sum(
            (0, self.birthdate_day), master_number=False
        )        

    @property
    def birthdate_month_num(self) -> int:
        """Returns the numerology sum of the birthday month.

        Example: The 12 in 1986-12-27 will give 3."""
        return self.get_numerology_sum(
            (0, self.birthdate_month), master_number=True
        ) 

    @property
    def birthdate_month_num_alt(self) -> int:
        """Returns the numerology sum-reduce of the birthday month.

        Example: The 12 in 1986-12-27 will give 3."""
        return self.get_numerology_sum(
            (0, self.birthdate_month), master_number=False
        )        

    @property
    def birthdate_year_num(self) -> int:
        """Returns the numerology sum of the birthday year.

        This method sums-reduces the 4 digits of the year.
        The alternative one sums-reduces the 2 last digits."""
        return self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_year), master_number=True
        )

    @property
    def birthdate_year_num_alt(self) -> int:
        """Returns the numerology sum of the birthday year.

        This method sums-reduces the 4 digits of the year.
        The alternative one sums-reduces the 2 last digits."""
        return self.get_numerology_sum(
            fct.int_to_tuple(self.birthdate_year), master_number=False
        )

    @property
    def birthdate_year_num_alternative(self) -> int:
        """Returns the numerology sum of the birthday year.

        The original method sums-reduces the 4 digits of the year (1958 > 23 > 5).
        This alternative one sums-reduces the 2 last digits ((19)58 > 13 > 4)."""
        birthday_year_truncate = fct.int_to_tuple(self.birthdate_year)[-2:]
        return self.get_numerology_sum(
            fct.int_to_tuple(birthday_year_truncate), master_number=True
        )


    @property
    def attitude_number(self) -> int:
        """Returns the numerology sum of the birthday day and month."""
        return self.get_numerology_sum(
            (self.birthdate_day_num, self.birthdate_month_num),
            master_number=True,
        )

    @property
    def challenge_numbers(self) -> tuple:
        """Returns 4 challenge numbers.

        Challenge #1: abs(birthday_day - birthday_month)
        Challenge #2: abs(birthday_day - birthday_year)
        Challenge #3: abs(#1 - #2)
        Challenge #4: abs(bitrhday_month - birthday_year)."""

        #calculate
        challenge_1 = abs(self.birthdate_day_num_alt - self.birthdate_month_num_alt)
        challenge_2 = abs(self.birthdate_day_num_alt - self.birthdate_year_num_alt)
        challenge_3 = abs(challenge_1 - challenge_2)
        challenge_4 = abs(self.birthdate_month_num_alt - self.birthdate_year_num_alt)

        return (challenge_1 , challenge_2, challenge_3, challenge_4)


    @property
    def pyramid_numbers(self) -> tuple:
        """Returns 4 top success numbers (pyramid).

        pyramid #1: sums-reduces of (birthday_day + birthday_month)
        pyramid #2: sums-reduces of (birthday_day + birthday_year)
        pyramid #3: (#1 + #2)
        pyramid #4: (bitrhday_month - bitrhday_year)."""

        pyr_1 = self.get_numerology_sum(
                    (self.birthdate_day_num_alt, self.birthdate_month_num_alt), 
                    master_number=False
                )
        pyr_2 =self.get_numerology_sum(
                    (self.birthdate_day_num_alt, self.birthdate_year_num_alt),
                    master_number=False
                )
        pyr_3 = self.get_numerology_sum(
                    (pyr_1, pyr_2),
                    upper_bound=11,
                    master_number=False
                )
        pyr_4 = self.get_numerology_sum(
                    (self.birthdate_month_num_alt, self.birthdate_year_num_alt),
                    upper_bound=11,
                    master_number=False
                )


        return pyr_1 , pyr_2, pyr_3, pyr_4        


    @property
    def pyramid_ages(self) -> tuple:
        """Returns age of 4 top success numbers (pyramid).

        https://tracuuthansohoc.com/kim-tu-thap-than-so-hoc/."""

        master_num = self.get_numerology_sum(
                    (0, self.life_path_number), 
                    upper_bound=11,
                    master_number=False
                )
        age_1 = 36 - master_num
        age_2 = age_1 + 9 
        age_3 = age_2 + 9 
        age_4 = age_3 + 9 


        return age_1, age_2, age_3, age_4  


    @property
    def fortune_curr_year_number(self) -> int:
        """Returns the numerology sum of the current year birthday."""
        todays_date = datetime.date.today()
        year_sum = self.get_numerology_sum(
            fct.int_to_tuple(todays_date.year), master_number=True
        )
        return self.get_numerology_sum(
            (self.birthdate_day_num, self.birthdate_month_num, year_sum), 
            master_number=False
        )


    @property
    def fortune_next_1_year_number(self) -> int:
        """Returns the numerology sum of the next year birthday."""
        todays_date = datetime.date.today()
        year_sum = self.get_numerology_sum(
            fct.int_to_tuple(todays_date.year + 1), master_number=True
        )
        return self.get_numerology_sum(
            (self.birthdate_day_num, self.birthdate_month_num, year_sum), 
            master_number=False
        )

    @property
    def fortune_next_2_year_number(self) -> int:
        """Returns the numerology sum of the next 2 years birthday."""
        todays_date = datetime.date.today()
        year_sum = self.get_numerology_sum(
            fct.int_to_tuple(todays_date.year + 2), master_number=True
        )
        return self.get_numerology_sum(
            (self.birthdate_day_num, self.birthdate_month_num, year_sum), 
            master_number=False
        )


    @property
    def fortune_next_3_year_number(self) -> int:
        """Returns the numerology sum of the next 3 years birthday."""
        todays_date = datetime.date.today()
        year_sum = self.get_numerology_sum(
            fct.int_to_tuple(todays_date.year + 3), master_number=True
        )
        return self.get_numerology_sum(
            (self.birthdate_day_num, self.birthdate_month_num, year_sum), 
            master_number=False
        )        


    @property
    def key_figures(self) -> Dict:
        return self._key_figures
