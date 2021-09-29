import os,json
def log():
    c=0
    if os.path.exists("database.json"):
        print("login your file")
        f=open('database.json',"r")
        m=json.load(f)
        for det in m:
            print("Enter your "+det)
            n=input()
            if m[det]==n:
                c+=1
                if c==3:
                    print(m)
            else:
                print("your "+det,"not matched") 
                log()
    else:
        print("crate your file by using username and password")
        l=["username","password","conform password"]
        d={}
        f=open('database.json',"w+")
        for details in l:
            print("Enter your "+details)
            d[details]=input()
        if d[l[1]]==d[l[2]]:
            json.dump(d,f,indent=3)
        else:
            print("password does not match")
            os.remove("database.json")
        f.close()
        log()
log()

