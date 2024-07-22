import pandas as pd
import csv

class CSV:
	def __init__(self, fileName: str):

		if not fileName.endswith("csv"):
			raise Exception("Not a valid csv file name")
		
		self.csvFileName = fileName
		

	def initializeCsv(self, list: list[str]):
		self.columns = list

		try:
			pd.read_csv(self.csvFileName)
		except FileNotFoundError:
			dataFrame = pd.DataFrame(columns=list)
			dataFrame.to_csv(self.csvFileName, index=False)

	def addEntry(self, *args):
		print(args)
		columnCount = len(args)
		print(columnCount)

		print(self.columns)

		if columnCount != len(self.columns):
			raise Exception("The number of columns and the data does not match")
		
		newEntry = {}

		for i in range(len(self.columns)):
			item = self.columns[i]
			newEntry[item] = args[i]

		with open(self.csvFileName, "a", newline="") as csvFile:
			writer = csv.DictWriter(csvFile, fieldnames=self.columns)
			writer.writerow(newEntry)

		print("Entered record added successfully")