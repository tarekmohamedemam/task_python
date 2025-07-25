import csv
f = open("E-mails.csv", "r", newline="")
reader = csv.reader(f)
data = list(reader)
f.close()

emails = []
for i in range(1, len(data)):
    emails.append(data[i][3])

cleane_email = list(map(str.strip, emails))

domain= list(map(lambda x: x.split("@")[1], cleane_email))

print(f" before removing redundancy: {len(domain)}")

mysetemail = set(domain)

print(mysetemail)

print(f"after removing redundancy: {len(mysetemail)}")