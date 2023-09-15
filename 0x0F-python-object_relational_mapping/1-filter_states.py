#!/usr/bin/python3

"""
lists all states with a name starting with N from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]

    # connect to the database
    connection = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            port=3306,
            db=database
    )
    # create a cursor to interact with the database
    cursor = connection.cursor()
    # execute the query
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    # fecth the results
    results = cursor.fetchall()
    # process the results
    for row in results:
        print(row)
    # close cursor and connection
    cursor.close()
    connection.close()
