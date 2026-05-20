### List of dictionaries/array of objects
#### How to handle a missing a field that is critical
```
import pandas as pd
users = [
    {"user_id": "U123", "name": "Alice"},
    {"user_id": "U456", "name": "Bob"},
    {"user_id": "U789", "name": "Charlie"}
]

missing_users_id = [
    {"user_id": "U123", "name": "Alice"},
    {"name": "Bob"},  # Missing user_id - this is at index 1
    {"user_id": "U789", "name": "Charlie"}
]

def flatten_with_enumerate(list_of_dicts):
    flattened = []
    for idx, user in enumerate(list_of_dicts):  # Automatic counter
        if 'user_id' not in user:
            raise ValueError(f"Missing user_id at index {idx}")
        user_data = {k: v for k, v in user.items() if k != 'events'}
        for event in user.get('events', []):
            flattened.append({**user_data, **event})
    return pd.DataFrame(flattened)

users_df = flatten_with_enumerate(users)

users_df.head()
missing_users_id_df = flatten_with_enumerate(missing_users_id)
```
