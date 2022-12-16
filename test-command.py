import pymongo as pm
from datetime import datetime, timedelta

day = datetime.today()
day = day.replace(hour=0, minute=0, second=0, microsecond=0)

client = pm.MongoClient('localhost', 27017)
db = client['Project_SL']
coll = db['broker_summary']

data = [{
    "Top Buyer": {
      "1": {
        "Buyer": "ZP",
        "B.Lot": 280189,
        "B.Val": 241200000000,
        "B.Avg": 8607
      },
      "2": {
        "Buyer": "BK",
        "B.Lot": 147488,
        "B.Val": 127100000000,
        "B.Avg": 8619
      },
      "3": {
        "Buyer": "CC",
        "B.Lot": 97796,
        "B.Val": 84100000000,
        "B.Avg": 8596
      },
      "4": {
        "Buyer": "TP",
        "B.Lot": 75990,
        "B.Val": 65500000000,
        "B.Avg": 8613
      },
      "5": {
        "Buyer": "YP",
        "B.Lot": 75081,
        "B.Val": 64599999999,
        "B.Avg": 8607
      },
      "6": {
        "Buyer": "AK",
        "B.Lot": 72192,
        "B.Val": 62200000000,
        "B.Avg": 8614
      },
      "7": {
        "Buyer": "RX",
        "B.Lot": 60035,
        "B.Val": 51800000000,
        "B.Avg": 8628
      },
      "8": {
        "Buyer": "XC",
        "B.Lot": 56044,
        "B.Val": 48400000000,
        "B.Avg": 8640
      },
      "9": {
        "Buyer": "YU",
        "B.Lot": 52515,
        "B.Val": 45200000000,
        "B.Avg": 8609
      },
      "10": {
        "Buyer": "NI",
        "B.Lot": 41703,
        "B.Val": 35900000000,
        "B.Avg": 8615
      }
    },
    "Top Seller": {
      "1": {
        "Seller": "DX",
        "S.Lot": 455112,
        "S.Val": 391700000000,
        "S.Avg": 8606
      },
      "2": {
        "Seller": "BK",
        "S.Lot": 217339,
        "S.Val": 187000000000,
        "S.Avg": 8605
      },
      "3": {
        "Seller": "ZP",
        "S.Lot": 97791,
        "S.Val": 84100000000,
        "S.Avg": 8595
      },
      "4": {
        "Seller": "AK",
        "S.Lot": 84055,
        "S.Val": 72500000000,
        "S.Avg": 8624
      },
      "5": {
        "Seller": "YU",
        "S.Lot": 75445,
        "S.Val": 65000000000,
        "S.Avg": 8613
      },
      "6": {
        "Seller": "RX",
        "S.Lot": 46412,
        "S.Val": 40100000000,
        "S.Avg": 8641
      },
      "7": {
        "Seller": "XC",
        "S.Lot": 44932,
        "S.Val": 38800000000,
        "S.Avg": 8630
      },
      "8": {
        "Seller": "PD",
        "S.Lot": 35672,
        "S.Val": 30600000000,
        "S.Avg": 8591
      },
      "9": {
        "Seller": "CC",
        "S.Lot": 33587,
        "S.Val": 29000000000,
        "S.Avg": 8626
      },
      "10": {
        "Seller": "KZ",
        "S.Lot": 28046,
        "S.Val": 24000000000,
        "S.Avg": 8573
      }
    },
    "T. Val": 1100000000000,
    "F. NVal": -355200000000,
    "T. Lot": 1200000,
    "Avg": 8609,
    "Date": day - timedelta(days=1)
  }]

data.append(  {
    "Top Buyer": {
      "1": {
        "Buyer": "CC",
        "B.Lot": 233852,
        "B.Val": 201700000000,
        "B.Avg": 8624
      },
      "2": {
        "Buyer": "AK",
        "B.Lot": 186646,
        "B.Val": 161300000000,
        "B.Avg": 8641
      },
      "3": {
        "Buyer": "ZP",
        "B.Lot": 151887,
        "B.Val": 131300000000,
        "B.Avg": 8647
      },
      "4": {
        "Buyer": "YU",
        "B.Lot": 89546,
        "B.Val": 77500000000,
        "B.Avg": 8659
      },
      "5": {
        "Buyer": "BK",
        "B.Lot": 71482,
        "B.Val": 61800000000,
        "B.Avg": 8647
      },
      "6": {
        "Buyer": "YP",
        "B.Lot": 37924,
        "B.Val": 32600000000,
        "B.Avg": 8607
      },
      "7": {
        "Buyer": "PD",
        "B.Lot": 35138,
        "B.Val": 30300000000,
        "B.Avg": 8618
      },
      "8": {
        "Buyer": "RX",
        "B.Lot": 28275,
        "B.Val": 24600000000,
        "B.Avg": 8686
      },
      "9": {
        "Buyer": "BB",
        "B.Lot": 28000,
        "B.Val": 24200000000,
        "B.Avg": 8650
      },
      "10": {
        "Buyer": "OD",
        "B.Lot": 25965,
        "B.Val": 22400000000,
        "B.Avg": 8622
      }
    },
    "Top Seller": {
      "1": {
        "Seller": "CC",
        "S.Lot": 246009,
        "S.Val": 212300000000,
        "S.Avg": 8632
      },
      "2": {
        "Seller": "AK",
        "S.Lot": 155826,
        "S.Val": 134400000000,
        "S.Avg": 8627
      },
      "3": {
        "Seller": "BK",
        "S.Lot": 142639,
        "S.Val": 123300000000,
        "S.Avg": 8641
      },
      "4": {
        "Seller": "RX",
        "S.Lot": 129751,
        "S.Val": 111900000000,
        "S.Avg": 8626
      },
      "5": {
        "Seller": "ZP",
        "S.Lot": 86271,
        "S.Val": 74700000000,
        "S.Avg": 8655
      },
      "6": {
        "Seller": "YU",
        "S.Lot": 53959,
        "S.Val": 46500000000,
        "S.Avg": 8619
      },
      "7": {
        "Seller": "KZ",
        "S.Lot": 49584,
        "S.Val": 42800000000,
        "S.Avg": 8627
      },
      "8": {
        "Seller": "YP",
        "S.Lot": 42502,
        "S.Val": 36800000000,
        "S.Avg": 8666
      },
      "9": {
        "Seller": "BB",
        "S.Lot": 35486,
        "S.Val": 30600000000,
        "S.Avg": 8619
      },
      "10": {
        "Seller": "XC",
        "S.Lot": 22398,
        "S.Val": 19200000000,
        "S.Avg": 8592
      }
    },
    "T. Val": 932000000000,
    "F. NVal": -135900000000,
    "T. Lot": 1100000,
    "Avg": 8636,
    "Date": day - timedelta(days=2)
  })
# coll.insert_many(data)

client.close()