import psycopg2
import sys
import csv

def main():
    conn_string = "host='localhost' dbname='lab1' user='postgres' password='1'"

    print("Connecting to database\n    ->%s" % (conn_string))
   
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    print("Connected!\n")

    csvfile = open('./dataset.csv')
    csvreader = csv.reader(csvfile, delimiter=',')

    csvreader.__next__()

    for i in csvreader:
        query_string = """
            INSERT INTO data(credit_card, currency, catch_phrase, fda_ndc_code) VALUES (
                '{0}', '{1}', '{2}', '{3}');"""
        query = query_string.format(i[0], i[1], i[2], i[3])
        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
