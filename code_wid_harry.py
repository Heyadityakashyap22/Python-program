#comment kya hota hai es lecture me hum jaane gaye

"""adi
anu
aman
aditya kashyap"""


"""print("Subscribe Tashanditya",end=" please ")
print("Bhai log subscribe v kar do"""



#print("c:\nsubscribe") out put is c: subscribe(nexdt line me ) becxause \n is a new line character
#if you want to us forwardslash seaflly  write

#print("c:\\subscribe") use doubble \\(forward slash) output is c:\subscribe


#now i want to write

#rint("aditya is a \n good boy \t1")  ab \t is also a escape character jo ki space  dene kaa kaam kar taa hai
# new line \t= space \"= ye couart deta hai single ya double  esko hum strings ke bich me laga  saktwe hai


#           tute:- 8

"""var1="56" #string variables jiss ko aap wase ke wase hi store kar na chate hoo
var2=4 #ye ek number hai or number me v ye ek integer hai  es liye ye ek int.. hai
var3=56.7
var4="45"
var5=55555#float ye ek floating point variabler hai es ka matlab ye decimal value le sakta hai
#an python etna tezz hota hai ki ye esko  typr  de deta hai toh lets see TYPE"""

"""print(int(var4)+int(var1))
var1="56"
var4="45" agr en do string ko add kar na  hai to appp ko print(int(var4)+int(var1)) aais e print karwaana hoo gaa NOTE= do dtring jab add hota hai contniate hoo jata hai """
#esi function ko ##typecast kahte hai
"""esi trh aapp kiss v variable me typecast kar sakte hai
(var=str
 var=int
 var=float)"""

#print(100 * str(int(var1)+int(var2))) # mai aap ko bata duu agar aap no. ke sath karnaa chate hai too app koo plhe jo int hai usko str me typecast kar naa hoo jiase hum ne program me kiya hai

#print(1 * "hello world\n")# agar tum helloo world ko 10 1000 baar print karwaana chahte hoo to  10* helloo world likh ke karwaa sakte hai

"""<class 'str'>
<class 'int'>
<class 'float'>"""
# toh ye theer typr kr variables  hai\\\\\\   Ab yaha hum agar  var 1 + var2 kiya jaaye to  ye  output  dega  60.7 wahi agar var1 + var 2 kiya  jaaye toh  ye error degaa q ki python ye  samjh nii paaya ......
#but  agar  tum do trh ke string ko add kaeroo gaye to error  nii mile gaa  like var1+var4 then u will get   hello world aditya


"""
#if you want to take3 input from user tooh tum ko input ka  use kar na hoo gaa

print("Enter ypur number")
inpnum=input()# maine yaha input function kaa use kiyaa ab aap joo v number  daale  gaye woo  asd a string   print  hoo ga(as as string)

print("you Entred ", int(inpnum)/1.57)
# ab jub yee aagaya  to mujhe  es nu8mber me 10 add karwaanne hai to NOTE= log genrelly ye  kar te hai print("you entred",inpnum+10 but ye  glat hai q ki
#ye inpnum ek string hai tum uskoo ek int se addd kar ne  jaa rahe  hoo to kase hoo un have too change  string to int like int(inpnum+10) aise kar ke  )"""
"""
#Callculator kaise banta hai

print("Please Enter Your Number")
inpnum1=(input())
print("Please Enter Your Another Number")
inpnum2=(input())
print("Your Answer Is",int(inpnum1) + int(inpnum2)) #{app esme kuch v kar sakte hoo like divdision, multiolication, addition, substraction but haa aap joo  varaiable kaa dayan  rakhnaa hoo gaa}
"""
#tut9
#String slicing
"""
mystr= "Aditya singh kashyap is a good boy"
print(len(mystr))
print(mystr[0:6])# python me index zero se start hooti  hai A=0 d=1 i=2 t=3 y=4 a=5  toh mujhe isko sclicing karni hai like print(mystr[4])  Ab hum ko  tukra chahiye
#uske liye maan lo 0:5 print adity hoga q ki eska rule hoota hai ki 0 toh including hooga but 5 excluding hoo gaa esi liye 0:6 likhnaa pare gaa
# ab agar tum chahte hoo ki  aap ke line me  kitne  character hai  wo pata  chale too [len] ka use hota hai.....
print(mystr[0:34]) # hum ko ek jada  likhnaa hota hai"""
"""
mystr="Aditya"
print(mystr[::-1])
print(len(mystr))# ab agar ek ek chor ke print karwaana vchahte hoo tohh (mystr[0:5:2])  aise likhnaa cchaiye or agar aap  kuch nii likhte hai tohh like print(mystr[:]) ye yaa print(mystr[::]) toh ye puri print kare gaa
#or agar ek ek miss karwana hai to [0:6:2] aise likhe gaa toh ek ek miss kare kee likjhee gaa  agra  2 2 charactor miss karwaana hai to [:3] ye likh ne se 2 2 char. miss hoo gaa
#agar tum  jada number likh te hoo to like [::59959959] toh ye  jitna resolver kare gaa utna hi kare gaa  (::-1) agar aap koo ulta kar naa hai to ye use karoo string ulta hoo jayen gaa
"""

         #alpha numric character  functions
"""
mystr="aditya kashyap have a youtube channal please subscribe Tashaditya"#Python isnumeric() method checks whether all the characters of the string are numeric characters or not. It returns True if all the characters are true, otherwise returns False. Numeric characters include digit characters and all the characters which have the Unicode numeric value property.
print(mystr.isalnum())# their is a bullion deta type in a python aslo  *** ab agar ab ko true or false dekh na hai to ye use karoo agar jo [mystr.isnum() use kae ne se ye false bataye gaa q ki esme space ko wo count kare ta hai us space me string ni hai ab agar space hata ke dekhoo ye true print karwaaye gaa
#esko ****alpha numaric kahte hai true wlw koo
print(mystr.isalpha()) # fir vv ye false dega q ki numaric toh hai hi  ni  or space v aagai hai
print(mystr.endswith("youtube")) #ab agar chahte hoo ki ye bataye ki kya tumhara santance youtube se end karta hai yaa nii tohh ye function use karoo output= false
print(mystr.endswith("channalu")) #ab yaha kya huaa agar tumhara santance given word se end kare gaa toh ye true print karwaaye ga output=true or agar tum spelliung v galt karoo gaye too v yee false hiii dekhaaye gaa
print(mystr.endswith("channal"))# dekha right likh ne se ye tr4ue print karwaaye gaa False


aditya
aman
anubhav

print(mystr.count("a")) # es wale function se tum count kar sakte hoo kii es string me is kon sa letter kitni baar hai like "a" output aaya 7
print(mystr.capitalize())# ye function lagane se ye ek starting ke letter koo captil kar degaa
print(mystr.find("channal")) #YE FUNCTION STRING ME SE word ko dundh taa hai
print(mystr.lower())#es function se tum apne pure string ko small{lower me  kar deta hai }
print(mystr.upper())# es function se tum apne string ko captial letter me  kar salte haii ....
print(mystr.replace("aditya","ankit")) #ye functhion se aap apne string ke kisi word ko replace kar skte hai like aditya koo maine ankit se kar diya
"""

"""
                                        1                 #Python Lists And List Functions |tut1
numbers=[2, 30, 24, 15, 46, 0.7, 9]#app es me float ko v sort kar sakte hai
#numbers.sort()
#numbers.reverse()#app number ko reverse v kar sakte hai ye wala function use kare ke
#print(numbers[3])# ye sub aani chiye aap kase numbers me se ek particular ko print karwaa saktete hoo
print(numbers[:])# AAP slicing  kar te hai like app es trh se v kar saktre hai or sare tarike hai like [:7],[:]
#toh yee jo  hoti hai naa esko defult values hoti hai yaha pee
print(numbers[1:])# ab agar tum kisi number ko remove kar nachate hoo to ye kar sakte hoo yaa fir oe dekhoo
print(numbers[1:4])
""""[2, 30, 24, 15, 46, 0.7, 9]"""
#[30, 24, 15, 46, 0.7, 9]        ye dusra haii  [30, 24, 15]
#output hai ye
"""
print(numbers[1:7])#[30, 24, 15, 46, 0.7, 9] ye output hai

#extanded slice
#ye ek naya para metre hoota haii
print(numbers[:])# etne pe eska parameter by defult ek zero hota hai or ek length hoota hai
print(numbers[::])# yahape v ye pura hi print karwaa ye gaa q ki by defult last parametre eska 1 hota hai dekhoo
print(numbers[::1])#[2, 30, 24, 15, 46, 0.7, 9]
#[2, 30, 24, 15, 46, 0.7, 9]
#[2, 30, 24, 15, 46, 0.7, 9]
#ab agra 1 ki jagah 2 likha jaaye toh kya hoo gaa ye ek ko skip maare gaa print karwwaye gaa like.....
print(numbers[::2])#[2, 24, 46, 9] ye dekhoo but yehi hum 3 like too
print(numbers[::3])# ab ye do uchale gaa ......[2, 15, 9]
print(numbers[::-1])# ye -1 lagane se pure number ko reverse kar diya but kabhi v -1 se kam naa le number warnaa aap ko lage gaa ki ye kaam kar rah hai but aaisa kuch ni hai
print(numbers[::-3])# just like aaise
print(numbers[1:7:2])# ye confused hoo gaya mai

# ab kuch functions pe aate hai
print(len(numbers))# es se aap ke numbers ka length pata chal jaata hai    7
print(max(numbers))# ye max use kar ne se aap ke numbers me se kon sub se bara hai wo pata chale gaa    46
print(min(numbers))# es wale se aap  ke numbers me  sub se chota kon sa woo bataaye ga    0.7
# ab aate hai append pe  append kaa matlan hoota hai list ke numbers me  keo numbers aadd kar na
numbers.append(5)

print(numbers)# dekha  aap ne kaise ye 5 add kar diyta number mee     [2, 30, 24, 15, 46, 0.7, 9, 5]
numbers.append(5)
numbers.append(5)
numbers.append(5)
numbers.append(5)"""
#print(numbers)#es se ye 5 4 baar add hoo gaa    [2, 30, 24, 15, 46, 0.7, 9, 5, 5, 5, 5]
# kabhi kabhi loog khali list print karte hai or fir baad me number daate hai

"""
list=[1, 2, 3, 43, 45, 5]
#list.append(71)
#list.append(71)
#list.append(71)
#list.append(71)
#print(list) # ye dekhoo [71, 71, 71, 71] es ne  ye 4 baar print karwqaaa diya app keo v number loo 71 ki jagahh
list.insert(1, 56)
list.insert(4, 56)
print(list) # ab ye hoota hai insert function agar tum kahi v kar sajte hoo maine  yah pe 1 ke bad 56 ko karwway hai    [1, 56, 2, 3, 43, 45, 5]
#[1, 56, 2, 3, 56, 43, 45, 5]       ye dekhoo tum kahi v kar sajkte hoo insert"""
friends = ['Aditya', 'Aman', 'Anubhav', 'Mukesh']
for friend in friends:
    print("Hi " + friend)

 friend = [""]