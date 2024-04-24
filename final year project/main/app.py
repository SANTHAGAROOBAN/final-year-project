import math
from flask import Flask, request, render_template 


def estimate_effort_cocomo(size, complexity, experience):

  effort_estimate = size * math.pow(complexity, 1.05) * math.pow(experience, -0.2)

  return effort_estimate


def estimate_cost_cocomo(size, complexity, experience, cost_per_person_month):
 

    effort_estimate = estimate_effort_cocomo(size, complexity, experience)

    cost_estimate = effort_estimate * cost_per_person_month

    return cost_estimate


def estimate_modules_fpa(function_points):


  modules_estimate = function_points * 0.7

  return modules_estimate


def estimate_manpower_ucp(use_case_points):
 
  manpower_estimate = use_case_points * 0.8

  return manpower_estimate


size = 10000  # Estimated lines of code
complexity = 3  # Complexity on a scale of 1 to 5
experience = 4  # Experience on a scale of 1 to 5
cost_per_person_month = 1890  # Cost per person-month in USD
function_points = 70  # Number of function points in the project
use_case_points = 100 

effort_estimate = estimate_effort_cocomo(size, complexity, experience)
print("The estimated software effort is {} person-months.".format(effort_estimate))


cost_estimate = estimate_cost_cocomo(size, complexity, experience, cost_per_person_month)

print("The estimated software cost is {} USD.".format(cost_estimate))


modules_estimate = estimate_modules_fpa(function_points)

print("The estimated number of modules is {}".format(modules_estimate))


manpower_estimate = estimate_manpower_ucp(use_case_points)

print("The estimated manpower is {}".format(manpower_estimate))

app = Flask(__name__)  

@app.route('/')
def index():

  return render_template("index.html")


@app.route('/estimate', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":

       # getting input with name = fname in HTML form
       size = request.form.get("a1")
       complexity = request.form.get("a2")
       experience = request.form.get("a3")
       cost_per_person_month = request.form.get("a4")
       function_points = request.form.get("a5")
       use_case_points = request.form.get("a6")

            
       size = int(size)
       complexity = int(complexity)
       experience = int(experience)
       cost_per_person_month = int(cost_per_person_month)
       function_points = int(function_points)
       use_case_points = int(use_case_points)
      
       
       print(size)
       print(complexity)
       print(experience)
       print(cost_per_person_month)
       print(function_points)
       print(use_case_points)

            
       effort_estimate = estimate_effort_cocomo(size, complexity, experience)

       cost_estimate = estimate_cost_cocomo(size, complexity, experience, cost_per_person_month)

       modules_estimate = estimate_modules_fpa(function_points)

       manpower_estimate = estimate_manpower_ucp(use_case_points)

          
 
       return render_template("out1.html",ts1=effort_estimate,ts2=cost_estimate,ts3=modules_estimate,ts4=manpower_estimate)
                           
       #return render_template("out.html",x=voltage,y=current,z=float(res),s=int(speed))
    return render_template("form.html")

if __name__=='__main__':
   app.run(debug=True)