import pandas as pd

data = {
    "user": ["Katie", "Emma", "Wyatt"],
    "age": [16,14,12],
    "auth_token_active": [True, True, False]
}
df = pd.DataFrame(data)

newdf = df.to_string()

print(newdf)