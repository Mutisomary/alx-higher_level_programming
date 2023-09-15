#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database = argv[1], argv[2], argv[3]
    statename = argv[4]

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
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
        ORDER BY states.id ASC
    """
    cursor.execute(query, (statename,))
    # fetch the results
    results = cursor.fetchall()
    # process the results
    for row in results:
        print(row)
    # close cursor and connection
    cursor.close()
    connection.close()
