import re

print(re.match(r'\d{3}-\d{3,5}','010-12345'))
print(re.match(r'\d{3}-\d{3,5}','010 12345'))

print(re.split(r'[\s\,]+','a,b, c  d'))

print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


m = re.match('^(\d{3})[\-\s]+(\d{3,8})$','010 - 12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))


print(re.match(r'(\d+)(0*)$','102300').group(2))

print(re.match(r'(\d+?)(0*)$','102300').group(2))


telephone = re.compile(r'\d{3}[\s\-]+\d{3,5}')
print(telephone.match('101 - 12345'))

email = re.compile(r'^[a-zA-Z0-9]+[\.]*[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
print(email.match('someone@gmail.com'))
print(email.match('bill.gates@microsoft.com'))
print(email.match('258685520@qq.com'))

email2 = re.compile(r'\<[a-zA-Z]+[\s]+[a-zA-Z]+\>[\s]*[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$')
print(email2.match('<Tom Paris> tom@voyager.org'))