"""
Junyu Mou
MET CS 521 A2
Fall 2020
Final Project

"""
import datetime
''' ===============================PART(1): get personal information====================================='''
pf = input("Enter the personal information file: ")# input personal information e.g.personal information.txt
pinfo = open(pf,'r').read().splitlines()
newreport = open('report '+ datetime.date.today().isoformat()+'.txt','w')# open the report .txt file or create one
name = ''
age = ''
gender = ''
weight = ''
height = ''
''' read the file and import information to python variable'''
for i in pinfo:
    if i.startswith('name'):
        name = i[ i.find(':', 0, len(i)) + 1 : ]
        if name.startswith(' '):
            name = name[1:]
    if i.startswith('age'):
        age = i[ i.find(':', 0, len(i)) + 1 : ]
        if age.startswith(' '):
            age = age[1:]
    if i.startswith('gender'):
        gender = i[ i.find(':', 0, len(i)) + 1 : ]
        if gender.startswith(' '):
            gender = gender[1:]
    if i.startswith('weight'):
        weight = i[ i.find(':', 0, len(i)) + 1 : ]
        if weight.startswith(' '):
            weight = weight[1:]
    if i.startswith('height'):
        height = i[ i.find(':', 0, len(i)) + 1 : ]
        if height.startswith(' '):
            height = height[1:]

'''get personal information'''
class personal_information:#class output persoal information  
    def __init__(self,name,age,gender,weight,height):# init() method in class
        self.name = name 
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
    def __str__(self):# for getting the personal information __str__() method in class
        return 'name:'+ self.name + '  age:' + str(self.age) + '  gender:' + self.gender + '  weight:' + str(self.weight) + '  height:' + str(self.height)
    ''' this method write the personal infomration in report'''
    def report_prtsonal_information(self,report):
        report.write('name: ' + self.name + '\n')
        report.write('age: ' + str(self.age) + '\n')
        report.write('gender: ' + self.gender + '\n')
        report.write('weight: ' + str(self.weight) + '\n')
        report.write('height: ' + str(self.height) + '\n')
        report.write('date: ' + str(datetime.date.today()) + '\n')
        

'''print welcome ''' 
def WELCOME(name,weight):# the function welcomes the user
    print("Welcome: "+name)
    print("Weight: " + weight + 'kg')
    print("Date: ",str(datetime.date.today()))
    print()
'''RUN WELCOME '''
WELCOME(name,weight)# the welcome screen of the program, the beginning of the program 

''' ===============================PART(2): setup nutrition targets====================================='''
print("Enter nutrition goal in grams per kg of body weight.")   
'''this part ask the user to input nutrition goals '''
while True:
    pt_input = input("Enter protain goal in number, enter 0 to get default value: (default: 3g protein per kg of body weight):")
    try:
        float(pt_input)
    except:
        print("The input must be an number!")
        continue        
    pt_input_float = float(pt_input)
    if int(pt_input_float) == 0:
        pt = 3 * float(weight)
    else:
        pt = pt_input_float * float(weight)
        
    ct_input = input("Enter carbohydrate goal in number, enter 0 to get default value: (default: 4.5g carbohydrate per kg of body weight):")
    try:
        float(ct_input)
    except:
        print("The input must be an number!")
        continue       
    ct_input_float = float(ct_input)
    if int(ct_input_float) == 0:
        ct = 4.5 * float(weight)
    else:
        ct = ct_input_float * float(weight)
    break

def Nutrition_Target(pt,ct):
    print()
    print("Protein goal:",pt,'g')
    print("Carbohydrate goal:",ct,'g')
    print("weight of vegetable: 300g to 500g")
    print()
'''print nutrition target '''
Nutrition_Target(pt,ct)# calculated nutrition target will be showed after the welcome screen 
    
''' ===============================PART(3): estabilsh food library and input foods====================================='''    
foodlist = [] #food names 
foodprotein = {}# food name and protein 
foodcarbohydrate = {}#foodname and carbohydrate

'''open the files where the food information saved'''
library_fl = open("library_fl.txt",'r')
library_p = open("library_p.txt",'r')
library_c = open("library_c.txt",'r')
library_fl_read = library_fl.read().splitlines()
library_p_read = library_p.read().splitlines()
library_c_read = library_c.read().splitlines()

''' read files and input data into dictionaries and list '''
for l in library_fl_read:
    foodlist.append(l)
for l in library_p_read:
    pos = l.find(":",0,len(l))
    foodprotein[l[1 : pos]] = float(l[pos+1 : ])
for l in library_c_read:
    pos = l.find(":",0,len(l))
    foodcarbohydrate[l[1 : pos]] = float(l[pos+1 : ])    

'''make lists for food consumption '''   
vege = []
p_e_d = []
c_e_d = []
while True:
    print()
    print("Enter foods and weights, if the food is vegetable just type \"vegetable\" for name")
    foodname = input("Enter the name of the food, or type END to end the day: ")      
    if foodname == 'end' or foodname == 'END':
        break 
    
    foodweight = input("Enter the weight of the food in grams: ")
    try:
        float(foodweight)
    except:
        print("the weight of the food must be an number!")
        continue
    
    if foodname == 'vegetable':
        vege.append(float(foodweight))
    elif foodname not in foodlist:
        fp = input("Enter protein in grams per 100g of the food: " )
        try:
            float(fp)
        except:
            print("record nutrition facts failed, the protein input must be an number!")
            continue       
        if float(fp) < 0:
            print("the protein can\'t be negetive!")
            continue
        elif float(fp) > 100:
            print("error: the input is too large!")
            continue       
        fc = input("Enter carbohydrate in grams per 100g of the food: " )
        try:
            float(fc)
        except:
            print("record nutrition facts failed, the carbohydrate input must be an number!")
            continue       
        if float(fc) < 0:
            print("the carbohydrate can\'t be negetive!")
            continue
        elif float(fc) > 100:
            print("error: the input is too large!")
            continue    
        foodlist.append(foodname)
        foodprotein[foodname] = float(fp)
        foodcarbohydrate[foodname] = float(fc)
        
        p_e = ( float(foodweight) / 100 ) * float(fp)
        c_e = ( float(foodweight) / 100 ) * float(fc)
        p_e_d.append(p_e)
        c_e_d.append(c_e)
    else:
        p_e = ( float(foodweight) / 100 ) * float(foodprotein[foodname])
        c_e = ( float(foodweight) / 100 ) * float(foodcarbohydrate[foodname])
        p_e_d.append(p_e)
        c_e_d.append(c_e)

'''build a class which can be used to explore the food library in the programm '''
class explorelibrary:
    def __init__(self,fl,lp,lc):
        self.foodlist = fl
        self.foodprotein = lp
        self.foodcarbohydrate = lc
    def __str__(self):
        return 'This class can be used to explore the food library, methods: __init__(), ALLFOOD(), FOODDIC()'
    def __count(self,lst): # private method 
        self.__count = 0 # private attribute
        for i in lst:
            self.__count += 1
            count = self.__count
        return count #return value
    def ALLFOOD(self):
        for i in self.foodlist:
            print(i + ' ', end = ' ')
        print()
        print('There are',self.__count(self.foodlist),'foods so far')
    def FOODDIC(self,dic):
        if dic == self.foodprotein:
            print('Nutrition facts: protein')
        else:
            print('Nutrition facts: carbohydrate')
        for i in dic:
            print(i, ': ',dic[i],'g')
        print('There are',self.__count(self.foodlist),'foods so far')

''' ===============================PART(4): calculate nutrition consumption for the day and compare with goal====================================='''       
       
p_e_total = sum(p_e_d)# total protein consumption
c_e_total = sum(c_e_d)# total carbohydrate consumption   
vege_total = sum(vege) # total vegetable consumption  
compare_p = p_e_total - pt # difference between goal and actural consumption
compare_c = c_e_total - ct
'''write the result in txt to generate a report '''
def result_report(pt,ct,p_e_total,c_e_total,vege_total,compare_p,compare_c,report):
    report.write('\n')
    report.write("The protein goal for the day: " + str(pt) + 'g'+ "  The actual protein consumption this day: " +  str(p_e_total) + 'g' +'\n')
    report.write("The carbohydrate goal for the day: " + str(ct)+'g'+ "  The actual protein consumption this day: "+  str(c_e_total)+'g'+'\n')
    report.write("Vegetation recommanded for the day: 300g to 500g, The actual vegetation consumption: " + str(vege_total) + 'g' +'\n')     
    report.write('\n')
    if compare_p >= 0:
        report.write("The protein is enough for the day, good job!"+'\n')
    else:
        report.write("you need " + str(0-compare_p) + 'g'+' more for protein'+'\n')
    
    if compare_c >= 0:
        report.write("The carbohydrate is enough for the day, good job!"+'\n')
    else:
        report.write("you need " + str(0-compare_c) + 'g' + ' more for carbohydrate'+'\n')
        
    
    if vege_total >= 300 and vege_total <= 500:
        report.write("your vegetation consumption is in a reasonable range, good job!"+'\n')
    elif vege_total < 300:
        report.write("insufficient vegetation, you need " + str(300 - vege_total) + 'g more'+'\n')
    else:
        report.write("you may eat too much dietary fibre"+'\n')
    
    '''write a simple graph in report '''
    report.write('\n')
    report.write("  protein    target: " + (int(pt/10) * '+') + '\n' )
    report.write("  protein     eaten: " + (int(p_e_total/10) * '+')+ '\n' )
    report.write("carbohydrate target: " + (int(ct/10) * '+')+ '\n' )
    report.write("carbohydrate  eaten: " + (int(c_e_total/10) * '+')+ '\n' )
    report.close()
    
''' ===============================PART(5): save all information into txt to backup food information permanently====================================='''        
library_fl_write = open('library_fl.txt','w')  
library_p_write = open('library_p.txt','w')  
library_c_write = open('library_c.txt','w')        

for i in foodlist:
    library_fl_write.write(i + '\n')
library_fl_write.close()

for i in foodprotein:
    library_p_write.write('<' + i + ':' + str(foodprotein[i]) + '\n')
library_p_write.close()

for i in foodcarbohydrate:
    library_c_write.write('<' + i + ':' + str(foodcarbohydrate[i]) + '\n')
library_c_write.close()
       
''' ===============================RUN THER PROGRAM=====================================''' 
'''GENERATE A NEW REPORT FOR TODAY '''
pi = personal_information(name,age,gender,weight,height)# import all personal information into personalinformation class 
pi.report_prtsonal_information(newreport)# write the personal information in report

result_report(pt,ct,p_e_total,c_e_total,vege_total,compare_p,compare_c,newreport)# write all result on the reprt file(.txt)    
'''The program will generate a .txt file with today's date as part of the name, all result will written in the file, 
for each day, the program generate a new file with the date, as long as the system date change, the program will 
generate a new file. '''
print("================================================TEST PART===========================================================")
print("The result will be written into the .txt file")
print('Besides that, this program has several functions which allow users to check the data ')
print()
print('Ckeck the personal information: ')
print(pi)
print()
print("check all foods already in food library: ")
explorelibrary(foodlist,foodprotein,foodcarbohydrate).ALLFOOD()
print()
print("check protein for foods: ")
explorelibrary(foodlist,foodprotein,foodcarbohydrate).FOODDIC(foodprotein)
print()
print("check carbohydrate for foods: ")
explorelibrary(foodlist,foodprotein,foodcarbohydrate).FOODDIC(foodcarbohydrate)
print()
print("print the description for explorelibrary():")
print(explorelibrary(foodlist,foodprotein,foodcarbohydrate))        
        