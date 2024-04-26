import pandas as pd

data = {
    "user": ["Katie", "Emma", "Wyatt"],
    "age": [16,14,12],
    "auth_token_active": [True, True, False]
}
df = pd.DataFrame(data)

def activeSession(n):
    return (n, data["user"][int(n)], data["auth_token_active"][int(n)])

sessionID = map(activeSession, (0, 1, 2))

print(list(sessionID))