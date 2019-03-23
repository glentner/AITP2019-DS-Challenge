import csv

with open('./data/gsod.obs.csv') as csvfile:
  with open('./data/us-in.station-ids', "r") as ids:
    with open('./data/us-in.station-wban', "r") as wban:
      with open('./data/good_data.csv', "a") as indiana:
        readCSV = csv.reader(csvfile, delimiter = ",")
        i = 0
        for row in readCSV:
          print(i)
          i = i + 1
          iddata = ids.readlines()  
          words = iddata[0].split("|")
          for word in words:
            if(row[0] == word):
              print(row)
              indiana.write(str(row) + "\n")
              break
          ids.seek(0)
      	  wbandata = wban.readlines()
          words = wbandata[0].split("|")
          for word in words:
            if(row[1] == word):
              print(row)
              indiana.write(str(row) + "\n")
	      break
          wban.seek(0)
