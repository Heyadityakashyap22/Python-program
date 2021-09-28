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

mystr="Aditya"
print(mystr[-1:-2])
print(len(mystr))# ab agar ek ek chor ke print karwaana vchahte hoo tohh (mystr[0:5:2])  aise likhnaa cchaiye or agar aap  kuch nii likhte hai tohh like print(mystr[:]) ye yaa print(mystr[::]) toh ye puri print kare gaa
#or agar ek ek miss karwana hai to [0:6:2] aise likhe gaa toh ek ek miss kare kee likjhee gaa  agra  2 2 charactor miss karwaana hai to [:3] ye likh ne se 2 2 char. miss hoo gaa
#agar tum  jada number likh te hoo to like [::59959959] toh ye  jitna resolver kare gaa utna hi kare gaa




