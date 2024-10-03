from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
  peoples = [
    {"name":"keshav", "Age":20, "city":"Gurgaon"},
     {"name":"Rohit", "Age":21, "city":"Delhi"},
      {"name":"Rahul", "Age":18, "city":"Patna"},
       {"name":"Ram", "Age":17, "city":"Noida"},
        {"name":"Shyam", "Age":12, "city":"stm"},
         {"name":"Mohan", "Age":54, "city":"uk"},
          {"name":"Rohan", "Age":22, "city":"punjab"},
           {"name":"Avanish pal", "Age":21, "city":"motipur"},
            {"name":"Vikas", "Age":29, "city":"rithala"},
    
  ]
  for people in peoples:
    print(people)
  return render(request , 'index.html', context={"peoples":peoples})

def About_view(request):
  return HttpResponse("<h1>hello i am about page</h1>")