class Taxpayers:
    
    def kappa(self,vat_number,children,income,tax):
        
        self.vat_number=vat_number
        self.children=children
        self.income=income
        self.tax=tax
        
    def kippo(self,children,income):
        
        if self.income<12000:
            self.tax=(self.income*(10/100))
        if self.income>12000:
            self.tax=(self.income*(15/100))
        if self.children>0:
            self.tax-=self.tax*self.children/10
        self.tax+=-taxx
            
def keppo(vat_number,children,income,taxx):
    
    k=Taxpayers()
    k.kappa(vat_number,children,income,taxx)
    k.kippo(children,income)
    print(" Το ΑΦΜ είναι : ",k.vat_number, ","," τα παιδιά είναι : ",k.children,","," το εισοδημά είναι : ",k.income," και ο φόρος είναι : ",k.tax)
    return k.tax

filetoberead=open("samostax.txt","r")
f=filetoberead.read()
allnum=[float(a) for a in f.split() if a.replace('.','').isdigit()]
zed=0
vat_number=0
children=0
income=0
taxx=0
fullincome=0
while(zed<len(allnum)):
    vat_number=allnum[zed]
    zed+=1
    children=allnum[zed]
    zed+=1
    income=allnum[zed]
    zed+=1
    taxx=allnum[zed]
    zed+=1
    fullincome+=keppo(vat_number,children,income,taxx)
    print(" Το συνολικό εισόδημα είναι : ",fullincome)
    
    


