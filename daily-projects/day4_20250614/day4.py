from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import sqlite3 as db


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
with open("CMC_api.txt") as f:
    api_key = f.read().strip()

def fetch_data():
  parameters = {
    'convert':'USD',
  }

  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,

  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data =  json.loads(response.text)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
  
  return data

def load_data():
   data = fetch_data()
   conn = db.connect("crypto.db")
   cn = conn.cursor()
   cn.execute("DROP TABLE IF EXISTS crypto_db")

   create_table_query = """
      CREATE TABLE IF NOT EXISTS crypto_db
      (
          ID INTEGER PRIMARY KEY AUTOINCREMENT,
          "name" VARCHAR(100),
          "rank" INTEGER,
          "symbol" VARCHAR(10),
          "price_usd" FLOAT
      )
  """

   cn.execute(create_table_query)
   for item in data["data"]:
      cn.execute("""
        INSERT INTO crypto_db
        (
            "name",
            "rank",
            "symbol",
            "price_usd"              
                 
        ) 
        VALUES (?, ?, ?, ?)
      """, (
          item["name"],
          item["cmc_rank"],
          item["symbol"],
          item["quote"]["USD"]["price"],
      ))
   conn.commit()
   cn.close()
   conn.close()
   print("Loaded Data to SQLite3.")


def run_etl() -> None:
  load_data()

if __name__ == "__main__":
  run_etl()
