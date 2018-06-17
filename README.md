# WebSocket Coins
[WSCoins](http://wscoins.com.pl/) project shows the current price of Bitcoin and Ethereum cryptocurrencies using WebSocket technology(**Django Channels v2.0**).
The main goal of the project is to test WebSocket technologi.
 
# Project logic
**Celery** as tasks scheduler receve data from cryptocompare website. Data are received in 10 second intervals.
As cache and message broker I use **Redis**
