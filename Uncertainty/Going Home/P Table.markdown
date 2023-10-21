# Week Table
Week           | P(Week-Off) | P(Working)
Week-Off       | 0.5        | 0.5

# Mood Table
Week           | Mood         | P(Mood)
Week-Off       | Happy        | 0.3
Week-Off       | Sad          | 0.5
Week-Off       | Just okay    | 0.2
Working        | Happy        | 0.4
Working        | Sad          | 0.3
Working        | Just okay    | 0.3

# Reason Table
Week           | Reason       | P(Reason)
Week-Off       | Important    | 0.4
Week-Off       | Festival     | 0.4
Week-Off       | Moody        | 0.2
Working        | Important    | 0.1
Working        | Festival     | 0.3
Working        | Moody        | 0.6

# Permission Table
Reason         | Permission   | P(Permission)
Important      | Granted      | 0.9
Important      | Denied       | 0.1
Festival       | Granted      | 0.8
Festival       | Denied       | 0.2
Moody          | Granted      | 0.5
Moody          | Denied       | 0.5

# Final Decision Table
Mood           | Permission   | Final Decision   | P(Final Decision)
Happy          | Granted      | Going Home       | 0.9
Happy          | Granted      | Staying          | 0.1
Happy          | Denied       | Going Home       | 0.1
Happy          | Denied       | Staying          | 0.9
Sad            | Granted      | Going Home       | 0.8
Sad            | Granted      | Staying          | 0.2
Sad            | Denied       | Going Home       | 0.3
Sad            | Denied       | Staying          | 0.7
Just okay      | Granted      | Going Home       | 0.6
Just okay      | Granted      | Staying          | 0.4
Just okay      | Denied       | Going Home       | 0.4
Just okay      | Denied       | Staying          | 0.6
