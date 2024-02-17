#!/usr/bin/python3
"""To List all states from database hbtn_0e_0_usa"""
import sys
import MySQLdb
if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name = %s ORDER BY\
           states.id ASC".format(sys.argv[4])
    cur.execute(sql)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
