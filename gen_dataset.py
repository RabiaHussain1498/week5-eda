import numpy as np
import pandas as pd

rng = np.random.default_rng(seed=42)
n = 5000

orders = pd.DataFrame({
    "order_id": np.arange(1, n + 1),
    "order_date": pd.date_range("2024-01-01", periods=n, freq="h"),
    "customer_id": rng.integers(1000, 1200, size=n),
    "product_category": rng.choice(
        ["Electronics", "electronics", "Home Goods", "Apparel", "Books"], size=n
    ),
    "quantity": rng.integers(1, 8, size=n),
    "unit_price": rng.normal(45, 20, size=n).round(2),
    "region": rng.choice(["North", "South", "East", "West", None], size=n, p=[0.24, 0.24, 0.24, 0.24, 0.04]),
})

# Introduce the mess, on purpose — do not skip this part
orders.loc[rng.choice(n, 150, replace=False), "customer_id"] = None
orders.loc[rng.choice(n, 30, replace=False), "quantity"] *= -1          # returns, disguised as negative quantity
orders.loc[rng.choice(n, 20, replace=False), "unit_price"] = 4999.99    # data-entry outliers
orders = pd.concat([orders, orders.sample(15, random_state=1)])        # duplicate rows, unannounced

orders.to_csv("data/orders_raw.csv", index=False)
print("shape:", orders.shape)
print(orders.head())
