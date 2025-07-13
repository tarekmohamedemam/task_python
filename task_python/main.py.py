import sys
sys.path.append('/content/sample_data')

import define_index_func as d_i
import vowel_count as v_c
import multiplication_table as m_t
import mario_pyramid as m_p
import sorted_list as s_l
import check_login as cl
import email_validation as ev
import email_domains as ed

# index of 'i'
s = input("Enter your string: ")
index_result = d_i.define_index(s)
print(f"Index of 'i' in your string is: {index_result}")

# count vowels
s2 = input("Enter another string: ")
vowel_count_result = v_c.count_vowels(s2)
print(f"Number of vowels: {vowel_count_result}")

# multiplication table
n = int(input("Enter a number for multiplication table: "))
for line in m_t.multiplication(n):
    print(line)

# mario pyramid
h = int(input("Enter pyramid height: "))
for row in m_p.mario(h):
    print(row)

# sort list
asc, desc = s_l.sort_list()
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

