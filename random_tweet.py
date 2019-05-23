import argparse
import csv
import random

def get_tweets_coumn_as_list(reader):
	line_count = 0
	tweets = []
	for row in reader:
		if line_count == 0:
			pass
		else:
			tweets.append(row[5])  # Get "text" column in CSV, 6th from the left (zero indexed)
	return tweets

def read_file(filename):
	with open(filename) as csv_file:
		reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		tweets = []
		for row in reader:
			if line_count == 0:
				line_count += 1
			else:
				tweets.append(row[5])  # Get "text" column in CSV, 6th from the left (zero indexed)
				line_count += 1
		return tweets

def parse_arguments():
	parser = argparse.ArgumentParser(description='Takes in Twitter archive csv and prints a random tweet.')
	parser.add_argument("filename", help="CSV filename")
	return parser.parse_args()

if __name__ == "__main__":
	args = parse_arguments()
	filename = args.filename

	# Read CSV file and get tweets column into list
	tweets = read_file(filename)

	#Get random tweet
	print(random.choice(tweets))


