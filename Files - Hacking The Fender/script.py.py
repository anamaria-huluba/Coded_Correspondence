# Reading In The Passwords(1-10)

# checkpoint 1
import csv

# checkpoints 1-6
compromised_users = []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    print(password_row['Username']) 

#returns:
# jean49
# haydenashley
# michaelastephens
# denisephillips
# andrew24
# kaylaabbott
# tmartinez
# mholden
# randygilbert
# watsonlouis
# mdavis
# patrickprice
# kgriffith
# hannasarah
# xaviermartin
# hrodriguez
# erodriguez
# danielleclark
# timothy26
# elizabeth19

# checkpoint 7

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

print(compromised_users)

# return:
# ['jean49', 'haydenashley', 'michaelastephens', 'denisephillips', 'andrew24', 'kaylaabbott', 'tmartinez', 
# 'mholden', 'randygilbert', 'watsonlouis', 'mdavis', 'patrickprice', 'kgriffith', 'hannasarah', 
# 'xaviermartin', 'hrodriguez', 'erodriguez', 'danielleclark', 'timothy26', 'elizabeth19']

# checkpoints 8-10

with open('compromised_users.txt', 'w') as compromised_user_file:
  for comromised_user in compromised_users:
    compromised_user_file.write(comromised_user)

# Notifying the Boss(11-15)

# checkpoints 11 & 12
import json

# checkpoint 13-15

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  json.dump(boss_message_dict, boss_message)

# Scrambling the Password(16-19)

# checkpoint 16-18
with open('new_passworc.csv', 'w') as new_passwords_obj:
  slash_null_sing = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
  
  """
  new_passwords_obj.write(slash_null_sing)
