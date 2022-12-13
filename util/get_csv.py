import csv
import os.path


def read_csv_Data():
    rr = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"data.csv")),fieldnames=['data','value'])
    return rr
