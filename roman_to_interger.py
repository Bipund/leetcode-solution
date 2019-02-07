class Solution:
    def romanToInt(self, s):
        self.s=s;
        s=list(s)
        a=list(s)
        for i in range(len(s)):
            if (s[i]=="I"):
                a[i]=1;
            if(s[i]=="V"):
                a[i]=5;
            if(s[i]=="X"):
                a[i]=10;
            if(s[i]=="L"):
                a[i]=50;
            if(s[i]=="C"):
                a[i]=100;
            if(s[i]=="D"):
                a[i]=500
            if(s[i]=="M"):
                a[i]=1000;s
        j=0;
        res=0;
  
        while (j < len(a)):
            s1 =(a[j]) 
  
            if (j+1 < len(a)):
    
                s2 =(a[j+1]) 
  
                if (s1 >= s2):
                    res = res + s1 
                    j = j + 1
                else:
                    res = res + s2 - s1 
                    j = j + 2
            else: 
                res = res + s1 
                j = j + 1
        return(res)
