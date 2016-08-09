import matplotlib.pyplot as plt 
import datetime
import csv



## Uploads Graph 
##   Plot over time 
##   http://matplotlib.org/users/pyplot_tutorial.html



x_unix=[]
y_uploadfps=[]

x_unix_2 = []
y_mdfps = []

# Import information
f = open('ampf_uploads.csv')
# f = open('query_result (x).csv')
#f = open('query_result.csv')
csv_f = csv.reader(f)
firstrow = 0

for row in csv_f: 
  if firstrow == 0:
    firstrow += 1
  else:
    x_unix.append(row[2])
    y_uploadfps.append(row[3])

# METADATA
f = open('ampf_metadata.csv')
# f = open('query_result (7).csv')
csv_f = csv.reader(f)
firstrow = 0

for row in csv_f: 
  if firstrow == 0:
    firstrow += 1
  else:
    x_unix_2.append(row[1])
    y_mdfps.append(row[2])


# AGGREGATE CALC
# x_unix_3 = []
# y_aggregate = []
# # Create aggregate set
# print min(x_unix[0],x_unix_2[0])
# print max(x_unix[-1],x_unix_2[-1])

# # for i in range(min(x_unix[0],x_unix_2[0]), max(x_unix[-1],x_unix_2[-1]),1 ):
# for i in range(1463122800,1463381999,1):
#   x_unix_3.append(i)
#   y_aggregate.append(y_uploadfps[i] + y_mdfps[i])


# Convert unix timestamps to datetime in PST
# x_dates = [dateutil.parser.parse(s) for s in x_unix]
x_dates = [datetime.datetime.utcfromtimestamp(float(s)) - datetime.timedelta(hours=7) for s in x_unix]
x_dates_2 = [datetime.datetime.utcfromtimestamp(float(s)) - datetime.timedelta(hours=7) for s in x_unix_2]
# x_dates_3 = [datetime.datetime.utcfromtimestamp(float(s)) - datetime.timedelta(hours=7) for s in x_unix_3]






# Create plot
plt.plot(x_dates,y_uploadfps,x_dates_2,y_mdfps) #,x_dates_3,y_aggregate) 
# plt.setp(lines,color='r',linewidt=2.0)

plt.show()
