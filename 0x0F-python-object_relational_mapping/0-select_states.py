#!/usr/bin/python3
#   Write a script that lists all states from the database hbtn_0e_0_usa
import MySQLdb
from sys import argv

if __name__ = "__main__":
  db = MySQLdb.connect(host="localhost", port=3360, user=argv[1],
                       passwd=argv[2], db=argv[3]);

  curl = db.cursor();
  curl.execute("SELECT * FROM hbtn_0e_0_usa ORDER BY id ASC")
  rows = curl.fetchall()
  for row in rows:
      print(row)
  curl.close()
  db.close()
