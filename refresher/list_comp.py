# numbers = [1, 3, 5]
# doubled = [num * 2 for num in numbers]

# for num in numbers:
#     doubled.append(num * 2)

friends = ["Rolf", "Sam", "Samntha", "Saurbh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S") ]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(starts_s)
