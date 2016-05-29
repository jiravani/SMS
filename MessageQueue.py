__author__   = "Justin Iravani"

import MySQLdb

source = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_data_raw")
target = MySQLdb.connect("7.194.99.103", "Justin", "justin", "mls_dw")

source_cursor = source.cursor()
target_cursor = target.cursor()

target_table = "some_table"

# target_cursor.execute("DELETE FROM %s WHERE 1=1;" % (target_table)) # empty table
# target_cursor.execute("ALTER TABLE %s AUTO_INCREMENT = 1;" % (target_table)) # reset auto_increment

source_cursor.execute("SELECT * FROM mls_dw.DiM_pOtAtO;")

results = source_cursor.fetchall()

for row in results:
    sql = """INSERT INTO `mls_dw`.`event_fact`
            (`event_id`,`prim_player_id`,`sec_player_id`,`prim_team_id`,`sec_team_id`,
             `date_id`,`time_id`,`event_type_id`,`game_id`)
            VALUES
            (%d,%d,%d,%d,%d,%d,%d,%d);""" % (row)
    print(sql)

    # try:
    #     # Execute the SQL command
    #
    #     target_cursor.execute(sql)
    #
    #     # Commit your changes in the database
    #     target.commit()
    #
    # except:
    #     # Rollback in case there is any error
    #     print "error"
    #     target.rollback()

source.close()
target.close()
