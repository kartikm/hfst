import hfst

import os.path
assert os.path.isfile('streets.txt')
defs = hfst.compile_pmatch_file('streets.txt')
cont = hfst.PmatchContainer(defs)
assert cont.match("Je marche seul dans l'avenue des Ternes.") == "Je marche seul dans l'<FrenchStreetName>avenue des Ternes</FrenchStreetName>."

nonexistent_file = 'foofoofoofoofoofoofoofoofoofoofoofoo'

assert not os.path.isfile(nonexistent_file)
try:
    hfst.compile_pmatch_file(nonexistent_file)
    assert False
except IOError as e:
    pass
