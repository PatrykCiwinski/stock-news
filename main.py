STOCK = "NVDA"
COMPANY_NAME = "NVIDIA CORPORATION"
import requests
import os
from twilio.rest import Client

account_sid = "AC45109d1315819230c7f030ae49951959"
auth_token = "3027f1c41e5060045cab46ba25fe007d"
twilio_number="+19783008627"
my_number="+48739974641"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
Stock_PARAMETERS={"apikey":"BJ35UY13WVI10DOO", "function": "TIME_SERIES_DAILY", "symbol":STOCK}
News_PARAMETERS={"apiKey":"3d0ef3de331746b384797842f1d2a006","QInTitle":COMPANY_NAME}

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response=requests.get(url=STOCK_ENDPOINT, params=Stock_PARAMETERS)
response.raise_for_status()
stock_data=response.json()
stock_time=stock_data["Time Series (Daily)"]
# for date in stock_time:
#     print(date[1]["4. close"])
stock_data_list=[value for (key, value) in stock_time.items()]

yesterday_closing_price=stock_data_list[0]["4. close"]
print(yesterday_closing_price)
day_before_yesterday_closing_price=stock_data_list[1]["4. close"]
print(day_before_yesterday_closing_price)
difference=abs(float(yesterday_closing_price)-float(day_before_yesterday_closing_price))
print(difference)
diff_percent=(difference/float(yesterday_closing_price))*100
print(diff_percent)
if float(diff_percent)>5:
    response=requests.get(url=NEWS_ENDPOINT, params=News_PARAMETERS)
    response.raise_for_status()
    articles_data=response.json()["articles"]

three_articles=articles_data[:3]
print(three_articles)

# Send a separate message with each article's title and description to your phone number. 


formatted_articles=[f"Title: {article['title']},\n Brief: {article['description']}" for article in three_articles]
print(formatted_articles)



client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=twilio_number,
        to=my_number)