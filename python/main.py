import os
import time
from datetime import datetime

from lib.command import CMD
from lib.config import *
from lib.database import Database

db_path = f"{os.path.expanduser('~')}/wslfp"
db = Database(f"{db_path}/wslfp.db")

def execute(command, args=None, read=False):
    return os.popen(command % args if args else command).read()


def get_wsl_ip():
    return execute(CMD.WSL_IP, read=True)


def get_portproxy_list():
    return execute(CMD.PORTPROXY_LIST, read=True)


def main():
    print(INTRO)
    time.sleep(2)

    ports = db.retrieve_ports()
    try:
        last_id, last_ip, _, deleted = db.retrieve_last()
        if not deleted:
            print("delete last ip section")
            for port in ports:
                print(f"deleting port proxy for ip {last_ip} at port {port[0]}")
                execute(CMD.PORTPROXY_DELETE.format(port[0], PLACEHOLDER_IP))
            db.ip_deleted((datetime.today(), last_id))
            print("deleted succesfully")

    except:
        print("no section found...\n\r starting new port proxy section")

    wsl_ip = get_wsl_ip()[:-1]
    for port in ports:
        print(f"generating port proxy for ip {str(wsl_ip)} at port {port[0]}")
        execute(CMD.PORTPROXY_ADD.format(port[0], PLACEHOLDER_IP, port[0], wsl_ip))
        time.sleep(0.05)

    print("finishing database...")
    db.insert_new_ip((wsl_ip, datetime.today(), None))
    time.sleep(2)

    print("portproxy finished succesfully")


if __name__ == "__main__":
    main()
