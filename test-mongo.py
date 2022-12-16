import pymongo as pm
from datetime import datetime, timedelta
import matplotlib.pyplot as plt


# data = {
#     "Top Buyer": {
#         "1": {
#             "Buyer": "ZP",
#             "B.Lot": 280189,
#             "B.Val": 241200000000,
#             "B.Avg": 8607
#         },
#         "2": {
#             "Buyer": "BK",
#             "B.Lot": 147488,
#             "B.Val": 127100000000,
#             "B.Avg": 8619
#         },
#         "3": {
#             "Buyer": "CC",
#             "B.Lot": 97796,
#             "B.Val": 84100000000,
#             "B.Avg": 8596
#         },
#         "4": {
#             "Buyer": "TP",
#             "B.Lot": 75990,
#             "B.Val": 65500000000,
#             "B.Avg": 8613
#         },
#         "5": {
#             "Buyer": "YP",
#             "B.Lot": 75081,
#             "B.Val": 64599999999,
#             "B.Avg": 8607
#         },
#         "6": {
#             "Buyer": "AK",
#             "B.Lot": 72192,
#             "B.Val": 62200000000,
#             "B.Avg": 8614
#         },
#         "7": {
#             "Buyer": "RX",
#             "B.Lot": 60035,
#             "B.Val": 51800000000,
#             "B.Avg": 8628
#         },
#         "8": {
#             "Buyer": "XC",
#             "B.Lot": 56044,
#             "B.Val": 48400000000,
#             "B.Avg": 8640
#         },
#         "9": {
#             "Buyer": "YU",
#             "B.Lot": 52515,
#             "B.Val": 45200000000,
#             "B.Avg": 8609
#         },
#         "10": {
#             "Buyer": "NI",
#             "B.Lot": 41703,
#             "B.Val": 35900000000,
#             "B.Avg": 8615
#         }
#     },
#     "Top Seller": {
#         "1": {
#             "Seller": "DX",
#             "S.Lot": 455112,
#             "S.Val": 391700000000,
#             "S.Avg": 8606
#         },
#         "2": {
#             "Seller": "BK",
#             "S.Lot": 217339,
#             "S.Val": 187000000000,
#             "S.Avg": 8605
#         },
#         "3": {
#             "Seller": "ZP",
#             "S.Lot": 97791,
#             "S.Val": 84100000000,
#             "S.Avg": 8595
#         },
#         "4": {
#             "Seller": "AK",
#             "S.Lot": 84055,
#             "S.Val": 72500000000,
#             "S.Avg": 8624
#         },
#         "5": {
#             "Seller": "YU",
#             "S.Lot": 75445,
#             "S.Val": 65000000000,
#             "S.Avg": 8613
#         },
#         "6": {
#             "Seller": "RX",
#             "S.Lot": 46412,
#             "S.Val": 40100000000,
#             "S.Avg": 8641
#         },
#         "7": {
#             "Seller": "XC",
#             "S.Lot": 44932,
#             "S.Val": 38800000000,
#             "S.Avg": 8630
#         },
#         "8": {
#             "Seller": "PD",
#             "S.Lot": 35672,
#             "S.Val": 30600000000,
#             "S.Avg": 8591
#         },
#         "9": {
#             "Seller": "CC",
#             "S.Lot": 33587,
#             "S.Val": 29000000000,
#             "S.Avg": 8626
#         },
#         "10": {
#             "Seller": "KZ",
#             "S.Lot": 28046,
#             "S.Val": 24000000000,
#             "S.Avg": 8573
#         }
#     },
#     "T. Val": 1100000000000,
#     "F. NVal": -355200000000,
#     "T. Lot": 1200000,
#     "Avg": 8609,
#     "Date": datetime(2022, 12, 14, 0, 0)
# }

# Connect to the MongoDB server
client = pm.MongoClient('localhost', 27017)

# Connect to the database
db = client['Project_SL']

# Connect to the collection
coll = db['broker_summary']

# Insert the data
# coll.insert_one(data)

# Query the data
query = coll.find().sort('Date', pm.DESCENDING)

day = []
value = []
for data in query:
    day.append(data['Date'])
    value.append(data['F. NVal'])

# query = coll.find_one({'Date': datetime(2022, 12, 14, 0, 0)})
# Close the connection
client.close()


plt.bar(day, value, align='center')
plt.ylabel('Rupiah')
plt.show()
