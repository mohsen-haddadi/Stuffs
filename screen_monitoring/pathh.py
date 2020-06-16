from pathlib import Path

mypath = Path().absolute().parent.parent  # each '.parent' goes one level up - vary as required
print(mypath)