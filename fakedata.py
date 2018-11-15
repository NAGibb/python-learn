from faker import Faker
fake = Faker()

# fake.name()
# for _ in range(10):
#  print(fake.name())


from faker import Factory
from faker.providers import internet

#fake = Factory.create()
#fake.add_provider(internet)

#print(fake.ipv4_private())


#import pydbgen
#from pydbgen import pydbgen
#myDB=pydbgen.pydb()

#myDB.gen_table(db_file='Testdb.DB',table_name='People',
#fields=['name','city','street_address','email'])


#testdf=myDB.gen_dataframe(5,['name','city','phone','date'])
#testdf

#for _ in range(10):
#    print(myDB.realistic_email('Tirtha Sarkar'))

#for _ in range(10):
#    print(myDB.simple_ph_number())

#    se=myDB.gen_data_series(data_type='date')
#    print(se)

#myDB.gen_table(5,fields=['name','city','job_title','phone','company','email'],
# db_file='People.db',table_name='People',primarykey='name',real_city=False)

#print(fake.profile(fields=None, sex=None))


#person_profile = fake.profile(fields=None, sex=None)
#for key,val in person_profile.items():
    #print("['{}', '{}'],".format(key, val))
#    employee.append("'{}', '{}'".format(key, val))

employee = []


#print(employee)


#print('simple')
#print(fake.simple_profile(sex=None))
# {   'address': '2404 Rebecca Walk Suite 544\nPort Jamesberg, MI 53206',
#     'birthdate': datetime.date(1943, 6, 23),
#     'blood_group': 'B+',
#     'company': 'Combs Inc',
#     'current_location': (Decimal('-22.2115295'), Decimal('120.744441')),
#     'job': 'Personnel officer',
#     'mail': 'michaeljackson@yahoo.com',
#     'name': 'Brian Kelly',
#     'residence': '7893 Christopher Crescent\nZacharybury, NY 11899',
#     'sex': 'M',
#     'ssn': '740-64-4032',
#     'username': 'hunterarnold',
#     'website': ['http://parsons.com/', 'https://www.vargas-rich.com/']}


#new_employee = 'first_name','last_name','address','phone','dob','hiredate','ssn'
#new_employee = '{}' , '{}'.format(first_name, last_name)
#employee.append(new_employee)


#employee.append("'first_name','last_name'")


# Adding a new key value pair
#employee.append('test', 'value' )

#print(employee)
import csv, datetime



csv_header = 'first_name','last_name', 'address', 'phone' , 'date_of_birth','hiredate','ssn'
employee_number = 2000
print ("Number of employees: %s" % employee_number)
print (datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))
with open('employee.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows([csv_header])
    for i in range(employee_number):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address()
        phone = fake.phone_number()
        dob = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=62)
        hiredate = fake.date_between(start_date="-20y", end_date="-1y")
        ssn = fake.ssn(taxpayer_identification_number_type="SSN")
        employee.append("'{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}'".format(first_name, last_name, address, phone, dob, hiredate, ssn))
        writer.writerows([employee])
csvFile.close()
print (datetime.datetime.now().strftime("%a, %d %B %Y %H:%M:%S"))




#print("first_name:%s" % first_name)
#print("last_name:%s" % last_name)
#print("address:%s" % address)
#print("phone:%s" % phone)
#print("birthdate:%s" % dob)
#print("hiredate:%s" % hiredate)
#print("ssn:%s" % ssn)
