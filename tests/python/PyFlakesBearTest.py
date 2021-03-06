from bears.python.PyFlakesBear import PyFlakesBear
from tests.LocalBearTestHelper import verify_local_bear

good_file = """
print("Hi")
"""

bad_file = """
import os
print("Hi")
"""

PyFlakesBear = verify_local_bear(PyFlakesBear,
                                 valid_files=(good_file,),
                                 invalid_files=(bad_file,))
