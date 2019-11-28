# simple-flask-api
simple flask api 

## Installation

### Requirements:

   - Python 2.7+ or 3.4+
   - Flask 0.12.3+
   - Mysql Connector

```pip install Flask-API```

```pip install mysql-connector```

### Starting
```python app.py```

## script_conf.json

Should create the file ```script_conf.json``` in the directory ```/config``` with the ```bot_id``` and the ```chat_id``` from Telegram, to broadcast some msg when the methods are configured for.

```json
{
    "script-conf":{
        "telegram":{
            "bot_id"       : "bot_id", 
            "chat_id"      : "chat_id"
         }
    }
}
```

### CURL example to POST request  for directly message broadcast to telegram
```curl -i -H "Content-Type: application/json" -X POST -d '{"bot":"bot_id", "chat_id":"chat_id", "msg":"Message here..."}' http://localhost:5000/broadcast```

### Routes

```@app.route("/lead/<name>/<email>/<origin>/<alert>", methods=['GET'])```

```@app.route("/campaing/<origin>", methods=['GET'])```
