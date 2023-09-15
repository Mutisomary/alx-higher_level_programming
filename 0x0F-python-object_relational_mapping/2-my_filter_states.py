#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    (username, password, database, statename) = (argv[1], argv[2],
                                                 argv[3], argv[4])

    # connect to the database
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    # create a cursor to interact with the database
    cursor = connection.cursor()
    # execute the SQL query
    query = ("SELECT * FROM states WHERE name = '{}'"
            "ORDER BY states.id ASC").format(statename)
    cursor.execute(query)
    # fetch the results
    results = cursor.fetchall()
    # process the results
    for row in results:
        print(row)
    # close cursor and connection
    cursor.close()
    connection.close()
