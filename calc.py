def calculator():
    while True:
        c = str(input("Enter the operation (*, /, +, -, %, **, //, T for Tax, Q for quit)): "))
        
        #quit
        if c.lower() == 'q':
            print("Thank you for using the calculator!")
            break

        #for Tax
        if c == 'T' or c == 'Tax':
            a = int(input("Enter the $ amount: $"))
            state = str(input("Enter the Province (Ex: Alberta, Ontario): "))
            #Ver 1 in Hard coded Tax
            """ 
            if state == 'ON':
                print('Tax for that amount '+str(a)+' in ' +state+' is $',a * 0.13) 
                exit()
            elif state == 'BC':
                print('Tax for that amount '+str(a)+' in ' +state+' is $',a * 0.08)
                exit()
            else:
                print("Invalid Province")
                exit()
            """
            #Ver 2 in Tax: calling a function from another file
            """
            filename = 'C:\SriAIEngr\Head_First_Python\Learning\Tax.csv'
            import fetch_value_from_csv 
            taxPerc = fetch_value_from_csv.fetch_value_from_csv(filename, state, 2) 
            """

            #Ver 3 in Tax: Web Scrapping
            """
            import fetch_value_from_website
            taxPerc = fetch_value_from_website.fetch_value_from_website(state)
            #print(taxPerc)
            tax = float(taxPerc.replace('%', ''))
            print(''+taxPerc+ ' tax for that amount $'+str(a)+' in province, [' +state+'] is $',(a*tax)/100) 
            #exit()
            """
            #Ver 4 in Tax: From SQLite DB
            import DBcm
            import os
            db_details = r"C:\SriAIEngr\Head_First_Python\Learning\tax_rates.sqlite3"
            SQL = """SELECT tax_percent_str FROM Tax WHERE province = ?"""
            with DBcm.UseDatabase(db_details) as db:
                db.execute(SQL, (state,))  # Pass the parameter safely using a tuple
                taxPerc = db.fetchone()[0]
            tax = float(taxPerc.replace('%', ''))
            print(''+taxPerc+ ' tax for that amount $'+str(a)+' in province, [' +state+'] is $',(a*tax)/100) 
            continue

        #For Calc
        a = int(input("Enter the 1st number: "))
        b = int(input("Enter the 2nd number: "))

        """ ver 1 in calc
        if c == '*':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a * b))
        elif c == '/':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a / b))
        elif c == '+':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a + b))
        elif c == '-':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a - b))
        elif c == '%':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a % b))
        elif c == '**':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a ** b))
        elif c == '//':
            print("Result of "+str(a)+ ""+c+ "" +str(b)+" = " +str(a // b))
        else:
            print("Invalid operation")
        """
        #ver 2 in Calc
        import operator 
        operator_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,  # Use truediv for standard division
            '//': operator.floordiv,
            '%': operator.mod,
            '**': operator.pow
        }
        #calc = operator_map[c](a, b)
        print(f"Result: {a}{c}{b} = {operator_map[c](a, b)}")
        continue
    
calculator()