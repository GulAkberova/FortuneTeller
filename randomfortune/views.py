from django.shortcuts import render
import random

fortunelist = [
"Bugun super olacag!Inan ve tutdugun yoldan el cekme!",
"Ola biler yorulmusan.Ancag dayanma.Ancag ireli",
"Sen cox mesgulsan,ancag sen cox xowbextsen!",
"Fikirlewme.Hereket et!",
"Ola biler gunun pis kecir.Ancag bu pis heyatin var demek deyil!",
"Her wey gozlediyinnen dahada yaxsi olacag!",
"inan ve davam et",
"Her wey yaxwi olacag!",
"Her wey alt ust olacag!",
"Allah belavi verecey.Gunah isleme!",
'bol pul'
]



def fortune(request):
    fortune=random.choice(fortunelist)
    context={
        "fortune":fortune
    }
    return render(request,"/templates/randomfortune/fortune.html",context)


