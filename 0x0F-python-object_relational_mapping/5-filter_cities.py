#!/usr/bin/python3
""" lists all cities from hbtn_0e_4_usa """
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    conn = mysql.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON \
cities.state_id=states.id WHERE states.name=%(state)s ORDER BY cities.id \
ASC", {'state': sys.argv[4]})
    query_rows = cur.fetchall()
    for i in range(len(query_rows)):
        print(query_rows[i][0], end="\n" if i == len(query_rows) - 1 else ", ")
    cur.close()
    conn.close()
