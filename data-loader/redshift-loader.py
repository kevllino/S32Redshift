import psycopg2
import time
conn = psycopg2.connect("dbname=db1 user=data_loader host=*.us-west-2.redshift.amazonaws.com port=5439")
cur = conn.cursor()

def load_batch(batch_id):
    path = 's3://bucket1/load-manifests/session_manifest_jsonpath/session_manifest_' + batch_id + '.json'
    cur.execute("""copy x_load.raw_session(
        session_id,
        session_status,
        start_tsp,
        end_tsp,
        last_updated,
        start_event_id,
        end_event_id,
        duration,
        nb_of_events)
        from %s with
        credentials 'aws_iam_role=arn:aws:iam::account_number:role/Redshift-Role'
        json 's3://bucket1/load-manifests/session_manifest_jsonpath/session_jsonpath.json'
        TIMEFORMAT as 'epochmillisecs'
        manifest
        maxerror as 10;""", (path, ))
    conn.commit()

if __name__ == '__main__':
    # [str(b1) + "-" + str(b1 + 50) for b1 in range(0,2000,50)]
    for batch_id in ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500', '500-550', '550-600', '600-650', '650-700', '700-750', '750-800', '800-850', '850-900', '900-950', '950-1000', '1000-1050', '1050-1100', '1100-1150', '1150-1200', '1200-1250', '1250-1300', '1300-1350', '1350-1400', '1400-1450', '1450-1500', '1500-1550', '1550-1600', '1600-1650', '1650-1700', '1700-1750', '1750-1800', '1800-1850', '1850-1900', '1900-1950', '1950-2000']:
        load_batch(batch_id)
        time.sleep(90)
    cur.close()
