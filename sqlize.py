############------------ IMPORTS ------------############
import csv

############------------ FUNCTION(S) ------------############
def create_sql():
	'''
	USE Legacy
	UPDATE dbo.tblAffiliateSettings
	SET TrackingHtml = '<INSERT TAG HERE>'
	WHERE AffiliateSiteName = '<INSERT AFFILIATE NAME HERE>
	'''
	with open('JanusCommunicationAnalyticsTags.csv', 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		
		sql_scripts = open('sql_scrips.txt', 'w')

		for i, row in enumerate(csv_reader):
			if row[6] == 'CS-34847':
				sql_scripts.write(f"""USE Legacy\nUPDATE dbo.tblAffiliateSettings\nSET TrackingHtml = '{row[5]}'\nWHERE AffiliateSiteName = '{row[0]}'\n\n\n""")

		sql_scripts.close()
		

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    create_sql()