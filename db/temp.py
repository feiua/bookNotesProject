import sqlite3, os

# Connect to the database
folder_dir = os.path.abspath(os.path.dirname(__file__))
folder_dir = folder_dir.replace('\\', '/')
database_path = '{database_folder}/{database_name}'.\
    format(database_folder=folder_dir, database_name='data/mydatabase.db')

conn = sqlite3.connect(database_path)
c = conn.cursor()

# Drop the table
c.execute("DROP TABLE {table_name};".format(table_name="notebook_table"))

# Commit the changes
conn.commit()

# Close the connection
conn.close()