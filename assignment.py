class Inform:
    def __init__(self, name, pnumber, sex):
        self.name = name
        self.pnumber = pnumber
        self.sex = sex

    def introduce_inform(self):
        print("이름은 %s, 전화번호는 %s, 성별은 %s입니다." %(self.name,self.pnumber,self.sex))

a = []
while(True):
    name = input("이름을 입력하세요 : ")
    if name=='그만':
        break
    pnumber = input("전화번호를 입력하세요 : ")
    sex = input("성별을 입력하세요(male이나 female로 작성해주세요.) : ")
    
    if sex == "male" or sex == "female":
        a.append(Inform(name,pnumber,sex))
    else:
        sex = "unknown"
        a.append(Inform(name,pnumber,sex))
    
    for i in a:
        i.introduce_inform()
    print()

for i in a:
    i.introduce_inform()

    
    
