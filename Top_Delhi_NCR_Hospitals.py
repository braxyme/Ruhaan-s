import streamlit as st
import pandas as pd
import webbrowser as wb

#error while deploying this site in streamlit
#how can we keep the theme of this site when deployed
#how to access online csv file with a deployed site

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://hubpublishing.co.uk/wp-content/uploads/2019/11/lighter-life.jpg");
             background-size: 1550px 800px;
             background-repeat: no-repeat;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

set_bg_hack_url()

st.title('Medical Tourism')
st.subheader('Top hospitals in Delhi NCR')

st.markdown('___')
st.write('')

im3,img2, img3, img232 = st.columns(4)


st.write('')
st.write('')
st.markdown('**NCR - The National Capital Region**')
st.write('')
st.markdown('''<html><p style="background-color:#94e5ff;">NCR is a region that is betting on the capital of Delhi and infrastructure that is being established by linking 
           it to the capital of Delhi. From Delhi to the betting states of Haryana and Uttar Pradesh in the NCR, The districts 
           of Rajasthan have been incorporated into the NCR area so that the Delhi government can have an equal impact on growth. 
           Ghaziabad, Gurugram, Faridabad, Noida and Muzaffarnagar are among the NCR’s major cities. The National Capital 
           Region includes these cities, as well as newly merged districts and Delhi (NCR). All its states and districts, 
           including NCR, produced $ 128.9 billion of GDP in 2011-12, a figure that was 7.5 per cent of India’s total GDP 
           this year.</p></html>''', unsafe_allow_html=True)
st.write('')
st.markdown('1. **Medanta** - The Medicity, Gurgaon')
st.write('')
st.write('')
ac,ar,at = st.columns(3)
with ar:
    st.image('https://th.bing.com/th/id/R.0e511ab5ae916bb7dbcc73109a6ef56c?rik=PBiSmHAUud9tVw&riu=http%3a%2f%2fstatic.dnaindia.com%2fsites%2fdefault%2ffiles%2f2017%2f12%2f24%2f635938-medanta.jpg&ehk=PsaVw8dDD7v7lr3UnWtkn07cpVQVnnHDnlVCLeeFKnk%3d&risl=&pid=ImgRaw&r=0', width=300)
st.write('')
st.write('')
meda = [
'1250 bedded hospital',
'350 bedded I.C.U. for management of critically ill patients',
'Availability of 3 Tesla MRI scan, gamma camera and other advanced facilities',
'37 well equipped operation theaters',
'Rehabilitation facilities like physical therapy, occupational therapy arranged for patients who have undergone orthopedic surgery',
'Facilities like travel arrangements, medical visa, health insurance arranged for patients visiting from abroad',
'State-of-art diagnostic centers and pathology labs equipped with modern machinery',
'Air ambulance services for emergency transport',
'Tele-medicine services for patients who cannot travel due to their health','','','','','','','','','',''
]

medb =['Ayurvedic Medicine','Bariatric Surgery','Cardiology and Cardiac Surgery','Diabetology','Endocrinology',
'Gynecology and Obstetrics','Hematology','Laparoscopic Surgery','Nephrology','Neurology and Neurosurgery','Ophthalmology',
'Orthopedics','Pediatrics and Pediatric Surgery','Physiotherapy','Respiratory Medicine','Rheumatology','Sleep Medicine','Vascular Surgery',
'Urology and Urosurgery']

medc = ['JCI accredited','NABH accredited','NABL accredited or blood bank and laboratory',
        'Best multi-specialty hospital award at MT India Healthcare Awards 2016','','','','','','','','','','','','','','','']

medantadict = {
    'Services and Facilities':meda,
    'Specialities':medb,
    'Awards and Recognitions':medc
}
medantadatfrm = pd.DataFrame(medantadict)
st.dataframe(medantadatfrm)
st.write('')
mednk = [!["Medanta's Site"]'https://www.medanta.org/']
st.markdown('**'+mednk+'**')
st.write('')
st.write('')
st.markdown('2. **Indraprashta Apollo Hospital**')
st.write('')
st.write('Indraprastha Apollo Hospital has become the favored destination of millions of patients spanning across different '
         'countries. Apollo Hospitals opened its doors in 1983 and ever since nurtured a goal which read as “Our mission is '
         'to bring healthcare of international standards within the reach of every individual.')
st.write('')
st.write('')
dd,dr,dk = st.columns(3)
with dr:
    st.image('https://th.bing.com/th/id/OIP.XKgICxrtMJX-l6wZuAV-mAHaFT?w=225&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7', width=300)
st.write('')
st.write('')

apollodict = {
    'Doctors':['Dr. Arun Prasad','Dr. Nidhi Goyal','Dr. Vishal Garg','Dr. Vibhu Bahl','Dr. Adosh Lall',
               'Dr. Nameet Jerath','Dr. Yash Gulati','Dr. C M Batra','Dr. Prof. Vipul Vijay','Dr. Saket Goel','Dr. Deepak Govil',
               'Dr. Vivek Gupta'],
    'Specalizations and Qualifications':['Specialization: Senior General, GI & Bariatric Surgeon Specializing in Laparoscopy, VATS Thoracoscopy, Endoscopic and Robotic Surgery',
                                         'Radiologist','MBBS, MD – Medicine, DM – Gastroenterology, 17 years experience, Gastroenterologist',
                                         'MS – Orthopaedics, MBBS, 20 years experience, Orthopedist',
                                         'MDS – Periodontology and Oral Implantology, BDS, 24 years experience, Dental Surgeon, Periodontist, Dentist',
                                         'MBBS, MD – Pediatrics, 21 years experience, Pediatrician',
                                         'MS – Orthopaedics, M.Ch – Orthopaedics, MBBS, Orthopedist, Joint Replacement Surgeon, Spine Surgeon',
                                         'MBBS, MD – General Medicine, DNB – Endocrinology, Diabetes, Metabolism, Diploma in Child Health (DCH) 33 years experience, Endocrinologist',
                                         'MBBS, MS – Orthopaedics, DNB – Orthopedics/Orthopedic Surgery, MNAMS – Orthopaedics, 14 years experience, Orthopedist, Joint Replacement Surgeon',
                                         'MBBS, MS – General Surgery, 26 years experience, General Surgeon, Laparoscopic Surgeon',
                                         'MBBS, MS – General Surgery, PhD – Gastrointestinal Surgery, 37 years experience, GastroIntestinal Surgeon, General Surgeon, Intestine Surgeon',
                                         'MBBS, MD – General Medicine, DM – Cardiology, FACC, 28 years experience, Cardiologist, Interventional Cardiologist'
                                         ]
}

apollodatafrm = pd.DataFrame(apollodict)
st.dataframe(apollodatafrm)
st.write('')
apllonk = 'https://delhi.apollohospitals.com/'
if st.button("Apollo's Official Site"):
    wb.open_new_tab(apllonk)
st.write('')
st.write('')
st.markdown('3. **Jaypee Hospital**')
st.write()

st.write('Jaypee Hospital at Noida is the flagship hospital of the Jaypee Group, which heralds the group’s noble intention '
         'to enter the healthcare space. This hospital has been planned and designed as a 1200 bedded tertiary care '
         'multi-specialty facility and has commissioned 525 beds in the first phase.')

st.write('')
st.markdown('**"" We aim to promote healthcare to the common masses, with the growing needs of society by providing quality and '
         'affordable healthcare with commitment. ""**')

st.write('')
st.write('')
hn,hk,hl = st.columns(3)
with hk:
    st.image('https://th.bing.com/th/id/OIP.lUSfG8yBxmOBH4NkgSCxBQHaEd?w=279&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7', width=300)
st.write('')
st.write('')
dr,dt,dn = st.columns(3)
with dt:
    st.markdown('**Highlights of the institute**')
st.markdown('**•** Experienced Team of Cardiologists, Cardiothoracic Surgeons, Cardiac Anaesthetists')
st.markdown('**•** Collective experience of over 90,000 cardiac surgeries')
st.markdown('**•** 4 Cath Labs')
st.markdown('**•** Region’s First Hybrid OT with Biplane Cath Lab')
st.markdown('**•** Delhi NCR’s one of the most premier institutes for cardiac treatment')

st.write('')
jaypenk = 'https://www.jaypeehealthcare.com/'
if st.button("Jaypee's Official Site"):
    wb.open_new_tab(jaypenk)
st.write('')
st.write('')
st.markdown('4. **Max Hospital**')
st.write('')

st.text('Our Hospital Network')
st.write('')
st.write('Max Healthcare is Indias leading provider of world-class healthcare services, with 3000+ doctors and a network '
         'of 17 hospitals.')
st.write('')
st.markdown('**Our comprehensive diagnostics, technology-aided consultations with eminent doctors and quality healthcare at '
            'affordable cost are some of the many reasons Max Healthcare is every patients first choice.**')

st.write('')
st.write('')
ll,lk,lo = st.columns(3)
with lk:
    st.image('https://th.bing.com/th/id/OIP.dHncdaRL74Y3cFB9ecgV4AHaE8?w=263&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7', width=300)
st.write('')
st.write('')

maxdict = {
    'Awards': ['Operational Excellence Healthcare', 'Healthcare Leadership Award',
               'Health Brand of The Year - Healthcare', 'Center of Excellent for Bariatric Surgery',
               'Nursing Excellence', "Indias Most Trusted Healthcare..."]
}
maxdatafrm = pd.DataFrame(maxdict)
st.dataframe(maxdatafrm)
st.write('')
maxnk = 'https://www.maxhealthcare.in/'
if st.button("Max's Official Site"):
    wb.open_new_tab(maxnk)
st.write('')
st.write('')
st.markdown('5. **Fortis Hospital**')
st.write('')
st.write('Fortis Hospital is well known for using latest and advanced technology in cardiac bypass surgery, non-invasive '
         'cardiology and paediatric cardiac surgery to name a few. It has an advanced set of laboratories for nuclear medicines, '
         'haematology, radiology, biochemistry, microbiology and transfusion medicine.')
st.write('')
st.write('')
od,og,oy = st.columns(3)
with og:
    st.image('https://th.bing.com/th/id/OIP.v_2pIlH3N76wxFv3i9_GUQHaEK?w=283&h=180&c=7&r=0&o=5&dpr=1.25&pid=1.7', width=300)
st.write('')
st.write('')
me,rndm,rg = st.columns(3)
with rndm:
    st.markdown('**Features**')
st.markdown('**•** Travel and Visa assistance provided for foreign nationals.')
st.markdown('**•** Won the “Best Single Specialty Hospital in Cardiology” three times at ICICI Lombard – CNBC TV18 India Healthcare Awards.')
st.markdown('**•** Won the “Best Heart Care Center in North India” – Global Healthcare Excellence Awards 2013.')
st.markdown('**•** Won the “Best Institute Award” by Delhi Medical AssociationNABL accredited laboratories.')
st.markdown('**•** Hi-tech medical infrastructure facilities that give a better experience')
st.write('')
fortsnk = 'https://www.fortishealthcare.com/'
if st.button("Fortis Official Site"):
    wb.open_new_tab(fortsnk)
st.write('')
st.write('')

er,ea,et = st.columns(3)
with et:
    st.markdown('By **Ruhaan Gupta**')
    st.markdown('For Any Query, Contact At')
    query = f"[Query]({'http://192.168.1.5:8503'})"

    st.markdown(query, unsafe_allow_html=True)
    st.markdown('Phone: **+91 7428120450**')
    st.markdown('Email: **ruhaang0705@gmail.com**')

#http://192.168.1.5:8503

st.write('')
st.markdown('''___''')

st.write('')
st.write('')

read = pd.read_csv('tstcsv1.csv')

st.subheader('Comments')
st.write('')
crrnt = -1
n = True

for i in range(len(read['Name'])):
    crrnt += 1

    st.write('')
    a= str(read['Ratings'][crrnt])
    if a=='1 star':
        a = '⭐'
    elif a=='2 stars':
        a = '⭐⭐'
    elif a=='3 stars':
        a = '⭐⭐⭐'
    elif a=='4 stars':
        a = '⭐⭐⭐⭐'
    elif a=='5 stars':
        a = '⭐⭐⭐⭐⭐'

    st.markdown('**' + str((read['Name'][crrnt])) + '**'+' - ' + a)
    st.write(read['Comment'][crrnt])

st.write('')

st.markdown('''**__________________________________________________________________________________________**''')

st.markdown('**Write Comment**')
st.write('')

ratew = st.selectbox('How Will You Rate Us', ['1 star', '2 stars', '3 stars', '4 stars', '5 stars',])
adf,ade = st.columns(2)
with adf:
    namew = st.text_input('Enter your Name')
with ade:
    cmmntw = st.text_area('Enter your Opinion')


if st.button('📨'):
    read = pd.read_csv('tstcsv1.csv')
    dty = list(read['Name'])
    if namew == '':
        n = False
    dty.append(namew)

    dtr = list(read['Comment'])
    if cmmntw == '':
        n = False
    dtr.append(cmmntw)

    dtd = list(read['Ratings'])
    dtd.append(ratew)
    dict = {
        'Ratings':dtd,
        'Name': dty,
        'Comment': dtr
    }
    if n == True:
        datfrm = pd.DataFrame(dict)
        datfrm.to_csv('tstcsv1.csv')

        st.success('Successfully Sent The Comment')
        st.write('Reload The Page To See Your Comment')
    else:
        st.warning('Failed To Send')
        st.write('Make Sure You Have Not Left Anything Empty')
