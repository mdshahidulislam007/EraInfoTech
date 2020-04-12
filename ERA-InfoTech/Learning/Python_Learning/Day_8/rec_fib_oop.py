class Series:
    
 
    def fibo(self,n):
        
        if n<=1:
            return n
        else:
            return (self.fibo(n-1)+self.fibo(n-2))

s= Series()
s.fibo()
print("Fibonacci series:")
for i in range(5):   
    print(s.fibo(i))
        

