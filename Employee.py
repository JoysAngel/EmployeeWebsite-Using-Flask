from flask import Flask, render_template

employee = Flask(__name__)

@employee.route('/')
def Adding_Employee():
    return  render_template("addemployee.html")

@employee.route('/search')
def Search_Employee():
    return render_template("searchemployee.html")

@employee.route('/update')
def Update_Employee():
    return render_template("updateemployee.html")

@employee.route('/delete')
def Delete_Employee():
    return render_template("deleteemployee.html")

if __name__=="__main__":
    employee.run()