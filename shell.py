import json

with open('data.json') as f:
    list_1 = json.load(f)

print(len(list_1))

a = list_1[0]
a1 = list_1[1]
a2 = list_1[2]
a3 = list_1[3]
a4 = list_1[4]
a5 = list_1[5]
a6 = list_1[6]
a7 = list_1[7]
a8 = list_1[8]
a9 = list_1[9]

from my_app.models import Customer, Work, Account

Customer.objects.all()
c = Customer(name=a['name'], phone=a['phone'], email=a['email'])
c.save()
c1 = Customer(name=a1['name'], phone=a1['phone'], email=a1['email'])
c1.save()
c2 = Customer(name=a2['name'], phone=a2['phone'], email=a2['email'])
c2.save()
c3 = Customer(name=a3['name'], phone=a3['phone'], email=a3['email'])
c3.save()
c4 = Customer(name=a4['name'], phone=a4['phone'], email=a4['email'])
c4.save()
c5 = Customer(name=a5['name'], phone=a5['phone'], email=a5['email'])
c5.save()
c6 = Customer(name=a6['name'], phone=a6['phone'], email=a6['email'])
c6.save()
c7 = Customer(name=a7['name'], phone=a7['phone'], email=a7['email'])
c7.save()
c8 = Customer(name=a8['name'], phone=a8['phone'], email=a8['email'])
c8.save()
c9 = Customer(name=a9['name'], phone=a9['phone'], email=a9['email'])
c9.save()


Work.objects.all()
w = Work(address=a['address'], city=a['city'], company=a['company'], postalZip=a['postalZip'], customer=c)
w.save()
w1 = Work(address=a1['address'], city=a1['city'], company=a1['company'], postalZip=a1['postalZip'], customer=c1)
w1.save()
w2 = Work(address=a2['address'], city=a2['city'], company=a2['company'], postalZip=a2['postalZip'], customer=c2)
w2.save()
w3 = Work(address=a3['address'], city=a3['city'], company=a3['company'], postalZip=a3['postalZip'], customer=c3)
w3.save()
w4 = Work(address=a4['address'], city=a4['city'], company=a4['company'], postalZip=a4['postalZip'], customer=c4)
w4.save()
w5 = Work(address=a5['address'], city=a5['city'], company=a5['company'], postalZip=a5['postalZip'], customer=c5)
w5.save()
w6 = Work(address=a6['address'], city=a6['city'], company=a6['company'], postalZip=a6['postalZip'], customer=c6)
w6.save()
w7 = Work(address=a7['address'], city=a7['city'], company=a7['company'], postalZip=a7['postalZip'], customer=c7)
w7.save()
w8 = Work(address=a8['address'], city=a8['city'], company=a8['company'], postalZip=a8['postalZip'], customer=c8)
w8.save()
w9 = Work(address=a9['address'], city=a9['city'], company=a9['company'], postalZip=a9['postalZip'], customer=c9)
w9.save()

Account.objects.all()

acc = Account(pin=a['pin'], acc_num=a['acc_num'], pan=a['pan'], cvv=a['cvv'], customer=c)
acc.save()
acc1 = Account(pin=a1['pin'], acc_num=a1['acc_num'], pan=a1['pan'], cvv=a1['cvv'], customer=c1)
acc1.save()
acc2 = Account(pin=a2['pin'], acc_num=a2['acc_num'], pan=a2['pan'], cvv=a2['cvv'], customer=c2)
acc2.save()
acc3 = Account(pin=a3['pin'], acc_num=a3['acc_num'], pan=a3['pan'], cvv=a3['cvv'], customer=c3)
acc3.save()
acc4 = Account(pin=a4['pin'], acc_num=a4['acc_num'], pan=a4['pan'], cvv=a4['cvv'], customer=c4)
acc4.save()
acc5 = Account(pin=a5['pin'], acc_num=a5['acc_num'], pan=a5['pan'], cvv=a5['cvv'], customer=c5)
acc5.save()
acc6 = Account(pin=a6['pin'], acc_num=a6['acc_num'], pan=a6['pan'], cvv=a6['cvv'], customer=c6)
acc6.save()
acc7 = Account(pin=a7['pin'], acc_num=a7['acc_num'], pan=a7['pan'], cvv=a7['cvv'], customer=c7)
acc7.save()
acc8 = Account(pin=a8['pin'], acc_num=a8['acc_num'], pan=a8['pan'], cvv=a8['cvv'], customer=c8)
acc8.save()
acc9 = Account(pin=a9['pin'], acc_num=a9['acc_num'], pan=a9['pan'], cvv=a9['cvv'], customer=c9)
acc9.save()


