__author__ = 'far'
import sqlite3



# region DB auf


def dbauf():
    global conn, c
    conn = sqlite3.connect('t.db')
    c = conn.cursor()


dbauf()

# endregion

# region DB do
c.execute("drop table stocks")
c.execute('''create table stocks

(date text, trans text, symbol text,
qty real, price real)''')

# Insert a row of data
c.execute("""insert into stocks
          values ('2006-01-05','BUY','RHAT',100,35.14)""")

# Save (commit) the changes
conn.commit()
# endregion

# region DB zu

# We can also close the cursor if we are done with it
print("Ende")
c.close()
# endregion

