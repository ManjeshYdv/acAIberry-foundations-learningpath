import os 

#reading the APP_ENV

app_env=os.environ.get("APP_ENV","not set")

print(f"Current APP_env: {app_env}")

