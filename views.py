from django.db.models import Count
from django.shortcuts import render, redirect

# Create your views here.
from admins.forms import RegisterForms
from admins.models import RegisterModel, PatentModel


def index(request):
    if request.method == "POST":
        usid = request.POST.get('username')
        pswd = request.POST.get('password')
        try:
            check = RegisterModel.objects.get(userid=usid, password=pswd)
            request.session['userid'] = check.id
            return redirect('userpage')
        except:
            pass
    return render(request,'admins/index.html')

def register(request):
    if request.method == "POST":
        forms = RegisterForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('index')
    else:
        forms = RegisterForms()
    return render(request, 'admins/register.html', {'form': forms})

def userpage(request):
    return render(request,'admins/userpage.html')

def mydetails(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    return render(request,'admins/mydetails.html',{'obje':us_id})

def upload_page(request):
    usid = request.session['userid']
    us_id = RegisterModel.objects.get(id=usid)
    a=''
    b=''
    c=''
    d=''
    e=''
    f=''
    j=''
    k=''
    spl=''
    yr=''
    ans=''
    if request.method == "POST":
        a=request.POST.get('patentid')
        b=request.POST.get('patentname')
        c=request.POST.get('age')
        d=request.POST.get('problems')
        e=request.POST.get('address')
        f=request.POST.get('number')
        g=request.POST.get('emailid')
        h=request.POST.get('gender')
        i=request.POST.get('ward')
        j=request.POST.get('reason')
        k=request.POST.get('date')
        spl=k.split('-')
        yr=spl[2]
        if PatentModel.objects.filter(patentid=a):
            ans='This Patent Id Already Exist !! '
        else:
            PatentModel.objects.create(patentid=a,panentname=b,age=c,problem=d,address=e,moblenumber=f,mail=g,gender=h,ward_type=i,reason=j,date=k,year=yr,usid=us_id)
            ans='Sucessfully save!!'
    return render(request,'admins/upload_page.html',{'spl':ans})

def search_patent(request):
    aa=''
    bb=''

    if request.method == "POST":
        aa=request.POST.get('patid')
        request.session['pauid']=aa
        bb=request.POST.get('name')
        request.session['nmae']=bb
        if PatentModel.objects.filter(patentid=aa,panentname=bb):
            return redirect('particular_patent')
    return render(request,'admins/search_patent.html')

def particular_patent(request):
    cc=''
    dd=''
    cc=request.session['pauid']
    dd=request.session['nmae']
    obj=PatentModel.objects.filter(patentid=cc,panentname=dd)
    return render(request,'admins/particular_patent.html',{'obj':obj})

def dataset(request):
    obj = PatentModel.objects.all()
    return render(request,'admins/dataset.html',{'obj':obj})

def chart_page(request):
    qwe=''
    cht=''
    obj= PatentModel.objects.values('year').annotate(dcount=Count('year'))
    if request.method == "POST":
        qwe=request.POST.get('yr')
        cht=PatentModel.objects.filter(year=qwe).values('reason').annotate(dcount=Count('reason'))
    return render(request,'admins/chart_page.html',{'obj':obj,'cht':cht,'fg':qwe})