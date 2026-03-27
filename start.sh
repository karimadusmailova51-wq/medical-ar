#!/bin/bash

# Запустить Python-сервер в фоне
echo "Запуск Python-сервера..."
python3 server-proxy.py &

# Немного подождать, чтобы сервер успел стартовать
sleep 2

# Запустить Live Server через open (откроет index.html в браузере)
echo "Открываем index.html через Live Server..."
open -a "Google Chrome" "http://127.0.0.1:5500/index.html"

# Оставить терминал открытым для сервера
wait