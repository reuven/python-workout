#!/usr/bin/env python3


users = {}
with open('/etc/passwd') as f:
    for line in f:
        if not line.startswith("#") and line.strip():
            user_info = line.split(":")
            users[user_info[0]] = user_info[2]

for username, user_id in sorted(users.items()):
    print(f"{username}: {user_id}")
