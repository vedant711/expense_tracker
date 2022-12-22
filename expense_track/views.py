from django.shortcuts import render,redirect
from .models import User, Expense
from django.contrib import messages
from datetime import date

# Create your views here.
def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False 

def index(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        name = form['name']
        password = form['password']
        users = User.objects.filter(name=name).values()
        print(users)
        if users[0]['password'] == password:
            return redirect('/'+str(users[0]['id']))
    return render(request,'index.html')

def create(request):
    if request.method == 'POST':
        form = request.POST
        user = User()
        user.name = form['name']
        user.password = form['pass']
        user.balance = float(form['balance'])
        # user.pin = int(form['pin'])
        users = User.objects.filter(name=user.name).values()
        # all_users = User.objects.all()
        # last_user = all_users[len(all_users)-1]
        # print(last_user.id)
        if not users and user.name != 'admin' and user.password != '' and user.balance!=0:
            user.save()
            u = User.objects.get(name=user.name)
            # id= user1[0]['id']
            # u=User.objects.get(id=id)
            print(u)
            tran = Expense()
            # user = User.objects.get(id=id)
            tran.user = u
            tran.type = 'credit'
            tran.amount = float(user.balance)
            tran.balance = float(user.balance)
            tran.date = date.today()
            tran.to = u.name
            tran.fro = u.name
            tran.save()
            messages.add_message(request, messages.INFO, 'User added successfully')
            # return redirect('/tran/'+str(u['id']))
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Incorrect Input')

    return render(request,'create.html')
    # return render(request,'create.html')


def dashboard(request,id):
    all_users = User.objects.all()
    users = User.objects.filter(id=id).values()
    trans = Expense.objects.filter(user_id=id).values()
    context = {'users': users, 'trans':trans, 'all_users':all_users}
    return render(request,'indi_usr.html',context)

def credit(request,id):
    cred = request.POST
    amount = cred['credit']
    # pin = cred['pin']
    user = User.objects.get(id=id)
    if isfloat(amount):
        # if user.pin == int(pin):
        user.balance =  float(user.balance) + float(amount)
        user.save()
        tran = Expense()
        tran.user = user
        tran.type = 'credit'
        tran.amount = float(amount)
        tran.balance = float(user.balance)
        tran.to = user.name
        tran.fro = user.name
        tran.date = date.today()
        print(tran)
        tran.save()
        messages.add_message(request, messages.INFO, 'Amount Credited Successfully')
        # else:
        #     messages.add_message(request, messages.INFO, 'Incorrect PIN')

    else:
        messages.add_message(request, messages.INFO, 'Incorrect Input')
    return redirect('/'+id)

    # users[0]['balance'] = float(users[0]['balance']) + float(amount)
    
def debit(request,id):
    deb = request.POST
    amount = deb['debit']
    # pin = deb['pin']

    user = User.objects.get(id=id)
    if isfloat(amount):
        user.balance =  float(user.balance) - float(amount)
        if user.balance >=0:
            # if user.pin == int(pin):
            user.save()
            tran = Expense()
            tran.user = user
            tran.type = 'debit'
            tran.amount = float(amount)
            tran.balance = float(user.balance)
            tran.to = user.name
            tran.fro = user.name
            tran.date = date.today()
            tran.save()
            messages.add_message(request, messages.INFO, 'Amount Debited Successfully')
            # else:
            #     messages.add_message(request, messages.INFO, 'Incorrect PIN')
        else:
            messages.add_message(request, messages.INFO, 'Insufficient Balance')

    else:
        messages.add_message(request, messages.INFO, 'Incorrect Input')
    return redirect('/'+id)

def transfer(request,id):
    deb = request.POST
    amount = deb['transfer']
    to = deb['to']
    to_user = User.objects.get(id=int(to))
    user = User.objects.get(id=id)
    if isfloat(amount):
        user.balance =  float(user.balance) - float(amount)
        if user.balance >=0:
            user.save()
            to_user.balance=float(to_user.balance)+float(amount)
            tran = Expense()
            tran_credit = Expense()
            tran.user = user
            tran.type = 'debit'
            tran.amount = float(amount)
            tran.balance = float(user.balance)
            tran.to = to_user.name
            tran.fro = user.name
            tran.date = date.today()
            tran.save()
            tran_credit.user = to_user
            tran_credit.type = 'credit'
            tran_credit.amount= float(amount)
            tran_credit.balance = float(to_user.balance)
            tran_credit.to = to_user.name
            tran_credit.fro = user.name
            tran_credit.date = date.today()
            tran_credit.save()
            messages.add_message(request, messages.INFO, 'Amount Transferred Successfully')
    return redirect('/'+str(id))


def logout(request):
    return redirect('/')
