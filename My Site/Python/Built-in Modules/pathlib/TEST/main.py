#------------------------------------------------------------------------
# concrete path
#------------------------------------------------------------------------
from pathlib import Path






# print( Path('test.json').samefile('test.json') )            # // -> True
# print( Path('test.json').samefile('new_file.txt') )          # // -> False


# print( Path('test.json').stat().st_nlink )        # // -> 4


config_dir = Path.cwd()/'../config'