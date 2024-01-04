
class Category:

    name=''
    strCategory=''
    ledgerList=[]
    ledger=[]
    maxlen=0

def __init__(self,name):
     self.name=name
    


def getMaxLen(a):
    l=0
    i=0

    while(True):  
        x=a[i]
        for key in x.keys():
         v=x[key]
         if(l<len(str(v)) and type(v) is int):
             l=len(str(v))
        i=i+1
        if(i>=len(a)):
            break   

    return l    

def printBudget(self):
     self.PrintDesc(self.name)
     self.maxlen=self.getMaxLen(self.ledgerList)
     i=0
     while(True):
          if(i<len(self.ledgerList)):
               printItems(self,self.ledgerList[i],self.maxlen)
               i=i+1
          else:
               break
                    
def printItems(self,x,maxlen):
    for key in x.keys():
        k=key
        v=x[key]
        while(True):
            if(len(k)<23):
                k=k+' '
            else:
                while(True):
                    if(len(str(v))<maxlen ):
                         v=' '+v
                    else:
                         break        

                k=k+str(v)
                break

        print(k)   
    
def PrintDesc(self,Title):
        m=(30-len(Title))/2
        i=0
        str=""
        while(True):
            str=str+"*"
            i=i+1
            if(i>m):
                i=0
                break; 
        str=str+Title
        while(True):
            str=str+"*"
            i=i+1
            if(i>m):
                i=0
                break;   
        str=str+'*'

        return str

def PrintTotal(self):
 
    l=0
    i=0
    total=0
    while(True):    
        x=self.ledgerList[i]
        for key in x.keys():
         v=x[key]
         if(l<len(str(v)) and type(v) is int):
             total=total+v
        i=i+1
        if(i>=len(self.ledgerList)):
            break   

    print ("total:"+str(total) )   

def deposit(self,amount,description): 

        self.ledgerList.append({"amount": amount, "description": description})     
        if(description==""):
            return ""
 
def withdraw(self, amount,description):
        self.ledgerList.append({"amount": -amount, "description": description})
   
def get_balance(self):

        y=len(self.strCategory)
        m=(30-y)/2
        prntCat=''

        while(True):
            prntCat=prntCat+'*'
            m=m-1
            if(m==0):
                break
        prntCat=prntCat+self.strCategory

        while(True):
            prntCat=prntCat+'*'
            m=m-1
            if(m==0):
                break

            print(prntCat)
        for x in self.thislist:
            #print the category
               self.ledgerList=""
                
def printGraph(self ):
    x=''
    a='',
    b='',
    c='',
    adesc='',
    bdesc='',
    cdesc=''

    while(True):
          if(z<len(self.ledgerList)):
               x=self.ledgerList[z]
               for key in x.keys():
                    if(z==1):                       
                        a=x[key]
                        a=adesc

                    if(z==2):                       
                        b=x[key] 
                        b=bdesc   

                    if(z==3):                       
                        c=x[key] 
                        c=cdesc   


               z=z+1
          else:
               break

    self.le
    
    i=100
    a_roundoff=int(a/10)*10
    b_roundoff=int(b/10)*10
    c_roundoff=int(c/10)*10

    print(a)
    print(b)
    print(c)


    prntStr=''


    line1=''
    line2=''
    line3=''

    if(a>=b):
            if(a>=c):
                line1=adesc
                if(b>=c):
                            line2=bdesc                    
                            line3=cdesc
                else:
                            line2=cdesc
                            line3=bdesc  
            else:    
                line1=bdesc      
                if(a>=c):
                            line2=adesc                    
                            line3=bdesc
                else:
                            line2=cdesc
                            line3=adesc                 
                        

    
    else:
            if(b>=c):
                line1=bdesc
                if(a>=c):
                            line2=adesc                    
                            line3=cdesc
                else:
                            line3=cdesc   
                            line2=adesc

            else:  
                 line1=cdesc    
                 if(a>=b):
                            line2=adesc                    
                            line3=bdesc
                 else:
                            line3=bdesc   
                            line2=adesc             



    while(True):

         
            prntStr=' '+str(i)+'|'

            if(len(str(i))<2):
                  prntStr='  '+str(i)+'|'
            elif(len(str(i))==3):     
                  prntStr=''+str(i)+'|'
            else:
                 prntStr=' '+str(i)+'|'

            if(a_roundoff>=i):
                prntStr=prntStr+'  0'
            if(b_roundoff>=i):               
                prntStr=prntStr+'  0'  
            if(c_roundoff>=i):
                prntStr=prntStr+'  0'    



            print(prntStr)
            print('\n')
            i=i-10

            if(i<0):
    
                print('    -----------------')


                i=0
                j=0
                k=0
                strPrntName='    '
                while(True):
                      strPrntName='      '
                      if(i<len(line1)):
                            strPrntName=strPrntName+line1[i]+'  '

                      if(j<len(line2)):
                            strPrntName=strPrntName+line2[j]+'  ' 

                      if(k<len(line3)):
                            strPrntName=strPrntName+line3[k]+'  '     
                            
                      i=i+1
                      j=j+1
                      k=k+1

                      print (strPrntName)
                      print ('\n')
                      
                       
                      if( i>=len(line1) and j>=len(line2) and k>=len(line3) ):
                            break


                break

    





c=Category('Grocrry')
c.deposit('1000','Grocerry')






 

        



   
       

    

    


