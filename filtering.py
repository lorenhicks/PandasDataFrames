import pandas as pd

data = {
    "user": ["Katie", "Emma", "Wyatt"],
    "age": [16,14,12],
    "auth_token_active": [True, True, False]
}
df = pd.DataFrame(data)
df_active = df.filter(items=["user", "auth_token_active"])

print(df_active)