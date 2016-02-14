import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('answer')
f = open('edinburgh_number.txt','w')
f.write(searchterm + '\n')
