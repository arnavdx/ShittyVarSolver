# importing library sympy 
from sympy import *
import tkinter as tk
import sys
while True:
    top=tk.Tk()
    top.title("VarCalc Solver");
    entries=[]



    frame=tk.Frame()
    def boxe():
        global eq1,ev,var
        exp.config(state='disabled')
        ev=str(exp.get())     #for getting vars"
        c=0
        l=sympify(ev.split("=")[0])
        r=sympify(ev.split("=")[1])
        eq1=Eq(l,r)
        var=eq1.free_symbols
        for items in var:
            c+=1
            myvar = tk.StringVar()
            myvar.set('')
            
            
            ghk= tk.Entry(master=frame,width=5, relief=tk.SUNKEN, borderwidth=5, textvariable=myvar)
            ghk_label=tk.Label(master=frame,text=items)
            ghk.grid(row=2,column=c)
            myvar.trace('w',jk)
            ghk_label.grid(row=1,column=c)
            entries.append(myvar)
        btn.grid_forget()
        
        print(var)

        end.grid(column=3,row=2)
        jk(1,1,1)
        
        
    btn=tk.Button(text="Calculate", command=boxe, master=frame)
    
    
    
    def jk(a,b,c):
        global eq1,ev,ans,var
        st=eq1        
        for entry,i in zip(entries, var):
            x=str(entry.get())
            print("\n\n\nx= ",x)
            st=st.subs(i,x) 
            print('st')
        an=solve(st,dict=True)
        print(an)
        ans.grid(column=1,row=3)
        if st==sympify(false):
            print("yes")
            ans.config(text='False', font=("Arial", 25))
        elif st==sympify(true):
            ans.config(text='True', font=("Arial", 25))
        else:
            ans.config(text='\n'.join("{} = {}".format(k, v) for lol in (range(len(an))) for k, v in an[lol].items()), font=("Arial", 25))     #☝prety dict
        end.grid(column=3,row=3)
    
    
    
    def restart():
        top.destroy()
    end=tk.Button(command=restart, text="Input new Equation")
    
    
    
    def endall():
        top.destroy()
        sys.exit()
    top.protocol("WM_DELETE_WINDOW", endall)

    ans=tk.Label(height=0,width=0)
    exp = tk.Entry(width=50, relief=tk.SUNKEN, borderwidth=5)






    exp.grid(column=1,row=1,pady=(7,10))
    btn.grid()





    frame.grid(column=1,row=2)

    top.mainloop()
