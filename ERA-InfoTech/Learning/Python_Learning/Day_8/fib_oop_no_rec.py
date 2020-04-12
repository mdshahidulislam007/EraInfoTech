class Series:

    def fibo(self,n):
        
        print("Fibonacci Series of term ",n,":")
        n1=0
        n2=1
        for i in range(n):
            if i<=1:
                next=i
            else:
                next=n1+n2
                n1=n2
                n2=next
            print(next)
            

s = Series()
s.fibo(int(input("Please enter the number of Terms of the series: ")))
                
