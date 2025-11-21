import sys
if len(sys.argv)==5:
    account_number=sys.argv[1]
    holder_name=sys.argv[2]
    branch=sys.argv[3]
    balance=sys.argv[4]
    print("User provided values:")
else:
    print("No input values-default values")
    account_number="95134"
    holder_name="Arun"
    branch="Hubli"
    balance=90000
    print("account_number:",account_number)
    print("holder_name:",holder_name)
    print("branch:",branch)
    print("Balance:",balance)

        
    
