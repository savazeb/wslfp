import sqlite3


class Database:
    ip_table = "ip"
    port_table = "port"

    def __init__(self, filename):
        self.filename = filename
        try:
            self.connection = sqlite3.connect(self.filename)
        except sqlite3.Error as er:
            print(f"SQLite error {er}")

    def retrieve_last(self):
        cursor = self.connection.execute("select * from {} order by id desc limit 1".format(self.ip_table))
        return cursor.fetchone()

    def insert_new_ip(self, params):
        self.connection.execute(
            "insert into {} (ip, added_At, deleted_At) values (?, ? ,?)".format(self.ip_table), params
        )
        self.connection.commit()

    def ip_deleted(self, params):
        self.connection.execute("update {} set deleted_At = ? where id = ?".format(self.ip_table), params)
        self.connection.commit()

    def retrieve_ports(self):
        cursor = self.connection.execute("select * from {} order by id".format(self.port_table))
        return cursor.fetchall()

    def close(self):
        self.connection.close()
