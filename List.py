# mehmonlar=['Ali','VAli','HAsan','husan']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 kuni uchrashuvda kutamiz")
    
# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son}ning kvadrati {son**2} ga teng")

# friends=[]
# print("enter 5 clothest friend:")
# for n in range(5):
#     friends.append(input(f"enter name of {n+1} friend "))
#     print(friends)

# number=float(input("Enter number"))
# print (number**(1/2)) if number>0 else print('Enter positive number!')

# menu=['osh','qozonkabob','somsa','norin','shashlik','manti']
# buyurtmalar=['osh','norin','somsa','manti','shashlik','chuchvara']
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"menuda{taom} bor")
#     else: 
#         print(f"menuda{taom} mavjud emas")

# 4 yoshdan kichik bolalarga bepul, 4 va 12 oralig'i 50000 so'm, 12 yoshdan kattalarga 70000 so'm.
# mijoz=int(input("Iltimos yoshingizni kiritng:"))
# if mijoz<4:
#     print("Kirish bepul")
# elif mijoz<=12:
#     print("50000")
# else :
#     print("Sizga kirish 70.000")


# mijoz=int(input("Iltimos yoshingizni kiriting:"))
# if mijoz<4:
#     print("sizga kirish 5000")
# elif mijoz<=12:
#     print("siz uchun chipta narxi 50000")
# else:
#     print("siz uchun narx 70000")


# kun=input("Bugungi kunni kiriting:")
# if kun.lower()=='yakshanba' or kun.lower()=='shanba':
#     print("bugun dam olish kuni")
# else:
#     print("bugun ish kuni")


# kun=input("kunni kiriting:")
# harorat=float(input("Harorartni kiriting"))
# if (kun=='yakshanba' or kun=='shanba') and harorat>=36:
#     print("bugun cho'milishga boramiz")
# else:
#     print("bugun cho'milish atmen")

#true false qiyimat uchun tekshirish
narh=15000
choy=True
salat=False
if choy and salat:
    narh=narh+10000
elif choy or salat:
   narh=narh+5000
print(f"Jami:{narh} so'm")