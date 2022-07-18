import psycopg2
import datetime

db_name =  'feedback_database'
username =  'postgres'
password = 'ahmed'
host = '172.20.200.40'
port = 5432


class PostgressDB:

    def __init__(self):
        # Connect to your postgres DB
        self.connenction = psycopg2.connect(host=host,dbname=db_name,user=username,password=password,port=port)
        # Open a cursor to perform database operations
        self.cursor = self.connenction.cursor()
    
    def connection_close(self):
        if self.cursor:
            self.cursor.close()
        
        if self.connenction:
            self.connenction.close()
    
    def send_patient_data_to_postgres_database(self,patient_details):
        send_patient_data_to_database_qurey = ('''
        
        
            INSERT INTO "feedback_app_sms_sent_for_feedback"
            ("patient_uhid", "encounter_id","patient_name", "patient_contact_number", "patient_gender","patient_bed_number", "patient_bed_location", "patient_admission_date_time", "patient_discharge_date_time", "sms_sent_date")
            VALUES
            (%s, %s, %s, %s,%s, %s, %s,%s,%s,%s )

        ''')
        
        for i in list(patient_details.keys()):
            date_added = datetime.datetime.now()
            self.cursor.execute(send_patient_data_to_database_qurey,[   patient_details[i]["patient_id"],
                                                                        patient_details[i]["encounter_id"],
                                                                        patient_details[i]["patient_name"],
                                                                        patient_details[i]["phone_number"],
                                                                        patient_details[i]["gender"],
                                                                        patient_details[i]["bed_number"],
                                                                        patient_details[i]["location"],
                                                                        patient_details[i]["admission_datetime"],
                                                                        patient_details[i]["discharge_datetime"],
                                                                        date_added,
                                                                        ])
            self.connenction.commit()                    
        # data = self.cursor.fetchall()
                            
        #return data


    def delete_patient_above_24hr(self):
        delete_patient_above_24hr_query = ('''
        
        DELETE FROM "feedback_app_sms_sent_for_feedback"
        WHERE "sms_sent_date" < NOW() - INTERVAL '1 DAY'
     
        ''')

        self.cursor.execute(delete_patient_above_24hr_query)
        self.connenction.commit()