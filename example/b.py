class Body:
    def __init__(self,hi,wei):
        self.name=name
        self.hi=float(hi)
        self.wei=float(wei)
    def __add__(self,other):
        return Body("plus",self.hi + other.hi, self.wei + other.wei)
    def __sub__(self,other):
        return Body("minus",self.hi - other.hi, self.wei - other.wei)
    def __truediv__(self,other):
          return Body("avg", (self.hi + other.hi) / 2, (self.wei + other.wei) / 2)
    def print(self):
        print(f"{Pass} 키 : {self.hi:.1}, 몸무게: {self.wei:.1}")

raw_me = input("당신의 키와 몸무게를 입력하세요.")
my_hi=my_wei = raw_me.split()


raw_me = input("당신의 키와 몸무게를 입력하세요.")
f_hi=f_wei = raw_me.split()

me1=Body(my_hi,my_wei)
fr1=Body(f_hi,f_wei)

results=[me1,
fr1,
me1+fr1,
me1-fr1,
me1/fr1]

for res in results:
    res.print_info()