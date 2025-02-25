import sqlite3
conobj = sqlite3.connect('M18.db')
print(conobj)
curobj = conobj.cursor()
print(curobj)