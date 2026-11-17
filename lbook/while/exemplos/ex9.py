unconrfimed_users = ['alice', 'brian', 'candace']

confirmed_users = []


while unconrfimed_users:
    current_user = unconrfimed_users.pop()
    print("Verifyin user: " + current_user.title())
confirmed_users.append(current_user)


for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
