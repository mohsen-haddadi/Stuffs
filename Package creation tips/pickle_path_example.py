from pathlib import Path

mypath = Path().absolute().parent / 'pickled variables.p' # each '.parent' goes one level up - vary as required
mypath = str(mypath)
print(mypath)

