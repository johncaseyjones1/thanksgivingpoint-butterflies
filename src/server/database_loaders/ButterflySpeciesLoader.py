''' import pandas

excel_data = pandas.read_excel('/home/caseyjones/github/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/ButterflyMatrix.xlsx',sheet_name="Sheet1")

json_data = excel_data.to_json()

print("Json data:\n{}".format(json_data))
 '''
from excel2json import convert_from_file

convert_from_file('/home/caseyjones/github/thanksgivingpoint-butterflies/src/server/database_loaders/raw_data/ButterflyMatrix.xls')