import numpy as np
import pandas as pd
from datetime import datetime, timedelta

np.random.seed(42)

start = datetime(2019,1,1)
end = datetime(2021,12,31)
D = (end - start).days + 1

dates = [start + timedelta(days=i) for i in range(D)]
stores = ["store_1", "store_2"]
products = ["prod_A", "prod_B", "prod_C"]

rows = []
for d in dates:
    weekday = d.weekday()
    is_holiday = 1 if d.month==12 and d.day in (24,25,31) else 0
    for s in stores:
        for p in products:
            base = 50 if p=="prod_A" else (30 if p=="prod_B" else 15)
            season = 1 + 0.2*np.sin(2*np.pi*(d.timetuple().tm_yday)/365)
            promo = 1 if (np.random.rand() < 0.05) else 0
            promo_effect = 1.5 if promo else 1.0
            noise = np.random.normal(0, 5)
            weekday_effect = 1.2 if weekday>=5 else 1.0
            sales = max(0, int((base * season * weekday_effect * promo_effect) + (is_holiday*20) + noise))
            rows.append({"date": d.strftime('%Y-%m-%d'), "store": s, "product": p, "sales": sales, "promo": promo, "is_holiday": is_holiday})

df = pd.DataFrame(rows)
df.to_csv('data/retail_sales.csv', index=False)
print('Saved data/retail_sales.csv, shape:', df.shape)
