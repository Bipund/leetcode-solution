class Solution:
    def reverse(self, x):
        self.x=x;
        b=0;
        if x>0:
            while x>0:
                c=x%10;
                b=b*10+c;
                x=x//10;
            if(b<=2147483648):
                return (b);
            else:
                return(0);
       
        if x<0:
            x=x*(-1);
            while x>0:
                c=x%10;
                b=(b*10)+c;
                x=x//10;
            if(b<=2147483648):
                return (b*(-1));
            else:
                return(0);
        if x==0:
            return (0);
    
        
            
       
                    
                
                    
                

                    

        
        
        
        
           
