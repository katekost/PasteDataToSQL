import psycopg2
import sys
import json

def main():
    conn_string = "host='localhost' dbname='lab1' user='postgres' password='1'"

    print("Connecting to database\n    ->%s" % (conn_string))
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    print("Connected!\n")

    for i in json.loads(open('./dataset.json').read()):
        query_string = """
            INSERT INTO data(credit_card, currency, catch_phrase, fda_ndc_code) VALUES (
                '{0}', '{1}', '{2}', '{3}'
            );
        """
        query = query_string.format(i['credit_card'], i['currency'], i['catch_phrase'], i['fda_ndc_code'])
        res = cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
