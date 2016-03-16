import random, sys
from math import fabs
malenames=['Noah', 'Liam', 'Jacob', 'Mason', 'William', 'Ethan', 'Michael', 'Alexander', 'Jayden', 'Daniel', 'Elijah', 'Aiden', 'James', 'Benjamin', 'Matthew', 'Jackson', 'Logan', 'David', 'Anthony', 'Joseph', 'Joshua', 'Andrew', 'Lucas', 'Gabriel', 'Samuel', 'Christopher', 'John', 'Dylan', 'Isaac', 'Ryan', 'Nathan', 'Carter', 'Caleb', 'Luke', 'Christian', 'Hunter', 'Henry', 'Owen', 'Landon', 'Jack', 'Wyatt', 'Jonathan', 'Eli', 'Isaiah', 'Sebastian', 'Jaxon', 'Julian', 'Brayden', 'Gavin', 'Levi', 'Aaron', 'Oliver', 'Jordan', 'Nicholas', 'Evan', 'Connor', 'Charles', 'Jeremiah', 'Cameron', 'Adrian', 'Thomas', 'Robert', 'Tyler', 'Colton', 'Austin', 'Jace', 'Angel', 'Dominic', 'Josiah', 'Brandon', 'Ayden', 'Kevin', 'Zachary', 'Parker', 'Blake', 'Jose', 'Chase', 'Grayson', 'Jason', 'Ian', 'Bentley', 'Adam', 'Xavier', 'Cooper', 'Justin', 'Nolan', 'Hudson', 'Easton', 'Jase', 'Carson', 'Nathaniel', 'Jaxson', 'Kayden', 'Brody', 'Lincoln', 'Luis', 'Tristan', 'Damian', 'Camden', 'Juan']
femalenames=['Sophia', 'Emma', 'Olivia', 'Isabella', 'Ava', 'Mia', 'Emily', 'Abigail', 'Madison', 'Elizabeth', 'Charlotte', 'Avery', 'Sofia', 'Chloe', 'Ella', 'Harper', 'Amelia', 'Aubrey', 'Addison', 'Evelyn', 'Natalie', 'Grace', 'Hannah', 'Zoey', 'Victoria', 'Lillian', 'Lily', 'Brooklyn', 'Samantha', 'Layla', 'Zoe', 'Audrey', 'Leah', 'Allison', 'Anna', 'Aaliyah', 'Savannah', 'Gabriella', 'Camila', 'Aria', 'Kaylee', 'Scarlett', 'Hailey', 'Arianna', 'Riley', 'Alexis', 'Nevaeh', 'Sarah', 'Claire', 'Sadie', 'Peyton', 'Aubree', 'Serenity', 'Ariana', 'Genesis', 'Penelope', 'Alyssa', 'Bella', 'Taylor', 'Alexa', 'Kylie', 'Mackenzie', 'Caroline', 'Kennedy', 'Autumn', 'Lucy', 'Ashley', 'Madelyn', 'Violet', 'Stella', 'Brianna', 'Maya', 'Skylar', 'Ellie', 'Julia', 'Sophie', 'Katherine', 'Mila', 'Khloe', 'Paisley', 'Annabelle', 'Alexandra', 'Nora', 'Melanie', 'London', 'Gianna', 'Naomi', 'Eva', 'Faith', 'Madeline', 'Lauren', 'Nicole', 'Ruby', 'Makayla', 'Kayla', 'Lydia', 'Piper', 'Sydney', 'Jocelyn', 'Morgan']
printing=0
nextName=0
indexesToKill=[]
def Print(*arg, end='\n', sep=' '):
    global printing
    if printing:
        arg=list(arg)
        for i in range(len(arg)):
            try:
                float(arg[i])
            except:
                pass
            else:
                arg[i]=round(arg[i],2)
        print(sep.join([str(i) for i in arg]), end=end)
def peopleIndex(index, returnSex=0):
    r=None
    sex=None
    for p in range(len(people)):
        for i in range(len(people[p])):
            if people[p][i].index==index:
                r=i
                sex=p
    if r==None:
        Print(index,'not found.')
        raise ZeroDivisionError
    if returnSex:
        r=[r,sex]
    return r
class Person():
    def __init__(self, sex, birthAttributes): #attributes=[maxHeight, maxWeight, maxAge, endGrowAge]
        global numPeopleBorn, nextName
        numPeopleBorn+=1
        self.index=numPeopleBorn
        Print('born:',', '.join([str(i) for i in birthAttributes]))
        self.sex=sex
        nextName+=1
        self.name='Person'+str(nextName)#random.choice([femalenames,malenames][self.sex])
        self.height=0
        self.maxHeight=birthAttributes[0]
        self.weight=0
        self.maxWeight=birthAttributes[1]
        self.age=0
        self.maxAge=birthAttributes[2]
        self.endGrowAge=birthAttributes[3]
        self.attributes=[self.height, self.weight, self.age] #[height, weight, age]
        self.fullyGrown=False
        self.birthAttributes=birthAttributes
        self.married=0
        self.peopleRejectedBy=[]
        self.numChildren=0
        self.numChildrenWanted=random.randint(2,3)
        self.timeSinceChild=0
        self.dead=0
    def grow(self, years):
        self.age+=years
        self.timeSinceChild+=years
        self.fullyGrown=self.age>self.endGrowAge
        if not self.fullyGrown:
            self.height=self.maxHeight*(self.age/self.endGrowAge)
            self.weight=self.maxWeight*(self.age/self.endGrowAge)
        else:
            self.height=self.maxHeight
            self.weight=self.maxWeight
        if self.age>self.maxAge:
            self.die()
    def displayInfo(self):
        Print('name:',self.name,' sex:',['female','male'][self.sex],' height:',self.height,' weight:', self.weight,' age:',self.age,sep='')
    def die(self):
        if not self.dead:
            Print(self.name,'died at age:',self.age)
            if self.married:
                try:
                    Print('widowing:',people[1-self.sex][peopleIndex(self.partnerIndex)].name)
                    people[1-self.sex][peopleIndex(self.partnerIndex)].becomeWidowed()
                except ZeroDivisionError:
                    pass
            self.dead=1
            global indexesToKill
            indexesToKill.append(self.index)
        else:
            raise SyntaxError
    #        people[self.sex].remove(self)
    def updateOtherGenderRates(self):
#        if self.fullyGrown:
        rates=[]
        otherGenderAttributes=[] #[[person1Attribute1, person2Attribute1, person3Attribute1], [person1Attribute2, person2Attribute2, person3Attribute2]]
        x=0
        for attributeIndex in range(numAttributes): 
            otherGenderAttributes.append([])
            for person in people[1-self.sex]:
                otherGenderAttributes[attributeIndex].append(person.attributes[attributeIndex]) #add attributes
                x+=1
        otherGenderAttributes[2]=[fabs(self.age-age) for age in otherGenderAttributes[2]] #difference of age
        otherGenderAttributeRates=[]
        for attributeIndex in range(numAttributes):
            otherGenderAttributeRates.append([])
            attributes=otherGenderAttributes[attributeIndex]
            for attribute in attributes:
                try:
                    otherGenderAttributeRates[attributeIndex].append((attribute-min(attributes))/(max(attributes)-min(attributes))) #from 0 to 1
                except ZeroDivisionError:
                    otherGenderAttributeRates[attributeIndex].append(.5)
        otherGenderAttributeRates[1]=[1-otherGenderAttributeRates[1][i] for i in range(len(otherGenderAttributeRates[1]))] #flip weight, because is bad
        otherGenderAttributeRates[2]=[1-otherGenderAttributeRates[2][i] for i in range(len(otherGenderAttributeRates[2]))] #flip age, because is bad
        self.attributeRatesByPerson=[sum([otherGenderAttributeRates[atributeIndex][rangepersonIndex] for atributeIndex in range(numAttributes)])/numAttributes for rangepersonIndex in range(len(people[1-self.sex]))] #order by person
    def recieveMarriageProposal(self, person):
        Print(self.name,'got proposed by:',person.name)
        self.updateOtherGenderRates()
        
        candidates=[people[1-self.sex][i].index for i in range(len(people[1-self.sex]))]
        candidates=[x for (y,x) in sorted(zip(self.attributeRatesByPerson, candidates))]
        candidates=candidates[int(len(candidates)*(1-proposalAcceptanceRate)):]
        
        if self.fullyGrown and (person.index in candidates) and (not self.married):
            Print('yes accept marriage proposal')
        return self.fullyGrown and (person.index in candidates) and (not self.married)
    def recieveChildProposal(self):
        Print(self.name,end=' ')
        Print('recieves child proposal from:',people[1-self.sex][peopleIndex(self.partnerIndex)].name)
        if not self.married:
            Print('already married to:',people[1-self.sex][peopleIndex(self.partnerIndex)].name)
            raise ValueError
        
        wantChild=self.numChildren<self.numChildrenWanted and self.timeSinceChild>3
        if wantChild:
            Print(self.name,'accept marriage proposal')
            self.timeSinceChild=0
            self.numChildren+=1
        return wantChild
    def tick(self):
        self.updateOtherGenderRates()
        if self.fullyGrown and (not self.married):
            candidates=list(range(len(people[1-self.sex])))
            candidates=[x for (y,x) in sorted(zip(self.attributeRatesByPerson, candidates))]
            candidates=candidates[int(len(candidates)*(1-proposalAcceptanceRate)):]
##            for personIndex in range(len(people[1-self.sex])):
##                if self.attributeRatesByPerson[personIndex]>1-proposalAcceptanceRate and (not people[1-self.sex][personIndex].index in self.peopleRejectedBy):
##                    candidates.append(personIndex)
            if len(candidates)>0:
                chosen=random.choice(candidates)
                Print(self.name,'sending marriage proposal')
                if people[1-self.sex][chosen].recieveMarriageProposal(self):
                    if self.sex:
                        marry(self.index, people[1-self.sex][chosen].index)
                    else:
                        marry(people[1-self.sex][chosen].index, self.index)
                else:
                    self.peopleRejectedBy.append(people[1-self.sex][chosen].index)
        if self.married:
##            if not (self.partnerIndex==people[1-self.sex][peopleIndex(self.partnerIndex)].index and self.index==people[1-self.sex][peopleIndex(self.partnerIndex)].partnerIndex):
##                Print(self.partnerIndex==people[1-self.sex][peopleIndex(self.partnerIndex)].index,self.index==people[1-self.sex][peopleIndex(self.partnerIndex)].partnerIndex)
##                Print(self.name,self.partnerIndex,people[1-self.sex][peopleIndex(self.partnerIndex)].index, people[1-self.sex][peopleIndex(self.partnerIndex)].name,people[1-self.sex][peopleIndex(self.partnerIndex)].partnerIndex)
##                raise ValueError
                
            if self.numChildren<self.numChildrenWanted and self.timeSinceChild>3 and (not people[1-self.sex][peopleIndex(self.partnerIndex)].dead):
                Print(self.name,'sending child proposal')
                if people[1-self.sex][peopleIndex(self.partnerIndex)].recieveChildProposal():
                    self.timeSinceChild=0
                    self.numChildren+=1
                    reproduce(self,people[1-self.sex][peopleIndex(self.partnerIndex)])
        self.grow(1)
        self.attributes=[self.height, self.weight, self.age]
    def becomeWidowed(self):
        self.married=0
        self.partnerIndex=None
        Print(self.name,'became widowed ;(')
def reproduce(person1,person2):
    Print(person1.name, 'and', person2.name, 'are reproducing.')
    birthAttributes=[(person1.birthAttributes[i]+person2.birthAttributes[i])/2 for i in range(numBirthAttributes)] #get average
    birthAttributes=[[birthAttributes[i],mutationAttributes[i][2],mutationAttributes[i][3]][random.choice([0]*60+[1,2])] for i in range(numBirthAttributes)] #possibly mutate
    birthAttributes=[birthAttributes[i]+((2*random.random())-1)*birthAttributesVariables[i] for i in range(numBirthAttributes)] #add variable
    sex=random.randint(0,1)
#    Print('from:',person1.birthAttributes,'and',person2.birthAttributes,'to:',birthAttributes)
    people[sex].append(Person(sex, birthAttributes))#0 is female, 1 is male
def marry(maleIndex,femaleIndex):
    i1,i2=peopleIndex(femaleIndex),peopleIndex(maleIndex)
    Print('Marriage between:',people[0][i1].name,'and',people[1][i2].name, '(',maleIndex,',',femaleIndex,')')
    people[0][i1].married=1
    people[1][i2].married=1
    people[0][i1].partnerIndex=people[1][i2].index
    people[1][i2].partnerIndex=people[0][i1].index
def randomFloat(a,b):
    return random.random()*(b-a)+a
def randomAttributes():    
    return [randomFloat(mutationAttributes[i][0],mutationAttributes[i][1]) for i in range(numBirthAttributes)]
def average(l):
    j=0
    try:
        j=sum(l)/len(l)
    except ZeroDivisionError:
        pass
    return round(j,2)
proposalAcceptanceRate=1
numPeopleBorn=-1
mutationAttributes=[[5,7 ,3,8],[100,200 ,50,300],[60,100 ,40,120],[15,21 ,13,25]] # averageLow,averageHigh ,mutationLow,mutationHigh
birthAttributesVariables=[1,20,10,3] #variable for attributes
numBirthAttributes=4
numAttributes=3

startNumPeople=20

people=[[Person(0,randomAttributes()) for i in range(int(startNumPeople/2))],[Person(1,randomAttributes()) for i in range(int(startNumPeople/2))]]

year=0
data=[['year','people','average height','average weight', 'percentage married:']]
p=1
while len(people[0])+len(people[1])>0 and year<=400:
    fGen=0
    for gender in people:
        for person in gender:
#            person.displayInfo()
            person.tick()
            if person.index<startNumPeople:
                fGen+=1
    if fGen==0 and p:
        p=0
    if len(indexesToKill)>0:
        Print('killing:',indexesToKill)
    for i in indexesToKill:
        f=peopleIndex(i,1)
        Print('killing person:',f)
        people[f[1]].pop(f[0])
    indexesToKill=[]
    year+=1
    data.append([year,len(people[0])+len(people[1]),average([p.height for p in people[0]+people[1]]),average([p.weight for p in people[0]+people[1]]),int(average([p.married for p in people[0]+people[1]])*100)])
    print('year:',data[-1][0],'people:',data[-1][1],'average height:',data[-1][2],'average weight:',data[-1][3],'percentage married:',data[-1][4])
Print('The human race is extinct')
try:
    import xlsxwriter
    Print('opening workbook...')
    workbook = xlsxwriter.Workbook('evolution data.xlsx')
    Print('saving...')
    worksheet = workbook.add_worksheet()

    for row in range(len(data)):
        for column in range(len(data[row])):
            worksheet.write(row,column,data[row][column])
    workbook.close()
except:
    print("Couldn't save to excel file, download 'xlsxwriter'")
