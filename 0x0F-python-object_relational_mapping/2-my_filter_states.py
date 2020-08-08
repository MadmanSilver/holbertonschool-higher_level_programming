#!/usr/bin/python3
""" lists all states that start with N from hbtn_0e_0_usa """
import MySQLdb as mysql
import sys

if __name__ == "__main__":
    conn = mysql.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE BINARY "{}" ORDER BY id \
ASC'.format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
