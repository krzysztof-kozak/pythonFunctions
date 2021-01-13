users = ('Martin', 'Patricia', "Helena", "Kris")

def greet_user(name: str) -> str:
  print(f'Hello {name}')

def return_first_user_from_list(users: list) -> str:
  return users[0]

for user in users:
  greet_user(user)

first_user = return_first_user_from_list(users)

print(first_user)