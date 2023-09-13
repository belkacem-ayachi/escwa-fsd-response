# UN Technical Exam

The following is a technical assessment

### Details: 
+ Author: Mohamad Rahhal

### Installation notes:
After cloning the repo, execute the following:

```bash
docker compose up
```

** Note: you need to have docker installed **


The above will run a docker container with a Django application on it, the application currently has only 1 endpoint to aggreate the response of the following request:

```bash
curl --location 'https://escwaapigateway.azure-api.net/DeltaLakeReader/escwa?name=ETDP%2FTotal%20Trades%20by%20Sector'
```

Curl to test endpoint:


```bash
curl --location 'http://127.0.0.1:8000/aggregate' \
--header 'Content-Type: application/json' \
--data '{
    "Reporter": "Algeria",
    "Sector": "Miscellaneous manufactured articles",
    "Partner": "Angola"
}'
```

You can input one or more of the below:

+ Reporter
+ Sector
+ Partner



Note:

+ Chat GPT was used to debug an issue with CSR Tokens (which in this case we want to ignore)

+ Used pre-written skeleton for the view urls.

+ Pip freeze to get the requirements

+ Django's default setup commands:

```
python3 -m django startproject 
python3 -m django startapp
python3 manage.py migrate
```
