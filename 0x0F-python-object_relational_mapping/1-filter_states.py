#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id")
    query_r = cur.fetchall()
    for r in query_r:
        print(r)
    cur.close()
    db.close()
