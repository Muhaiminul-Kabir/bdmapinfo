from datetime import datetime, timedelta, timezone

 


print(datetime.now(timezone(timedelta(hours=6))).isoformat())
