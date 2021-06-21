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
		
		in_this_ticket = 0

		for i, row in enumerate(csv_reader):
			if row[6] == 'CS-34847':
				in_this_ticket += 1

		return in_this_ticket
		

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    print(create_sql())
	# 132


