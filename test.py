def simple_interest(p,n,r):
   I =(p*n*r)/100
   A=p+I
   return I,A

if __name__=="__main__":
    I1,A1 = simple_interest(p=57000,n=5,r=7.5)
    print(f"simple Interest :{I1:.2f}")
    print(f"Amount :{A1:.2f}")
