from .models import *
from datetime import date, timedelta
from django.db.models import Q
from django.http import FileResponse, HttpResponse
import time

import io, os
from django.conf import settings
# reportlab.rl_config.TTFSearchPath.append(str(settings.BASE_DIR) + '/app/lib/reportlabs/fonts')
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, Flowable, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Roboto-Medium', 'Roboto-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Italic', 'Roboto-Italic.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-MediumItalic', 'Roboto-MediumItalic.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-BoldItalic', 'Roboto-BoldItalic.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Bold', 'Roboto-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-ThinItalic', 'Roboto-ThinItalic.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Thin', 'Roboto-Thin.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-Light', 'Roboto-Light.ttf'))
pdfmetrics.registerFont(TTFont('Roboto-LightItalic', 'Roboto-LightItalic.ttf'))
pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

def getAppointmentsList(appointments):
    today = date.today()
    tomorrow = date.today() + timedelta(days=1)
    appointmentsList = []
    if appointments:
        prevDay = appointments[0].date
        patientsList = []
        customData = {}
        key = 0
        obj = {}
        obj['key'] = key
        for appt in appointments:
            day = appt.date
            if prevDay != day:
                appointmentsList.append(obj)
                obj = {}
                key += 1
                obj['key'] = key
                obj['dates'] = day
                customData = {}
                patientsList = []
            appointment = {}
            appointment['id'] = appt.patient.id
            appointment['name'] = f"{appt.patient.fullname()}"
            appointment['time'] = f"{appt.time_from.strftime('%I:%M %p')} - {appt.time_till.strftime('%I:%M %p')}"
            appointment['visitNumber'] = appt.visit_number
            appointment['visitCompleted'] = appt.visit_completed
            patientsList.append(appointment)
            customData['patientsList'] = patientsList
            if day == today:
                customData['meta'] = 'Today'
            elif day == tomorrow:
                customData['meta'] = 'Tomorrow'
            else:
                customData['meta'] = day.strftime('%A')
            obj['dates'] = day
            obj['customData'] = customData
            prevDay = day
        if len(obj):
            appointmentsList.append(obj)
    return appointmentsList

def getAppointmentsByPartialDigits(query):
    appointments = Visit.objects.filter(Q(patient_id=query) | Q(date__day=query) | Q(date__month=query) | Q(date__year=query)).order_by('date')
    appointmentsList = getAppointmentsList(appointments)
    return appointmentsList

def getAppointmentsByName(query):
    appointments = Visit.objects.filter(Q(patient__first_name__icontains=query) | Q(patient__last_name__icontains=query)).order_by('date', 'time_from')
    appointmentsList = getAppointmentsList(appointments)
    return appointmentsList

def getAppointmentsByDate(query):
    appointments = Visit.objects.filter(date=query).order_by('time_from')
    appointmentsList = getAppointmentsList(appointments)
    return appointmentsList

def generatePDFReport(visit, examination):
    # examination = Examination.objects.get(id=1)
    # Create Bytestream buffer
    buf = io.BytesIO()
    # pdf = canvas.Canvas(buf, pagesize=A4)
    # width, height = A4
    # # pdf.translate(0, height)
    # text = pdf.beginText()
    # text.setTextOrigin(inch, inch)
    # # text.setFont('Arial', 16)
    # image = 'C:/Users/siddi/Documents/HarvardCS50W/finalProject-DRF/capstone/frontend/src/assets/avicennaLogo.png'
    # logo = pdf.drawImage(image, x= cm, y= height-(cm+45), preserveAspectRatio=True, anchor='c', mask='auto')
    # print(logo)
    # pdf.drawRightString(x= width-(cm), y= height-(cm+23.5), text='12th September, 2021')
    # print(date)
    # # date = pdf
    # # Add some lines of text
    # lines = [
    #     "This is line 1",
    #     "This is line 2",
    #     "This is line 3",
    #     "This is line 3",
    #     "This is line 3",
    #     "This is line 3",
    #     "This is line 3",
    #     examination.respiratory,
    #     str(width),
    #     str(height),
    # ]

    # for line in lines:
    #     text.textLine(line)

    # pdf.drawText(text)
    # pdf.showPage()

    # pdf.save()
    # buf.seek(0)

    doc = SimpleDocTemplate(buf,pagesize=A4,
                        rightMargin=cm,leftMargin=cm,
                        topMargin=cm,bottomMargin=18)
    doc.title = f"{visit.patient} - Report {visit.visit_number}"
    Story=[]
    logo = "C:/Users/siddi/Documents/HarvardCS50W/finalProject-DRF/capstone/frontend/src/assets/avicennaLogo.png"
    magName = "Pythonista"
    issueNum = 12
    subPrice = "99.00"
    limitedDate = "03/05/2010"
    freeGift = "tin foil hat"
    formatted_time = time.ctime()
    full_name = visit.patient.fullname()
    patient_id = visit.patient.id
    fathers_name = visit.patient.fathers_name
    mothers_name = visit.patient.mothers_name
    phone_number = visit.patient.Phone_Number
    blood_type = visit.patient.blood_type
    sex = visit.patient.sex
    dob = visit.patient.date_of_birth
    age = visit.patient.age
    occupation = visit.patient.occupation
    doctor = visit.assigned_doctor.fullname()
    bill = "$1245.00"
    pallor = u'\u2713' if examination.pallor else u'\u2715'
    icterus = u'\u2713' if examination.icterus else u'\u2715'
    oedema = u'\u2713' if examination.oedema else u'\u2715'
    lymphadenopathy = u'\u2713' if examination.lymphadenopathy else u'\u2715'
    koilonychia = u'\u2713' if examination.koilonychia else u'\u2715'
    clubbing = u'\u2713' if examination.clubbing else u'\u2715'
    others = examination.others
    chiefComplaints = examination.complaints
    diagnosis = examination.diagnosis
    respiratory = 'No abnormalities detected (NAD)' if examination.respiratory == 'NAD' else examination.respiratory
    cardiovascular = 'No abnormalities detected (NAD)' if examination.cardiovascular == 'NAD' else examination.cardiovascular
    cereberovascular = 'No abnormalities detected (NAD)' if examination.cereberovascular == 'NAD' else examination.cereberovascular
    per_abdominal = 'No abnormalities detected (NAD)' if examination.per_abdominal == 'NAD' else examination.per_abdominal
    local_examination = 'No abnormalities detected (NAD)' if examination.local_examination == 'NAD' else examination.local_examination
    address_parts = ["411 State St.", "Marshalltown, IA 50158"]
    # address = "The Burrow, Ottery St. Catchpole, Devonshire, England "
    address = visit.patient.address
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    im = Image(logo, 150, 29)
    im.hAlign = 'LEFT'
    sectionHeaderStyle = [
        ('BACKGROUND', (0,0), (-1, -1), '#C60000'),
        ('TEXTCOLOR', (0,0), (-1,-1), '#FFFFFF'),
        ('TEXTCOLOR', (0,0), (-1,-1), '#FFFFFF'),
        ('FONTSIZE', (0, 0), (-1,-1), 11),
        ('FONTNAME', (0, 0), (-1,-1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1,-1), 5)
    ]
    # Story.append(im)
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    styles.add(ParagraphStyle(name='CustomHeading', parent=styles['title'], alignment=TA_CENTER, fontSize=14, leading=22, spaceAfter=0))
    styles.add(ParagraphStyle(name='Date', parent=styles['Normal'], alignment=TA_RIGHT))
    styles.add(ParagraphStyle(name='Small', parent=styles['Normal'], fontSize=9))
    styles.add(ParagraphStyle(name='SmallRight', parent=styles['Small'], alignment=TA_RIGHT))
    ptext = '%s' % formatted_time
    tbl_data = [[im, Paragraph(ptext, styles["Date"])]]
    tbl = Table(tbl_data)
    tbl.setStyle(TableStyle([
        ('VALIGN',(0,0), (-1,-1), 'MIDDLE')
    ]))
    Story.append(tbl)
    # Story.append(Paragraph(ptext, styles["Date"]))
    Story.append(Spacer(1, 12))
    ptext = 'MEDICAL REPORT'
    Story.append(Paragraph(ptext, styles["CustomHeading"]))
    Story.append(Spacer(1, 5))
    # d = Drawing(100, 1)
    # d.add(Line)
    Story.append(HRFlowable(
        color='gray',
        thickness=0.3,
        width='100%',
        spaceAfter=5
    ))
    # tbl_data = [
    #     [Paragraph(f'Name: {full_name}', styles['Small']), Paragraph(f'Mobile: {phone_number}', styles["Small"]), Paragraph(f'Sex: {sex}', styles["Small"]) ],
    #     [Paragraph(f'DOB: {dob}', styles['Small']), Paragraph(f"Father's Name: {fathers_name}", styles["Small"]), Paragraph(f"Mother's Name: {mothers_name}", styles["Small"]) ],
    #     [Paragraph(f'Occupation: {occupation}', styles['Small']), Paragraph(f"Blood Type: {blood_type}", styles["Small"]), Paragraph(f"Date: {limitedDate}", styles["Small"]) ],
    #     [Paragraph(f"Address: {address}", styles["Small"])]
    # ]
    tbl_data = [
        ["Name", f": {full_name}", "", "Appointment Date", f": {limitedDate}"],
        ["ID", f": {patient_id}", "", "Age/Sex", f": {age} yrs / {sex}"],
        [Paragraph("Occupation", styles["BodyText"]), f": {occupation}", "", "Blood Type", f": {blood_type}"],
        [Paragraph("Doctor", styles["BodyText"]), f": {doctor}", "", "Mobile", f": {phone_number}"],
        ["Address", Paragraph(f": {address}", styles["BodyText"])]
    ]
    # tbl = Table(tbl_data, colWidths='100%')
    tbl = Table(tbl_data, spaceAfter=15)
    tbl.setStyle(TableStyle([
        # ('SPAN', (0,3), (2,3)),
        ('SPAN', (1,4), (-1,4)),
        ('VALIGN',(0,0), (-1,-1), 'TOP'),
        # ('FONTNAME', (0,0), (-1,-1), 'Roboto')
        # ('BOX', (0,3), (2,3), 1, 'black')
    ]))
    Story.append(tbl)
    # Story.append(HRFlowable(
    #     color='gray',
    #     thickness=0.3,
    #     width='100%',
    #     spaceBefore=5,
    #     spaceAfter=10
    # ))
    
    tbl_data = [['CHIEF COMPLAINTS'],]
    tbl = Table(tbl_data, colWidths='100%', style=sectionHeaderStyle, spaceAfter= 15)
    Story.append(tbl)
    Story.append(Paragraph(chiefComplaints, styles["BodyText"]))
    Story.append(Spacer(1, 25))

    tbl_data = [['PAST MEDICAL HISTORY'],]
    tbl = Table(tbl_data, colWidths='100%', style=sectionHeaderStyle, spaceAfter= 15)
    Story.append(tbl)
    chiefComplaints = 'Patient came in with rash on their back, constantly talking shit about their gramma'
    Story.append(Paragraph(chiefComplaints, styles["BodyText"]))
    Story.append(Spacer(1, 25))

    tbl_data = [['GENERAL'],]
    tbl = Table(tbl_data, colWidths='100%', style=sectionHeaderStyle, spaceAfter= 15)
    Story.append(tbl)
    tbl_data = [
        # [f"Pallor", f": Present", f"Clubbing", f": Present", f"Lymphadenopathy", f": --"],
        # [f"Icterus", f": --", f"Koilonychia", f": --", f"Oedema", f": --"],
        [f"Pallor: {pallor}", f"Clubbing: {clubbing}", f"Lymphadenopathy: {lymphadenopathy}"],
        [f"Icterus: {icterus}", f"Koilonychia: {koilonychia}", f"Oedema: {oedema}"],
    ]
    tbl = Table(tbl_data, colWidths='100%', spaceAfter=10)
    tbl.setStyle(TableStyle([
        # ('SPAN', (0,3), (2,3)),
        ('VALIGN',(0,0), (-1,-1), 'TOP'),
        # ('FONTNAME', (0,0), (-1,-1), 'Roboto')
        # ('BOX', (0,3), (2,3), 1, 'black')
    ]))
    Story.append(tbl)
    if others is not None:
        tbl_data = [
            [f"Others :", Paragraph(f"{others}", styles["BodyText"])]
        ]
        tbl = Table(tbl_data, spaceAfter=25, colWidths=(1.5*cm, None))
        tbl.setStyle(TableStyle([
            # ('SPAN', (0,3), (2,3)),
            ('VALIGN',(0,0), (-1,-1), 'TOP'),
            # ('FONTNAME', (0,0), (-1,-1), 'Roboto')
            # ('BOX', (0,3), (2,3), 1, 'black')
        ]))
        Story.append(tbl)
    else:
        Story.append(Spacer(1,15))

    tbl_data = [['VITALS'],]
    tbl = Table(tbl_data, colWidths='100%', style=sectionHeaderStyle, spaceAfter= 15)
    Story.append(tbl)
    tbl_data = [
        [f"BP: 124/122 mmHg", f"SpO2: 95%", f"Pulse: 63 bpm", f"Temp: 99 \xb0F"]
    ]
    tbl = Table(tbl_data, colWidths='100%', spaceAfter=25)
    Story.append(tbl)

    tbl_data = [['EXAMINATION'],]
    tbl = Table(tbl_data, colWidths='100%', style=sectionHeaderStyle, spaceAfter= 15)
    Story.append(tbl)
    tbl_data = [
        [f"Respiratory", ":", Paragraph(f"{respiratory}", styles["BodyText"])],
        [f"Cereberovascular", ":", Paragraph(f"{cereberovascular}", styles["BodyText"])],
        [f"Cardiovascular", ":", Paragraph(f"{cardiovascular}", styles["BodyText"])],
        [f"Per Abdominal", ":", Paragraph(f"{per_abdominal}", styles["BodyText"])],
        [f"Local Examination", ":", Paragraph(f"{local_examination}", styles["BodyText"])]
    ]
    tbl = Table(tbl_data, colWidths=(3*cm, 5, None), spaceAfter=25)
    tbl.setStyle(TableStyle([
        # ('SPAN', (0,3), (2,3)),
        ('VALIGN',(0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING',(0,0), (-1,-1), 15),
        # ('FONTNAME', (0,0), (-1,-1), 'Roboto')
        # ('BOX', (0,3), (2,3), 1, 'black')
    ]))
    Story.append(tbl)

    tbl_data = [['PROBABLE DIAGNOSIS'],]
    tbl = Table(tbl_data, colWidths='100%', style=sectionHeaderStyle, spaceAfter= 15)
    Story.append(tbl)
    tbl_data = [
        [Paragraph(f": {diagnosis}", styles["BodyText"])]
    ]
    tbl = Table(tbl_data, colWidths='100%', spaceAfter=10)
    tbl.setStyle(TableStyle([
        # ('SPAN', (0,3), (2,3)),
        ('VALIGN',(0,0), (-1,-1), 'TOP'),
        # ('FONTNAME', (0,0), (-1,-1), 'Roboto')
        # ('BOX', (0,3), (2,3), 1, 'black')
    ]))
    Story.append(tbl)
    # # Create return address
    # ptext = '%s' % full_name
    # Story.append(Paragraph(ptext, styles["Normal"]))       
    # for part in address_parts:
    #     ptext = '%s' % part.strip()
    #     Story.append(Paragraph(ptext, styles["Normal"]))   
    # Story.append(Spacer(1, 12))
    # ptext = 'Dear %s:' % full_name.split()[0].strip()
    # Story.append(Paragraph(ptext, styles["Normal"]))
    # Story.append(Spacer(1, 12))
    # ptext = 'We would like to welcome you to our subscriber base for %s Magazine! \
    #         You will receive %s issues at the excellent introductory price of $%s. Please respond by\
    #         %s to start receiving your subscription and get the following free gift: %s.' % (magName, 
    #                                                                                                 issueNum,
    #                                                                                                 subPrice,
    #                                                                                                 limitedDate,
    #                                                                                                 freeGift)
    # Story.append(Paragraph(ptext, styles["Justify"]))
    # Story.append(Spacer(1, 12))
    # ptext = 'Thank you very much and we look forward to serving you.'
    # Story.append(Paragraph(ptext, styles["Justify"]))
    # Story.append(Spacer(1, 12))
    # ptext = 'Sincerely,'
    # Story.append(Paragraph(ptext, styles["Normal"]))
    # Story.append(Spacer(1, 48))
    # ptext = 'Ima Sucker'
    # Story.append(Paragraph(ptext, styles["Normal"]))
    # Story.append(Spacer(1, 12))
    doc.build(Story)


    buf.seek(0)

    # pdf_root = str(settings.PDF_ROOT).replace('\\', '/')
    destination = settings.PDF_ROOT / f'{visit.patient.id}' / f'Generated'
    print(destination)
    filename = os.path.join(destination, f'{visit.patient} - Report {visit.visit_number}.pdf')
    # assert os.path.isfile(filename), f'{filename} is not a file'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
        f.write(buf.getbuffer())

    visit.visit_completed = True
    visit.save()

    return FileResponse(buf, as_attachment=False, filename=f'{visit.patient} - Report {visit.visit_number}.pdf')

