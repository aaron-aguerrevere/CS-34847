############------------ IMPORTS ------------############
import csv

############------------ FUNCTION(S) ------------############
def create_sql():
	with open('JanusCommunicationAnalyticsTags.csv', 'r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		
		for i, row in enumerate(csv_reader):
			if i == 0:
				print(", ".join(row))

'''
Legacy Site Name, Description, Website Name, Corporate Name,
Email Communication Sent, Analytics Tag, JIRA Ticket, Notes, 
'''

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    create_sql()


'''
USE Legacy
UPDATE dbo.tblAffiliateSettings
  SET TrackingHtml = '<INSERT TAG HERE>'
WHERE AffiliateSiteName = '<INSERT AFFILIATE NAME HERE>
'''