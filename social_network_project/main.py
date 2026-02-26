import pandas as pd

# Load dataset
data = pd.read_csv("friends.csv")

# Build graph
graph = {}

for _, row in data.iterrows():
    user1 = row["user1"]
    user2 = row["user2"]

    if user1 not in graph:
        graph[user1] = set()

    if user2 not in graph:
        graph[user2] = set()

    graph[user1].add(user2)
    graph[user2].add(user1)

# Function to recommend friends
def recommend_friends(user):
    if user not in graph:
        return []

    direct_friends = graph[user]
    recommendations = {}

    for friend in direct_friends:
        for mutual in graph[friend]:
            if mutual != user and mutual not in direct_friends:
                if mutual not in recommendations:
                    recommendations[mutual] = 0
                recommendations[mutual] += 1

    # Sort by number of mutual friends
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)

    return sorted_recommendations


# Ask user
user_input = input("Enter user name (A/B/C/D/E/F): ")

results = recommend_friends(user_input)

if results:
    print("Recommended Friends:")
    for user, score in results:
        print(user, " (Mutual Friends:", score, ")")
else:
    print("No recommendations found.")