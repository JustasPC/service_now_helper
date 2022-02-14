from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
import time
import pyperclip as pc


#Narsykles
browser3 = webdriver.Chrome()
browser2 = webdriver.Chrome()
browser2.get('')
browser3.get(')
option = input('Prisijunkite...')
browser2.get('')

#main  menu
def fun_main():
    condition = True
    while condition:
        print('************MAIN MENU**********')
        print('#1 Kurti Service now ')
        print('#2 Dabartinio laiko stampas')
        print('#3 Sustabdymo laikų info')
        print('#4 Suvaldymo laikų info')
        print('#5 Paž. pašalinimo laikų info')
        option = input('Pasirinkta:')
        condition = fun_job(option)
    
def fun_job(option):
    if option == '1':
        fun_register()
    if option == '2':
        print('##########')
        print(fun_laikas())
        print('#********#')
    if option == "3":
        fun_incident_times(3)
    if option == "4":
        fun_incident_times(4)
    if option == "5":
        fun_incident_times(5)
    if option == "":
        return False
    return True


def fun_incident_times(x):
    if x == 3:
        print('########################################################################')
        print('Incidentas laikomas sustabdytu kuomet jo būsena iš aktyvios tampa pasyvia')
        print('(t.y. Incidento veikimas sustabdomas, pvz.kenkėjiška')
        print('programinė įranga yra izoliuota ir nebekelia grėsmės).')
        print("Sustabdymo laikai:")
        print("Per 4 val. nuo Incidento identifikavimo D arba P3")
        print("Per 8 val. nuo Incidento identifikavimo V arba P2")
        print("Per 12 val. nuo Incidento identifikavimo N arba P1")
        print('########################################################################')
    if x == 4:
        print('########################################################################')
        print('Incidentas laikomas suvaldytu kuomet pašalinta grėsmė ir incidento priežastys')
        print('IT/IS toliau funkcionuoja įprasta tvarka.')
        print("Suvaldymo laikai:")
        print("Per 24 val. nuo Incidento sustabdymo D arba P3")
        print("Per 48 val. nuo Incidento sustabdymo V arba P2")
        print("Per 96 val. nuo Incidento sustabdymo N arba P1")
        print('########################################################################')
    if x == 5:
        print('########################################################################')
        print('Pažeidžiamumas laikomas pašalintu kuomet jį sukėlusios priežastys yra pašalintos')
        print('ir Pažeidžiamumas arba programinė įranga nebeegzistuoja;')
        print("Pašalinimo terminas:")
        print("Per 24 val. (1 para) nuo Pažeidžiamumo užregistravimo D arba P3")
        print("Per 120 val. (1 sav.) nuo Pažeidžiamumo užregistravimo V arba P2")
        print("Per 240 val. (2 sav.) nuo Pažeidžiamumo užregistravimo N arba P1")
        print('########################################################################')
        

def fun_type_cat(x):
    inc_listas = [{"name":'[KP]',
                   "head":'Kenkimo programinė įranga',
                   "N":"P3 pav. darb. 10 ir (ar) IT/IS komponentas sutrinka, IT/IS veikia įprast. būdu",
                   "V":"P2 pav. darb. skaičius 11..49 ir/ar IT/IS komponentas sutrinka, IT/IS veikia įprast. arba altern. būdu, 1 PC botnete",
                   "D":"P1 pav. darb. skaičius50+ ir/ar IT/IS veikimas visiškai sutrinka, sustoja, pc su ransomware, ATP ar C&C",
               'descr':'Virusai, ransomware, APT, botnetas',
               "Kat":"--"},
              {"name":'[NL]',
               "head":'Nepageidaujamų laiškų, klaidinančios ar žeidžiančios informacijos platinimas',
               'descr':'Klaidinančios, žeidžiančios informacijos platinimas',
                   "N":"P3 paveiktų darb. <=49 ir (ar) IT/IS komponentas sutrinka, IT/IS veikia įprast. būdu",
                   "V":"P2 paveiktų darb. skaičius 50..99 ir (ar) IT/IS komponentas sutrinka, IT/IS veikia įprast. arba altern.  būdu",
                   "D":"P1 paveiktų darb. skaičius 100+ ir (ar) IT/IS veikimas visiškai sutrinka, sustoja",
               "Kat":"--"},
              {"name":'[Į]',
               "head":'Įsilaužimas',
               'descr':'Sėkmingas įsilaužimas ir/ar neteisėtas IT/IS, taikomosios programinės įrangos ar paslaugos naudojimas',
              "N":"-----------",
               "V":"P2 pav. darb. skaičius 1..19 ir/ar bent 1 IT/IS veikimas sutrinka arba veik. alt. būdu, neautorizuotas prisijungimas",
               "D":"P1 paveiktų darb. skaičius 20+ ir/ar IT/IS veikimas visiškai sustoja, neautorizuotas prisijungimas",
               "Kat":"--"},
              {"name":'[MĮ]',
               "head":'Mėginimas įsilaužti',
               'descr':'Mėginimas įsilaužti, sutrikdyti IT/IS veikimą, prievadų skenavimas, slaptažodžių parinkimas, kenkimo programinės įrangos platinimas',
               "N":"P3 pav. darb. 10 ir (ar) IT/IS komponentas sutrinka, IT/IS veikia įprast. būdu",
               "V":"P2 pav. darb. skaičius 11..19 ir/ar bent 1 IT/IS veikimas iš dalies sutrinka/vyksta alt. būdu, bandoma išnaudoti žinomus exploit, bruteforcinami slaptažodžiai",
               "D":"P1 pav. darb. skaičius 20+ ir (ar) IT/IS veikimas visiškai sutrinka/sustoja, bandoma išnaudoti 0-day exploit",
               "Kat":"--"},
              {"name":'[IG]',
               "head":'Informacijos rinkimas',
              'descr':'Skenavimai, informacijos perėmimas, manipuliavimas naudotojų emocijomis, psichologija, pastabumo stoka, SE',
               "N":"P3 pav. darb. ir/ar IT/IS <= 10",
               "V":"P2 pav. darb. skaičius 11..49 ir/ar 1..4 IT/IS vyksta aktyvus info perėmimas",
               "D":"P1 pav. darb. skaičius 50+ ir/ar 5+ IT/IS vyksta aktyvus info perėmimas",
               "Kat":"--"},
              {"name":'[VULN]',
               "head":'Pažeidžiamumas',
               'descr':'IT/IS ar jos dalies programinė arba konfigūracijos spraga',
              "N":"P3 Pažeidžiamumo kritiškumas CVSS skalėje vertinamas iki 4.9",
               "V":"P2 Pažeidžiamumo kritiškumas CVSS skalėje vertinamas 5.0 – 6.9",
               "D":"P1 Pažeidžiamumo kritiškumas CVSS skalėje vertinamas 7.0 ir daugiau",
               "Kat":"--"},
              {"name":'[PT]',
               "head":'Paslaugų trikdymas, prieinamumo pažeidimai ',
               'descr':'DDoS, DDoS, aptinkamas paslaugos trikdymas',
              "N":"P3 paveiktų darb. <=10 ir (ar) IT/IS komponentas sutrinka, IT/IS veikia įprast. būdu",
               "V":"P2 pav. darb. skaičius 50..99 ir/ar bent 1 IT/IS veikimas iš dalies sutrinka/vyksta alt. būdu",
               "D":"P1 pav. darb. skaičius 100+ ir (ar) IT/IS veikimas visiškai sutrinka/sustoja",
               "Kat":"--"},
              {"name":'[DLP]',
               "head":'Informacijos turinio saugumo pažeidimai',
               'descr':'Neteisėta prieiga prie vidinės informacijos, neteisėtas tokios informacijos tvarkymas',
               "N":"P3 pav. darb. ir (ar) Dokumentų skaičius <=10",
               "V":"P2 pav. darb. ir (ar) Dokumentų skaičius 11..49 arba 1..9 neteisėtų prieigų prie info įtakojančios IT/IS veiklą/paslaugas",
               "D":"P1 pav. darb. ir (ar) Dokumentų skaičius 50+ arba 10+ neteisėtų prieigų prie info įtakojančios IT/IS veiklą/paslaugas",
               "Kat":"--"},
              {"name":'[KONF]',
               "head":'Konfidencialios ir Komercinės (gamybinės) Informacijos turinio saugumo pažeidimas',
               'descr':'Neteisėta prieiga prie konfidencialios ar komercinės (gamybinės) kategorijos informacijos, neteisėtas tokios informacijos tvarkymas ',
               "N":"--------",
               "V":"--------",
               "D":"P1 Neautorizuoto personalo prieiga prie Konfidencialios ir (ar) Komercinės (gamybinės) informacijos ",
               "Kat":"--"},
              {"name":'[NV]',
               "head":'Neteisėta veikla, sukčiavimas',
               'descr':'Neteisėta įtaka IT/IS veiklai, sukčiavimas, vagystė, nelegalios progr. įrangos ar leidinių naudojimas, tapatybės klastojimo',
               "N":"P3 pav. darb. ir (ar) IT/IS skaičius <=10",
               "V":"P2 pav. darb. ir (ar) IT/IS skaičius 11..19",
               "D":"P1 pav. darb. ir (ar) IT/IS skaičius 20+",
               "Kat":"--"},
              {"name":'[TP]',
               "head":'Kita',
               'descr':'Teisės aktų nuostatų pažeidimai ir kiti Incidentai, kurie neatitinka nė vienos iš nurodytų grėsmių',
               "N":"P3 Pažeistos 1 teisės akto nuostatos arba kat. nustato Saugumo ekspertas pasitaręs su ISĮ",
               "V":"P2 Pažeistos 2 teisės aktų nuostatos arba kat. nustato Saugumo ekspertas pasitaręs su ISĮ",
               "D":"P1 Pažeistos 3+ teisės aktų nuostatos arba kat. nustato Saugumo ekspertas pasitaręs su ISĮ",
               "Kat":"--"}]

#Renkames headeri (tipa)
    if x == 'type':
        print('************Pasirinkite kategorija:')
        for index in range(len(inc_listas)):
            print('### ',index+1,' ',inc_listas[index]['name'],' ',inc_listas[index]["head"])
            print(inc_listas[index]['descr'])
        tikrinimas = True
        while tikrinimas:
            option = input('Pasirink tipo nr.:')
            try:
                tmp = int(option)
                if tmp >= 1 and tmp <=11:
                    tmp = int(option)-1
                    tikrinimas = False
                else:
                    print('Pasirinktas neegzistuojantis kategorijos nr. Kartojama')
            except:
                print('Opcija neatpazinta')
        print('##############################')
        tikrinimas = True
        while tikrinimas:
            print('Galimos kategorijos pagal tipa:')
            print('###D: ',inc_listas[tmp]['D'])
            print('###V: ',inc_listas[tmp]['V'])
            print('###N: ',inc_listas[tmp]['N'])
            option = input('Pasirink kategorijos dydį D/V/N/P1/P2/P3:')
            try:
                if 'n' in option or "N" or "3" in option:
                    inc_listas[tmp]['Kat']='P3'
                    tikrinimas = False
                elif 'v' in option or "V" or "2" in option:
                    inc_listas[tmp]['Kat']='P2'
                    tikrinimas = False
                elif 'd' in option or "D" or "1" in option:
                    inc_listas[tmp]['Kat']='P1'
                    tikrinimas = False
                else:
                    print("Opcija neatpazinta")
            except:
                print("Kartoti...")
        return inc_listas[tmp]

               
def fun_description():
    pazeidimas={'Tipas':'-',
                'Kategorija':'-',
                'head':'-',
                'Hostname':'-',
                'Skaicius':'-',
                'Darbuotojas':'-',
                'Pozymiai':'-',
                'Busena':'-',
                'VV':'-',
                'Trukme':'-',
                'Saltinis':'-',
                'Metodas':'-',
                'Pasekmes':'-',
                'Mastas':'-',
                'NusPriemones':'-',
                'Valdpriem':'-',
                'Pazeidziamumas':'-',
                'VulnTipas':'-',
                'VulnKat':'-',
                'CVSS':'-',
                'Vulnhostname':'-',
                'VulnVV':'-',
                'VulnPaveik':'-',
                'VulnDescr':'-',
                'VulnPasekmes':'-',
                'VulnMitigation':'-'
                }
    incendentas=fun_type_cat('type')
    pazeidimas['Tipas']=incendentas['name']
    pazeidimas['head']=incendentas['head']
    pazeidimas['Kategorija']=incendentas['Kat']
    if incendentas['name']!='[VULN]':
        option = input('IT/IS ar Kompiuterinė įranga, kurioje nustatytas Incidentas:')
        pazeidimas['Hostname']=fun_op_checkas(option)
        option = input('Incidento paveiktų vartotojų, IT/IS ar Kompiuterinės įrangos skaičius:')
        pazeidimas['Skaicius']=fun_op_checkas(option)
        option = input('Paveiktas naudotojas arba N/A jei ju daug:')
        pazeidimas['Darbuotojas']=fun_op_checkas(option)
        print('Sufleris VV:[LTG] [CRG] [LNK] [TVPC] [VLRD] [INF] [GTC]')
        fun_check(pazeidimas['Darbuotojas'])
        option = input('Incidento požymiai:')
        pazeidimas['Pozymiai']=fun_op_checkas(option)
        option = input('Incidento būsena (aktyvus – šiuo metu vyksta, pasyvus – šiuo metu nevyksta):')
        pazeidimas['Busena']=fun_op_checkas(option)
        option = input('VV, kurio IT/IS ar Komp. įrangoje nustatytas Incidentas:')
        pazeidimas['VV']=fun_op_checkas(option)
        option = input('Incidento veikimo trukmė (Incidento pradžia ir pabaiga:')
        pazeidimas['Trukme']=fun_op_checkas(option)
        option = input('Incidento šaltinis:')
        pazeidimas['Saltinis']=fun_op_checkas(option)
        option = input('Incidento veikimo metodas:')
        pazeidimas['Metodas']=fun_op_checkas(option)
        option = input('Galimos ir esamos Incidento pasekmės:')
        pazeidimas['Pasekmes']=fun_op_checkas(option)
        option = input('Incidento poveikio pasireiškimo (galimo išplitimo) mastas:')
        pazeidimas['Mastas']=fun_op_checkas(option)
        option = input('Priemonės, kuriomis Incidentas nustatyta:')
        pazeidimas['NusPriemones']=fun_op_checkas(option)
        option = input('Galimos Incidento valdymo priemonės:')
        pazeidimas['Valdpriem']=fun_op_checkas(option)
    if incendentas['name']=='[VULN]':
        option = input('Pažeidžiamumo tipas:')
        pazeidimas['VulnTipas']=fun_op_checkas(option) 
        option = input('Pažeidžiamumo Kategorija:')
        pazeidimas['VulnKat']=fun_op_checkas(option)
        option = input('Pažeidžiamumo kritiškumas pagal CVSS skalę:')
        pazeidimas['CVSS']=fun_op_checkas(option)
        option = input('IT/IS ar Komp. įranga, kurioje nustatytas Pažeidžiamumas:')
        pazeidimas['Vulnhostname']=fun_op_checkas(option)
        option = input('VV, kurio IT/IS ar Komp. įrangoje nustatytas pažeidžiamumas:')
        pazeidimas['VulnVV']=fun_op_checkas(option)
        option = input('Pažeidžiamumo paveiktų vartotojų, IT/IS ar Kompiuterinės įrangos skaičius:')
        pazeidimas['VulnPaveik']=fun_op_checkas(option)
        option = input('Pažeidžiamumo trumpas paaiškinimas arba nuoroda į paaiškinimą:')
        pazeidimas['VulnDescr']=fun_op_checkas(option)
        option = input('Galimos Pažeidžiamumo pasekmės:')
        pazeidimas['VulnPasekmes']=fun_op_checkas(option)
        option = input('Rekomendacijos ir veiksmai reikalingi atlikti siekiant pašalinti Pažeidžiamumą:')
        pazeidimas['VulnMitigation']=fun_op_checkas(option)
    return pazeidimas

#Istraukia info apie darbuotoja is ManoLitrail kontaktu
def fun_check(vartotojas):
    info = vartotojas.split()
    if len(info)<=4:
        try:
            browser2.get('https://mano.litrail.lt/contacts/detailed')
            time.sleep(1)
            el = browser2.find_element_by_id('contactssearch-vardas')
            el.click()
            el.send_keys(info[0])
            el.send_keys(Keys.ENTER)
            time.sleep(1)
            el = browser2.find_element_by_id('contactssearch-pavarde')
            el.click()
            el.send_keys(info[1])
            el.send_keys(Keys.ENTER)
            time.sleep(1)
            el = browser2.find_elements_by_class_name('w2')
            asmuo =[]
            for i in el:
                if i.get_attribute('data-col-seq')=='0':
                    asmuo.append(i.text)
                if i.get_attribute('data-col-seq')=='1':
                    asmuo.append(i.text)
                if i.get_attribute('data-col-seq')=='2':
                    asmuo.append(i.text)
                if i.get_attribute('data-col-seq')=='3':
                    asmuo.append(i.text)
                if i.get_attribute('data-col-seq')=='5':
                    asmuo.append(i.text)
                if i.get_attribute('data-col-seq')=='6':
                    asmuo.append(i.text)
                    print(asmuo)
        except:
            print('Nepavyko rasti kontakto')
            print('N/A')
        
def fun_op_checkas(option):
    if option=="":
        return pc.paste()
    else:
        return option


def fun_orderis(pazeidimas):
    informacija={'Tipas':'Tipas:',
                'Kategorija':'Kategorija:',
                'head':'Aprašymas:',
                'Hostname':'IT/IS ar Kompiuterinė įranga, kurioje nustatytas Incidentas:',
                'Skaicius':'Incidento paveiktų vartotojų, IT/IS ar Kompiuterinės įrangos skaičius:',
                'Darbuotojas':'Paveiktas naudotojas arba N/A jei ju daug:',
                'Pozymiai':'Incidento požymiai:',
                'Busena':'Incidento būsena:',
                'VV':'VV, kurio IT/IS ar Komp. įrangoje nustatytas Incidentas:',
                'Trukme':'Incidento veikimo trukmė (Incidento pradžia ir pabaiga:',
                'Saltinis':'Incidento šaltinis:',
                'Metodas':'Incidento veikimo metodas:',
                'Pasekmes':'Galimos ir esamos Incidento pasekmės:',
                'Mastas':'Incidento poveikio pasireiškimo (galimo išplitimo) mastas:',
                'NusPriemones':'Priemonės, kuriomis Incidentas nustatyta:',
                'Valdpriem':'Galimos Incidento valdymo priemonės:',
                'Pazeidziamumas':'-',
                'VulnTipas':'Pažeidžiamumo tipas:',
                'VulnKat':'Pažeidžiamumo Kategorija:',
                'CVSS':'Pažeidžiamumo kritiškumas pagal CVSS skalę:',
                'Vulnhostname':'IT/IS ar Komp. įranga, kurioje nustatytas Pažeidžiamumas:',
                'VulnVV':'VV, kurio IT/IS ar Komp. įrangoje nustatytas pažeidžiamumas:',
                'VulnPaveik':'Pažeidžiamumo paveiktų vartotojų, IT/IS ar Kompiuterinės įrangos skaičius:',
                'VulnDescr':'Pažeidžiamumo trumpas paaiškinimas arba nuoroda į paaiškinimą:',
                'VulnPasekmes':'Galimos Pažeidžiamumo pasekmės:',
                'VulnMitigation':'Rekomendacijos ir veiksmai reikalingi atlikti siekiant pašalinti Pažeidžiamumą:'
                }
    try:
        info = pazeidimas['Darbuotojas'].split()
        if len(info)>=2:
            inicialai=info[0][0]+info[1][0]
        else:
            inicialai="N/A"
            info = "N/A"
    except:
        inicialai="N/A"
        reporter="N/A"
    textas=''
    headline = str(pazeidimas['Tipas'])+' '+str(pazeidimas['head'])+' ('+inicialai+') ['+str(pazeidimas['VV'])+'] ('+str(pazeidimas['Kategorija'])+')'
    for key in pazeidimas.keys():
        if pazeidimas[key]!='-':
            textas=textas+str(informacija[key])+' '+str(pazeidimas[key])+'\r\n'
    print(headline)
    print(textas)
    print('Tyrimas:', fun_laikas())
    print('Sustabdymas:', fun_laikas())
    print('Suvaldymas:', fun_laikas())
    con = True
    while con:
        option = input('Ar norite registruoti sia informacija Service now? y/n:')
        if 'y' in option or 'Y' in option:
            fun_ser_reg(headline,textas,info)
        else:
            con = False

            
def fun_register():
    pazeidimas = fun_description()
    fun_orderis(pazeidimas)  

#Service now registravimas
def fun_ser_reg(headline,textas, reporter):
    print('Team:')
    print('1. ITC-OPS-OG-IT SOC')
    print('2. SRVD-Business security-Cybersecurity')
    option = input('Pasirinkite team Nr.:')
    if option=='1' or option=='2':
        if option=='1':
            teamas = 'ITC-OPS-OG-IT SOC'
        if option=='2':
            teamas = 'SRVD-Business security-Cybersecurity'
    else:
        teamas = 'SRVD-Business security-Cybersecurity'
    salyga = True
    while salyga:
        if 'Create' in browser3.title:
            print('Service now puslapis registravimui atidarytas...')
            salyga=False
        else:
            option = input('Atidarykit service now registracijos langa...')
    try:
        browser3.switch_to.frame('gsft_main')
    except:
        print('Nerastas freimas...')
    try:
        el = browser3.find_element_by_id('sys_readonly.incident.number')
        print('Registruojamas ID: ',el.get_attribute('value'))
        el = browser3.find_element_by_id('sys_display.incident.u_reported_by')
        registror=el.get_attribute('value')
        if reporter!="N/A":
            el.clear()
            el.send_keys(reporter[0]+' '+reporter[1])
            el.send_keys(Keys.ENTER)
            print('Pranesejas: ',el.get_attribute('value'))
        el = browser3.find_element_by_id('incident.category')
        el.send_keys('CyberSecurity')
        time.sleep(1)
        #el = browser3.find_element_by_id('incident.subcategory')
        #el.send_keys(kategorija)
        el = browser3.find_element_by_id('incident.short_description')
        el.send_keys(headline)
        el = browser3.find_element_by_id('incident.description')
        el.send_keys(textas)
        el = browser3.find_element_by_id('sys_display.incident.assignment_group')
        el.clear()
        el.send_keys(teamas)
        el.send_keys(Keys.DOWN)
        el.send_keys(Keys.ENTER)
        time.sleep(1)
        el = browser3.find_element_by_id('sys_display.incident.assigned_to')
        el.send_keys(reportor)
        el.send_keys(Keys.ENTER)
    except:
        print('Nepavyko supildyti service now')
        
        
 
#Laikas LT formatu
def fun_laikas():
    laikas = time.localtime()
    metai=str(laikas.tm_year)
    if len(str(laikas.tm_mon))>1:
        menuo=str(laikas.tm_mon)
    else:
        menuo='0'+str(laikas.tm_mon)
    if len(str(laikas.tm_mday))>1:
        diena=str(laikas.tm_mday)
    else:
        diena='0'+str(laikas.tm_mday)
    if len(str(laikas.tm_hour))>1:
        valanda=str(laikas.tm_hour)
    else:
        valanda='0'+str(laikas.tm_hour)
    if len(str(laikas.tm_min))>1:
        minutes=str(laikas.tm_min)
    else:
        minutes='0'+str(laikas.tm_min)
    suvaldymas=metai+'-'+menuo+'-'+diena+' '+valanda+':'+minutes
    return suvaldymas




fun_main()
