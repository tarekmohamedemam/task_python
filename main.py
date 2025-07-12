import sys
sys.path.append('/content/sample_data')

import define_index_func as di
import vowel_count as vc
import multiplication_table as mt
import mario_pyramid as mp
import sorted_list as sl
import check_login as cl
import email_validation as ev
import email_domains as ed

# index of 'i'
s = input("Enter your string: ")
index_result = di.define_index(s)
print(f"Index of 'i' in your string is: {index_result}")

# count vowels
s2 = input("Enter another string: ")
vowel_count_result = vc.count_vowels(s2)
print(f"Number of vowels: {vowel_count_result}")

# multiplication table
n = int(input("Enter a number for multiplication table: "))
for line in mt.multiplication(n):
    print(line)

# mario pyramid
h = int(input("Enter pyramid height: "))
for row in mp.mario(h):
    print(row)

# sort list
asc, desc = sl.sort_list()
print("Ascending:", asc)
print("Descending:", desc)

# login check
u = input("Enter username: ")
p = input("Enter password: ")
login_result = cl.login(u, p)
print("Login result:", login_result)

# email validation
for attempt in range(5):
    email_input = input("Enter your email: ")
    result = ev.check_email(email_input)
    if result:
        print("Email is valid.")
        break
    else:
        print("Invalid email.")
else:
    raise Exception("Failed after 5 attempts.")

# extract domains from emails
emails_input = input("Enter emails separated by space: ")
emails = emails_input.split()
domains = ed.get_domains(emails)
print("Extracted domains:", domains)

