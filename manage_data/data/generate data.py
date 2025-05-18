import random
import json

# Sample data to generate 100 entries
uzbek_first_names = [
    "Olimjon", "Gulnoza", "Sardorbek", "Dilbar", "Shahzod", "Nilufar", "Javohir",
    "Malika", "Anvar", "Nodira", "Zafar", "Umida", "Oybek", "Dildora", "Rustam", 
    "Shoira", "Kamol", "Rayhona", "Shoxrux", "Muslima", "Islom", "Nozima", "Jasur", 
    "Shahnoza", "Bobur", "Zilola", "Ulug'bek", "Ziyoda", "Farhod", "Go'zal"
]

uzbek_last_names = [
    "Tursunov", "Ergasheva", "Mamatqulov", "Karimova", "Islomov", "Abdurahmonova", 
    "Rustamov", "O‘ktamova", "Jo‘rayev", "Sattorova", "Xudoyberdiyev", "Aliyeva", 
    "Mahmudov", "Solieva", "Nurmatov", "Toshpulatova", "Sodiqov", "Toshpo'latova", 
    "Rasulov", "Murodova", "Toirov", "Qodirova", "Berdiev", "Raufova", "Sherzodov"
]

eye_diseases = [
    ("Katarakta", "https://cdn.futura-sciences.com/sources/images/diaporama/1536-loeil-et-la-vision/album-oeil11.jpg"),
    ("Glaukoma", "https://www.researchgate.net/publication/235424200/figure/fig4/AS:393339380748311@1470790824925/Fond-doeil-gauche-normal-chez-un-sujet-age-de-47-ans-Petite-pupille-cliche-central.png"),
    ("Kon'yunktivit", "https://laretina.com/wp-content/uploads/2017/02/macularpucker-lar-s.jpg"),
    ("Retinopatiya", "https://superzrenie.com/wp-content/uploads/2016/06/diabetich-retinopatiya.jpg"),
    ("Quruq ko'z sindromi", "https://internist.ru/upload/iblock/5c9/5c9134cdc6862725a6e7949205e00073.jpg"),
    ("Astigmatizm", "https://glazalazer.ru/images/stories/laz_lechenie/deab_retinopatia/diab_retinopatia2.jpg"),
    ("Diabetik retinopatiya", "https://mgkl.ru/assets/images/images/diabetich.jpg"),
    ("Ko‘z yallig‘lanishi", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Fundus_photograph-normal_retina_EDA06.JPG/250px-Fundus_photograph-normal_retina_EDA06.JPG"),
    ("Makula degeneratsiyasi", "https://ophtalmologie-antibes.com/wp-content/uploads/2022/05/800px-Fundus_photograph_of_normal_right_eye.jpg"),
    ("Blefarit", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Human_eye1.jpg/320px-Human_eye1.jpg")
]

# Generate dataset
def generate_uzbek_eye_dataset(num=100):
    data = []
    for _ in range(num):
        name = f"{random.choice(uzbek_first_names)} {random.choice(uzbek_last_names)}"
        age = random.randint(18, 80)
        disease, image_url = random.choice(eye_diseases)
        data.append({
            "name": name,
            "age": age,
            "disease": disease,
            "image_url": image_url
        })
    return data

# Generate the dataset
dataset_100 = generate_uzbek_eye_dataset(100)


# Save the dataset as a Django fixture-style JSON file
import uuid

# Convert to Django fixture format
# Recreate the fixture using integer primary keys (1 to 100)
django_fixture_int_pk = []
for i, entry in enumerate(dataset_100, start=1):
    fixture_item = {
        "model": "app.Patient",  # Replace with your actual app and model name
        "pk": i,
        "fields": {
            "name": entry["name"],
            "age": entry["age"],
            "disease": entry["disease"],
            "eye_image_url": entry["image_url"]
        }
    }
    django_fixture_int_pk.append(fixture_item)

# Save to JSON fixture file
fixture_path_int = "eye_disease_fixture_intpk.json"
with open(fixture_path_int, "w", encoding="utf-8") as f:
    json.dump(django_fixture_int_pk, f, ensure_ascii=False, indent=2)

fixture_path_int

# Re-run after code state reset to regenerate the 100 fake Uzbek employee fixture

# import random
# import json

# # Sample Uzbek names and job titles
# first_names = [
#     "Olim", "Gulnoza", "Sardor", "Dilbar", "Shahzod", "Nilufar", "Javohir",
#     "Malika", "Anvar", "Nodira", "Zafar", "Umida", "Oybek", "Dildora", "Rustam", 
#     "Shoira", "Kamol", "Rayhona", "Shoxrux", "Muslima", "Islom", "Nozima", "Jasur", 
#     "Shahnoza", "Bobur", "Zilola", "Ulug'bek", "Ziyoda", "Farhod", "Go'zal"
# ]

# last_names = [
#     "Tursunov", "Ergasheva", "Mamatqulov", "Karimova", "Islomov", "Abdurahmonova", 
#     "Rustamov", "O‘ktamova", "Jo‘rayev", "Sattorova", "Xudoyberdiyev", "Aliyeva", 
#     "Mahmudov", "Solieva", "Nurmatov", "Toshpulatova", "Sodiqov", "Toshpo'latova", 
#     "Rasulov", "Murodova", "Toirov", "Qodirova", "Berdiev", "Raufova", "Sherzodov"
# ]

# occupations = [
#     "Oftalmolog", "Hamshira", "Texnik xodim", "Laborant", "Sterilizatsiya xodimi",
#     "Administrator", "Retinolog", "Optometrist",
#     "Receptionist", "Xavfsizlik xodimi", "Marketing mutaxassisi",
#     "Tibbiy yordam xodimi",
#     "Ko'z shifokori",
# ]

# def generate_phone_number():
#     return "+9989" + str(random.randint(100000000, 999999999))

# # Generate 100 fake employees
# employees = []
# for i in range(1, 41):
#     name = f"{random.choice(first_names)} {random.choice(last_names)}"
#     occupation = random.choice(occupations)
#     phone = generate_phone_number()
#     employees.append({
#         "model": "app.Staff",  # Replace 'app' with your actual app name
#         "pk": i,
#         "fields": {
#             "name": name,
#             "occupation": occupation,
#             "phone": phone
#         }
#     })

# # Save to JSON fixture
# employee_fixture_path = "employee_fixture.json"
# with open(employee_fixture_path, "w", encoding="utf-8") as f:
#     json.dump(employees, f, ensure_ascii=False, indent=2)

# employee_fixture_path
# import json

# # 50 eye diseases with detailed descriptions in Uzbek
# diseases_with_info = [
#     {
#         "name": "Katarakta",
#         "description": "Ko‘z gavhari (linza) xiralashuvi bilan tavsiflanadi. Ko‘rish asta-sekin susayadi, ayniqsa yoshi katta odamlarda ko‘p uchraydi. Jarrohlik yo‘li bilan davolash mumkin."
#     },
#     {
#         "name": "Glaukoma",
#         "description": "Ko‘z ichi bosimining ortishi natijasida ko‘rish nervi zararlanadi. Dastlab belgilar bilinmasligi mumkin, lekin vaqt o‘tishi bilan ko‘rlikka olib keladi."
#     },
#     {
#         "name": "Kon'yunktivit",
#         "description": "Ko‘zning tashqi qavati – kon'yunktivaning yallig‘lanishi. Virusli, bakterial yoki allergik shakllarda bo‘lishi mumkin."
#     },
#     {
#         "name": "Retinopatiya",
#         "description": "Ko‘z to‘r pardasi – retinalarning kasalliklari guruhi. Odatda diabet yoki qon bosimining oshishi bilan bog‘liq bo‘ladi."
#     },
#     {
#         "name": "Quruq ko‘z sindromi",
#         "description": "Ko‘z yoshlari yetarli darajada ajralmasligi yoki sifatining pastligi tufayli ko‘zning qurishi. Noqulaylik, achishish va ko‘rish muammolariga olib keladi."
#     },
#     {
#         "name": "Astigmatizm",
#         "description": "Ko‘zning korneasi yoki linzasidagi shakl o‘zgarishi tufayli yorug‘lik to‘g‘ri fokuslanmaydi. Noaniq ko‘rish bilan namoyon bo‘ladi."
#     },
#     {
#         "name": "Diabetik retinopatiya",
#         "description": "Diabetik bemorlarda uchraydigan retina kasalligi. Retinada qon tomirlarining zararlanishi tufayli yuzaga keladi."
#     },
#     {
#         "name": "Ko‘z yallig‘lanishi",
#         "description": "Ko‘zning har xil qismlarida yallig‘lanish jarayonlari bo‘lishi mumkin, masalan, uveit yoki keratit."
#     },
#     {
#         "name": "Makula degeneratsiyasi",
#         "description": "Retinaning markaziy qismi – makulaning shikastlanishi. Yoshi katta odamlarda ko‘rishning sekin pasayishiga olib keladi."
#     },
#     {
#         "name": "Blefarit",
#         "description": "Ko‘z qopqog‘i chetining yallig‘lanishi. Ko‘pincha yog‘ bezlarining nosoz ishlashi bilan bog‘liq bo‘ladi."
#     },
#     {
#         "name": "Uveit",
#         "description": "Ko‘zning o‘rta qavati – uveal to‘qimalarining yallig‘lanishi. Og‘riq, yorug‘likdan qo‘rqish va ko‘rish buzilishi bilan kechadi."
#     },
#     {
#         "name": "Keratit",
#         "description": "Ko‘zning old qavati – korneaning yallig‘lanishi. Bakterial, virusli yoki qo‘ziqorinli sabablari bo‘lishi mumkin."
#     },
#     {
#         "name": "Sklerit",
#         "description": "Ko‘zning oq qismi – skleraning yallig‘lanishi. Kuchli og‘riq va ko‘rishning yomonlashuvi bilan namoyon bo‘ladi."
#     },
#     {
#         "name": "Ko‘z ichi bosimi",
#         "description": "Ko‘z ichidagi suyuqlik bosimining normadan ortishi. Glaukomaning asosiy belgilaridan biri hisoblanadi."
#     },
#     {
#         "name": "Ko‘z to‘r pardasi ajralishi",
#         "description": "Retinaning ostidan ajralishi. Tezda jarrohlik aralashuvi talab qilinadi, aks holda ko‘rlikka olib keladi."
#     },
#     {
#         "name": "Ko‘rish nervi atrofiyasi",
#         "description": "Ko‘rish nervining nobud bo‘lishi. Ko‘rish qobiliyatining sekin yo‘qolishiga olib keladi."
#     },
#     {
#         "name": "Ko‘rish zaifligi",
#         "description": "Ko‘rishning tug‘ma yoki orttirilgan pastligi. Turli sabablarga ko‘ra yuzaga keladi, koreksiya yoki davolash talab etiladi."
#     },
#     {
#         "name": "Albinizm",
#         "description": "Melanin pigmentining yetishmasligi tufayli ko‘zlar nozik bo‘ladi va yorug‘likka juda sezuvchan bo‘ladi."
#     },
#     {
#         "name": "Ko‘z to‘r pardasi yirtilishi",
#         "description": "Retinada yoriq hosil bo‘lishi. Ko‘zda chaqnash, qora nuqtalar paydo bo‘lishi mumkin."
#     },
#     {
#         "name": "Ko‘z shikastlanishi",
#         "description": "Jismoniy ta’sir yoki jarohat natijasida ko‘zning mexanik shikastlanishi. Tez tibbiy yordam zarur."
#     },
#     {
#         "name": "Ko‘z qizarishi",
#         "description": "Ko‘pincha yallig‘lanish yoki allergiya belgisi sifatida paydo bo‘ladi. Ko‘z tomirlari kengayadi."
#     },
#     {
#         "name": "Fotofobiya",
#         "description": "Yorug‘likka ortiqcha sezuvchanlik. Ko‘pincha ko‘zdagi yallig‘lanishlar yoki asab kasalliklarida kuzatiladi."
#     },
#     {
#         "name": "Strabizm",
#         "description": "Ko‘zlarning bir tomonga qaray olmasligi. Bitta ob’ektga qaraganda ikki tasvir hosil bo‘ladi."
#     },
#     {
#         "name": "Amblyopiya",
#         "description": "Ko‘zning “dangasa” bo‘lishi. Bolalarda ko‘p uchraydi, erta aniqlansa davolanishi mumkin."
#     },
#     {
#         "name": "Dakriosistit",
#         "description": "Ko‘z yosh yo‘llarining yallig‘lanishi. Ko‘zdan doimiy yosh oqishi bilan kechadi."
#     },
#     {
#         "name": "Chalazion",
#         "description": "Ko‘z qopqog‘idagi yog‘ bezining tiqilib qolishi natijasida hosil bo‘lgan shish."
#     },
#     {
#         "name": "Hordeolum (arpa)",
#         "description": "Ko‘z qopqog‘ining chetidagi yallig‘langan bez. Og‘riqli va yallig‘langan bo‘lib, ichida yiring bo‘ladi."
#     },
 
#     {
#         "name": "Optik nevrit",
#         "description": "Ko‘rish nervining yallig‘lanishi. Ko‘rishning to‘satdan yomonlashuvi va ko‘z og‘rig‘i bilan kechadi."
#     },
#     {
#         "name": "Skleromalasiya",
#         "description": "Skleraning noziklashuvi yoki yumshash kasalligi. Odatda surunkali kasalliklar fonida rivojlanadi."
#     },
#     # {
#     #     "name": "Retinal vaskulit",
#     #     "description": "Retinadagi qon tomirlarning yallig‘lanishi. Autoimmun kasalliklar bilan bog‘liq bo‘lishi mumkin."
#     # },
#     # {
#     #     "name": "Ko‘zdagi kistalar",
#     #     "description": "Ko‘zning turli qismlarida hosil bo‘ladigan suyuqlik bilan to‘la bo‘shliqlar. Ko‘pincha benign bo‘ladi."
#     # },
#     {
#         "name": "Korneaning eroziyasi",
#         "description": "Korneaning sirt qatlamining shikastlanishi. Kuchli og‘riq va yorug‘lik sezuvchanligi bilan kechadi."
#     },
#     {
#         "name": "Korneaning chandiqlanishi",
#         "description": "Korneada avvalgi jarohat yoki infeksiyadan so‘ng hosil bo‘lgan chandiq. Ko‘rishni yomonlashtiradi."
#     },
#     # {
#     #     "name": "Ko‘z qorachig‘i kasalliklari",
#     #     "description": "Ko‘z qorachig‘ining kengayishi yoki torayishi bilan bog‘liq turli holatlar. Ko‘rishga ta’sir qiladi."
#     # },
#     # {
#     #     "name": "Ko‘zda allergiya",
#     #     "description": "Gulchang, chang yoki boshqa allergenlarga sezuvchanlik natijasida ko‘zning qichishishi, qizarishi va yoshlanishi."
#     # },
#     {
#         "name": "Irit",
#         "description": "Ko‘zning iris qismining yallig‘lanishi. Og‘riq, yorug‘likdan qo‘rqish va ko‘rishning pasayishi kuzatiladi."
#     },
#     {
#         "name": "Midriaziya",
#         "description": "Ko‘z qorachig‘ining normadan ortiq kengayishi. Neyrologik yoki dori ta’sirida yuzaga keladi."
#     },
#     # {
#     #     "name": "Mioziya",
#     #     "description": "Ko‘z qorachig‘ining haddan tashqari torayishi. Dorilar yoki asab tizimining shikastlanishi sababli bo‘lishi mumkin."
#     # },
#     # {
#     #     "name": "Vitreoretinopatiya",
#     #     "description": "Ko‘zning ichki suyuqligi va retina bilan bog‘liq kasalliklar. Odatda tug‘ma yoki genetik bo‘ladi."
#     # },
#     # {
#     #     "name": "Makulyar teshik",
#     #     "description": "Retinaning markaziy qismida teshik hosil bo‘lishi. Ko‘rishning pasayishiga olib keladi."
#     # },
#     # {
#     #     "name": "Ko‘zning mexanik shikastlanishi",
#     #     "description": "Jismoniy jarohatlar natijasida ko‘z to‘qimalarining shikastlanishi. Tezkor davolash talab etadi."
#     # },
#     # {
#     #     "name": "Epiphora",
#     #     "description": "Ko‘z yoshlarining ko‘p ajralishi. Yosh yo‘llarining tiqilishi yoki allergiya bilan bog‘liq bo‘ladi."
#     # },
#     # {
#     #     "name": "Ko‘zning ichki bosimining ko‘tarilishi",
#     #     "description": "Ko‘z ichi bosimi ortib boradi, glaukoma rivojlanish xavfi oshadi."
#     # },
#     # {
#     #     "name": "Ko‘zdagi og‘riq sindromi",
#     #     "description": "Ko‘zning ichki yoki tashqi qismlarida og‘riq hissi. Ko‘plab kasalliklarda uchraydi."
#     # },
#     # {
#     #     "name": "Korneaning transplantatsiyasi",
#     #     "description": "Korneaning shikastlangan qismini donor korneasi bilan almashtirish jarrohligi."
#     # },
#     # {
#     #     "name": "Retina degeneratsiyasi",
#     #     "description": "Retina hujayralarining asta-sekin nobud bo‘lishi. Ko‘rish yomonlashadi."
#     # }
# ]



# diseases_dict = {
#     "Katarakta": "Katarakta odatda jarrohlik yo‘li bilan davolanadi. Shox parda almashtirilib, sun’iy linza qo‘yiladi.",
#     "Glaukoma": "Glaukoma bosqichiga qarab dori vositalari (ko‘z tomchilari), lazerli yoki jarrohlik davolash usullari qo‘llaniladi.",
#     "Kon'yunktivit": "Bakterial kon'yunktivit uchun antibiotikli tomchilar, virusli holatlarda antiviral dorilar tavsiya etiladi.",
#     "Retinopatiya": "Diabetik retinopatiya uchun qon shakarini nazorat qilish, lazerli fotokoagulyatsiya yoki jarrohlik amaliyotlar qo‘llaniladi.",
#     "Quruq ko‘z sindromi": "Sun’iy ko‘z yoshlari, yog‘li ko‘z tomchilari va ba’zida yallig‘lanishga qarshi dorilar ishlatiladi.",
#     "Astigmatizm": "Ko‘zoynaklar, kontakt linzalar yoki refraktiv jarrohlik (LASIK) orqali tuzatiladi.",
#     "Diabetik retinopatiya": "Qandli diabetni nazorat qilish, retina uchun lazer terapiya, ko‘z ichi inyektsiyalari va vitrektomiya.",
#     "Ko‘z yallig‘lanishi": "Yallig‘lanishga qarshi tomchilar (kortikosteroidlar), antibiotiklar va dori terapiyasi.",
#     "Makula degeneratsiyasi": "Anti-VEGF inyektsiyalari, lazer terapiya va maxsus ko‘zoynaklar yordamida ko‘rishni qo‘llab-quvvatlash.",
#     "Blefarit": "Qovoqlarni iliq suv bilan tozalash, antibiotikli malhamlar yoki tomchilar.",
#     "Uveit": "Yallig‘lanishga qarshi dorilar, immunosupressiv terapiya yoki kortikosteroidlar bilan davolanadi.",
#     "Keratit": "Antibiotiklar, antifungal yoki antiviral tomchilar qo‘llaniladi.",
#     "Sklerit": "Yallig‘lanishga qarshi steroidlar va og‘riq qoldiruvchi dorilar bilan davolash.",
#     "Ko‘z ichi bosimi": "Bosimni kamaytiruvchi tomchilar, lazer yoki jarrohlik amaliyotlar kerak bo‘lishi mumkin.",
#     "Ko‘z to‘r pardasi ajralishi": "Zudlik bilan jarrohlik (pnevmatik retinopeksiya, skleral buckling yoki vitrektomiya) kerak.",
#     "Ko‘rish nervi atrofiyasi": "Asosiy sababni aniqlash va uni davolash; ko‘rishni tiklash qiyin.",
#     "Ko‘rish zaifligi": "Ko‘zoynaklar, linzalar yoki ko‘rishni qo‘llab-quvvatlovchi texnologiyalar bilan yordam beriladi.",
#     "Albinizm": "Maxsus ko‘zoynaklar, quyoshdan himoyalovchi vositalar tavsiya etiladi.",
#     "Ko‘z to‘r pardasi yirtilishi": "Lazerli yoki muzlatish (krioterapiya) orqali tuzatish.",
#     "Ko‘z shikastlanishi": "Zudlik bilan ko‘z shifokoriga murojaat qilish, kerakli davo turi aniqlanadi.",
#     "Ko‘z qizarishi": "Antihistamin tomchilar, sun’iy yoshlar yoki infektsiyaga qarshi vositalar.",
#     "Fotofobiya": "Asosiy sababni davolash, quyoshdan saqlovchi ko‘zoynaklar.",
#     "Ko‘zda og‘riq": "Og‘riqning sababiga qarab davo: yallig‘lanishga qarshi, antibakterial yoki jarrohlik.",
#     "Ko‘zda xiralik": "Shifokor tomonidan aniqlangan sababga qarab davolash: katarakta, yallig‘lanish yoki boshqa omillar.",
#     "Ko‘z g‘ilayligi": "Ko‘z mashqlari, prizmali ko‘zoynaklar yoki jarrohlik amaliyotlar.",
#     "Strabizm": "Ko‘z mushaklarini jarrohlik bilan tuzatish yoki terapevtik mashqlar.",
#     "Amblyopiya": "Ko‘rish mashqlari, bir ko‘zni yopish (occlusion therapy) yoki dori vositalari.",
#     "Ko‘z ichi yallig‘lanishi": "Kortikosteroidlar va immunosupressiv dorilar.",
#     "Skleromalasiya": "Kortikosteroidlar va asosiy sababga qarab dori terapiyasi.",
#     "Irit": "Nevrologik muolajalar, ko‘zoynaklar yoki jarrohlik.",
#     "Midriaziya": "Yallig‘lanishga qarshi va antibakterial davo.",
#     "Skleral ektaziya": "Kontakt linzalar, jarrohlik yoki maxsus protezlar.",
#     "Korneaning eroziyasi": "Antibiotik tomchilar, sun’iy yosh va himoya linzalari.",
#     "Korneaning degeneratsiyasi": "Sun’iy ko‘z yoshlar, jarrohlik yoki kornea transplantatsiyasi.",
#     "Chalazion": "Iliq kompresslar, ba’zida jarrohlik olib tashlash.",
#     "Dakriosistit": "Antibiotiklar va ba’zida yirtilish yo‘lini ochish uchun jarrohlik.",
#     "Ko‘zning qurib qolishi": "Sun’iy yoshlar, ko‘z tomchilari va ba’zan dori terapiyasi.",
#     "Ko‘zdagi allergiya": "Antihistamin tomchilar, steroid tomchilar va allergendan saqlanish.",
#     "Fotokeratit": "Ko‘z dami, sun’iy yoshlar, antibiotik tomchilar.",
#     "Hordeolum (arpa)": "Iliq kompresslar, antibiotikli malhamlar.",
#     "Korneaning chandiqlanishi": "Kornea transplantatsiyasi yoki shox parda tozalash amaliyoti.",
#     "Optik nevrit": "Steroid inyektsiyalari va asosiy sababni davolash."
# }


# # Generate fixture format
# fixture = []
# for i, disease in enumerate(diseases_with_info, 1):
#     fixture.append({
#         "model": "app.Disease",
#         "pk": i,
#         "fields": {
#             "name": disease["name"],
#             "description": disease["description"],
#             'treatment_method': diseases_dict[disease["name"]],
#         }
#     })



# # Save to JSON file
# file_path = "manage_data/data/disease_info_fixture.json"
# with open(file_path, "w", encoding="utf-8") as f:
#     json.dump(fixture, f, ensure_ascii=False, indent=2)

# file_path
