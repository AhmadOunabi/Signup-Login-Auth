from faker import Faker
fake=Faker()
name=fake.name()
name=name.replace(' ','_').lower()
print (name)