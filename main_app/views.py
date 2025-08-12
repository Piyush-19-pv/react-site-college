from django.shortcuts import render
from .forms import ContactForm
from django.shortcuts import render


# app/views.py
from django.shortcuts import render

def home(request): return render(request, 'main_app/home.html')
def Gen(request): return render(request, 'main_app/Gen.html')                                                                                              
def PrincipalMsg(request): return render(request, 'main_app/PrincipalMsg.html')
def Vision(request): return render(request, 'main_app/Vision.html')
def Mission(request): return render(request, 'main_app/Mission.html')
def Culture(request): return render(request, 'main_app/Culture.html')
def Core(request): return render(request, 'main_app/Core.html')
def Code(request): return render(request, 'main_app/Code.html')
def Governing(request): return render(request, 'main_app/Governing.html')
def Organogram(request): return render(request, 'main_app/Organogram.html')
def Principal(request): return render(request, 'main_app/Principal.html')
def Teaching(request): return render(request, 'main_app/Teaching.html')
from django.shortcuts import render, redirect
from .forms import FeedbackForm


import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

genai.configure(api_key="YOUR_API_KEY")  # 🔁 Replace with your API key
model = genai.GenerativeModel("gemini-pro")

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_input = data.get("message")

        response = model.generate_content(user_input)
        return JsonResponse({"reply": response.text})
    return JsonResponse({"error": "Invalid request"}, status=400)



    

def placements(request): return render(request, 'main_app/placements.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main_app/feedback_success.html')  # Create this success page
    else:
        form = FeedbackForm()
    return render(request, 'main_app/feedback.html', {'form': form})

# def Feedback(request): return render(request, 'main_app/feedback.html')
def Research(request): return render(request, 'main_app/Research.html')

def Programmes(request): return render(request, 'main_app/Programmes.html')
def CeepCourses(request): return render(request, 'main_app/CeepCourses.html')
def Certificate(request): return render(request, 'main_app/Certificate.html')
def Department(request): return render(request, 'main_app/Department.html')
def LessonPlans(request): return render(request, 'main_app/LessonPlans.html')
def AcadmicCalender(request): return render(request, 'main_app/AcadmicCalender.html')
def TimeTable(request): return render(request, 'main_app/TimeTable.html')
def copopso(request): return render(request, 'main_app/COPoPSO.html')
def library(request): return render(request, 'main_app/library.html')
def OurLearningResource(request): return render(request, 'main_app/OurLearningResource.html')
def OPCA(request): return render(request, 'main_app/OPCA.html')
def cultural_fest(request): return render(request, 'main_app/cultural_fest.html')
def job_fair(request): return render(request, 'main_app/job_fair.html')

def ncc(request): return render(request, 'main_app/ncc.html')
def Aqar(request): return render(request, 'main_app/Aqar.html')
def ssr(request): return render(request, 'main_app/ssr.html')


def gallery(request): return render(request, 'main_app/gallery.html')
def student_register(request): return render(request, 'main_app/student_register.html')
def faculty_register(request): return render(request, 'main_app/faculty_register.html')
def nirf(request): return render(request, 'main_app/nirf.html')
def rti(request): return render(request, 'main_app/rti.html')

def iqac(request): return render(request, 'main_app/iqac.html')



def sidebar_links_view(request):
    return render(request, 'myapp/sidebar_links.html')

def students_corner(request):
    return render(request, 'main_app/students_corner.html')

def institutional_policies(request):
    return render(request, 'main_app/institutional_policies.html')

def awards_achievements(request):
    return render(request, 'main_app/awards_achievements.html')

def allforms(request):
    return render(request, 'main_app/allforms.html')

def annual_reports(request):
    return render(request, 'main_app/annual_reports.html')

def alumni_association(request):
    return render(request, 'main_app/alumni_association.html')

def students_corner(request):
    return render(request, 'main_app/students_corner.html')

def students_corner(request):
    return render(request, 'main_app/students_corner.html')


def student_register(request):
    return render(request, 'main_app/student_register.html')
def faculty_register(request):
    return render(request, 'main_app/faculty_register.html')









def post_view(request):
    return render(request, 'career/post.html')

def com_view(request):
    return render(request, 'career/com.html')

def cc_view(request):
    return render(request, 'career/cc.html')

def opp_view(request):
    return render(request, 'career/opp.html')

def cu_view(request):
    return render(request, 'career/cu.html')

def te_view(request):
    return render(request, 'career/te.html')

def note_view(request):
    return render(request, 'career/note.html')

def cori_view(request):
    return render(request, 'career/cori.html')

# eventsviewsyear
from django.shortcuts import render

# List of event titles and slugs


def event_2025(request):
    return render(request, 'main_app/event_2025.html')

# start views in html page evnets
def world_thalassemia_day(request):
    return render(request, 'events/2025/world_thalassemia_day.html')

def retirement_ceremony(request):
    return render(request, 'events/2025/retirement_ceremony.html')

def awareness_lect_icc(request):
    return render(request, 'events/2025/awareness_lect_icc.html')

def farewell_party_wing2(request):
    return render(request, 'events/2025/farewell_party_wing2.html')
from django.shortcuts import render

def mega_job_fair(request):
    return render(request, 'events/mega_job_fair.html')

def world_ipr_day(request):
    return render(request, 'events/world_ipr_day.html')

def farewell_cs_dept(request):
    return render(request, 'events/farewell_cs_dept.html')

def farewell_mgmt_dept(request):
    return render(request, 'events/farewell_mgmt_dept.html')

def farewell_commerce_dept(request):
    return render(request, 'events/farewell_commerce_dept.html')

def slogan_writing_comp(request):
    return render(request, 'events/slogan_writing_comp.html')

def self_defense_training(request):
    return render(request, 'events/self_defense_training.html')

def red_cross_camp(request):
    return render(request, 'events/red_cross_camp.html')

def national_earth_day_nss(request):
    return render(request, 'events/national_earth_day_nss.html')

def guest_lec_mgt_dept(request):
    return render(request, 'events/guest_lec_mgt_dept.html')

def youth_red_cross_training(request):
    return render(request, 'events/youth_red_cross_training.html')

def world_earth_day_by_icc(request):
    return render(request, 'events/world_earth_day_by_icc.html')

def talk_show(request):
    return render(request, 'events/talk_show.html')

def world_heritage_day(request):
    return render(request, 'events/world_heritage_day.html')

def dental_health_checkup(request):
    return render(request, 'events/dental_health_checkup.html')

def industrial_visit_mgt_dept(request):
    return render(request, 'events/industrial_visit_mgt_dept.html')

def guest_lec_maths_dept(request):
    return render(request, 'events/guest_lec_maths_dept.html')

def fire_awareness_camp(request):
    return render(request, 'events/fire_awareness_camp.html')

def guest_lec_b_voc(request):
    return render(request, 'events/guest_lec_b_voc.html')

def first_aid_camp(request):
    return render(request, 'events/first_aid_camp.html')

def poster_making_comp_icc(request):
    return render(request, 'events/poster_making_comp_icc.html')

def world_health_day_by_yrc(request):
    return render(request, 'events/world_health_day_by_yrc.html')

def prize_distribution_by_iyc(request):
    return render(request, 'events/prize_distribution_by_iyc.html')

def awareness_on_helmets(request):
    return render(request, 'events/awareness_on_helmets.html')

def nukkad_natak(request):
    return render(request, 'events/nukkad_natak.html')

def documentary_on_posh(request):
    return render(request, 'events/documentary_on_posh.html')

def guest_lect_comp_dept(request):
    return render(request, 'events/guest_lect_comp_dept.html')

def guest_lec_pol_sci_dept(request):
    return render(request, 'events/guest_lec_pol_sci_dept.html')

def women_safety_program(request):
    return render(request, 'events/women_safety_program.html')

def career_prog_comm_dept(request):
    return render(request, 'events/career_prog_comm_dept.html')

def guest_lec_hist_dept(request):
    return render(request, 'events/guest_lec_hist_dept.html')

def trip_comp_sc_mgmt_dept(request):
    return render(request, 'events/trip_comp_sc_mgmt_dept.html')


def tringa(request):
    return render(request, 'events/tringa.html')
# Add more views for each event page


def event_2024(request):
    return render(request, 'main_app/event_2024.html')

# views.py

# views.py
from django.shortcuts import render

def lohri_function(request):
    return render(request, 'events/2024/lohri_function.html')

def vivekanand_jayanti(request):
    return render(request, 'events/2024/vivekanand_jayanti.html')

def iqac_meeting(request):
    return render(request, 'events/2024/iqac_meeting.html')

def national_math_day(request):
    return render(request, 'events/2024/national_math_day.html')

def navy_day(request):
    return render(request, 'events/2024/navy_day.html')

def world_aids_day(request):
    return render(request, 'events/2024/world_aids_day.html')

def env_control_day(request):
    return render(request, 'events/2024/env_control_day.html')

def poster_hindi(request):
    return render(request, 'events/2024/poster_hindi.html')

def felicitations(request):
    return render(request, 'events/2024/felicitations.html')

def interzonal_fest(request):
    return render(request, 'events/2024/interzonal_fest.html')

def zonal_youth(request):
    return render(request, 'events/2024/zonal_youth.html')

def archery_tournament(request):
    return render(request, 'events/2024/archery_tournament.html')

def poster_comp_sc(request):
    return render(request, 'events/2024/poster_comp_sc.html')

def digital_rangoli(request):
    return render(request, 'events/2024/digital_rangoli.html')

def visit_chem(request):
    return render(request, 'events/2024/visit_chem.html')

def inductions(request):
    return render(request, 'events/2024/inductions.html')

def ipr_workshop(request):
    return render(request, 'events/2024/ipr_workshop.html')

def best_out_waste(request):
    return render(request, 'events/2024/best_out_waste.html')

def fire_safety(request):
    return render(request, 'events/2024/fire_safety.html')

def freshers_ba_ma(request):
    return render(request, 'events/2024/freshers_ba_ma.html')

def blood_donation(request):
    return render(request, 'events/2024/blood_donation.html')

def freshers_party(request):
    return render(request, 'events/2024/freshers_party.html')

def youth_develop(request):
    return render(request, 'events/2024/youth_develop.html')

def hemoglobin_test(request):
    return render(request, 'events/2024/hemoglobin_test.html')

def nss_day(request):
    return render(request, 'events/2024/nss_day.html')

def poster_ncc(request):
    return render(request, 'events/2024/poster_ncc.html')

def hon_walk(request):
    return render(request, 'events/2024/hon_walk.html')

def deworming_day(request):
    return render(request, 'events/2024/deworming_day.html')

def eco_guest(request):
    return render(request, 'events/2024/eco_guest.html')

def guest_aryabhatta(request):
    return render(request, 'events/2024/guest_aryabhatta.html')

def panchayati_raj(request):
    return render(request, 'events/2024/panchayati_raj.html')

def anti_drug(request):
    return render(request, 'events/2024/anti_drug.html')

def freshers_general(request):
    return render(request, 'events/2024/freshers_general.html')

def women_cell(request):
    return render(request, 'events/2024/women_cell.html')

def guest_math(request):
    return render(request, 'events/2024/guest_math.html')

def guest_comm(request):
    return render(request, 'events/2024/guest_comm.html')

def drug_seminar(request):
    return render(request, 'events/2024/drug_seminar.html')

def tree_plantation(request):
    return render(request, 'events/2024/tree_plantation.html')

def voter_awareness(request):
    return render(request, 'events/2024/voter_awareness.html')

def talent_hunt(request):
    return render(request, 'events/2024/talent_hunt.html')

def slogan_comp(request):
    return render(request, 'events/2024/slogan_comp.html')

def com_eng(request):
    return render(request, 'events/2024/com_eng.html')

def first_aid_day(request):
    return render(request, 'events/2024/first_aid_day.html')

def literacy_day(request):
    return render(request, 'events/2024/literacy_day.html')

def paralympic_winners(request):
    return render(request, 'events/2024/paralympic_winners.html')

def guest_history(request):
    return render(request, 'events/2024/guest_history.html')


def placeholder(request, title):
    return render(request, 'placeholder.html', {'message': f'{title} Page Coming Soon'})

# Now each view (copy this pattern for all views)


# def lohri_function(request): return render(request, "events/2024/Lohri Function.html")
# def vivekanand_jayanti(request): return render(request, "events/2024/Vivekanand Jayanti.html")
# def iqac_meeting(request): return render(request, "events/2024/IQAC Meeting.html")
# def national_math_day(request): return render(request, "events/2024/National Math Day.html")
# def navy_day(request): return render(request, "events/2024/Navy Day.html")
# def world_aids_day(request): return render(request, "events/2024/World AIDS Day.html")
# def env_control_day(request): return render(request, "events/2024/National Env. Control Day.html")
# def poster_hindi(request): return render(request, "events/2024/Poster Comp Hindi Dept.html")
# def felicitations(request): return render(request, "events/2024/Felicitation Inter ZYF.html")
# def interzonal_fest(request): return render(request, "events/2024/Interzonal Youth Fest.html")
# def zonal_youth(request): return render(request, "events/2024/Zonal Youth Festival.html")
# def archery_tournament(request): return render(request, "events/2024/Archery Tournament.html")
# def poster_comp_sc(request): return render(request, "events/2024/Poster Comp. Sc..html")
# def digital_rangoli(request): return render(request, "events/2024/Digital Rangoli Comp Sc.html")
# def visit_chem(request): return render(request, "events/2024/Visit Chem Dept..html")
# def inductions(request): return render(request, "events/2024/Induction Prog..html")
# def ipr_workshop(request): return render(request, "events/2024/Workshop on IPR Culture.html")
# def best_out_waste(request): return render(request, "events/2024/Best Out of Waste.html")
# def fire_safety(request): return render(request, "events/2024/Fire Safety Training.html")
# def freshers_ba_ma(request): return render(request, "events/2024/Freshers Party BA, MA.html")
# def blood_donation(request): return render(request, "events/2024/Blood Donation Camp.html")
# def freshers_party(request): return render(request, "events/2024/Freshers Party.html")
# def youth_develop(request): return render(request, "events/2024/Youth Develop Program.html")
# def hemoglobin_test(request): return render(request, "events/2024/Hemoglobin Testing Camp.html")
# def nss_day(request): return render(request, "events/2024/NSS Day Celebration.html")
# def poster_ncc(request): return render(request, "events/2024/Poster Competition NCC.html")
# def hon_walk(request): return render(request, "events/2024/Walk at Hon Event.html")
# def deworming_day(request): return render(request, "events/2024/National Deworming Day.html")
# def eco_guest(request): return render(request, "events/2024/Expert Lect Eco Dept.html")
# def guest_aryabhatta(request): return render(request, "events/2024/Guest Lect Aryabhatta.html")
# def panchayati_raj(request): return render(request, "events/2024/Panchayati Raj.html")
# def anti_drug(request): return render(request, "events/2024/Anti Drug.html")
# def freshers_general(request): return render(request, "events/2024/Fresher's Party.html")
# def women_cell(request): return render(request, "events/2024/Women Cell.html")
# def guest_math(request): return render(request, "events/2024/Guest Lect Math Dept.html")
# def guest_comm(request): return render(request, "events/2024/Guest Lect Comm Dept.html")
# def drug_seminar(request): return render(request, "events/2024/Seminar Drug Prevention.html")
# def tree_plantation(request): return render(request, "events/2024/Tree Plantation.html")
# def voter_awareness(request): return render(request, "events/2024/Voter Awareness Rally.html")
# def talent_hunt(request): return render(request, "events/2024/Talent Hunt.html")
# def slogan_comp(request): return render(request, "events/2024/Slogan Competition Pol. Dept.html")
# def com_eng(request): return render(request, "events/2024/Com. Lect Eng. Dept.html")
# def first_aid_day(request): return render(request, "events/2024/World First Aid Day.html")
# def literacy_day(request): return render(request, "events/2024/International Literacy Day.html")
# def paralympic_winners(request): return render(request, "events/2024/Winners of Paralympics.html")
# def guest_history(request): return render(request, "events/2024/Guest Lect History Dept.html")

def event_2023(request):
    return render(request, 'main_app/event_2023.html')





def national_mathematics_day(request): return render(request, 'events/2023/national_mathematics_day.html')
def guest_lecture_chem(request): return render(request, 'events/2023/guest_lecture_chem.html')
def bronze_medal_asian_games(request): return render(request, 'events/2023/bronze_medal_asian_games.html')
def env_protection_campaign(request): return render(request, 'events/2023/env_protection_campaign.html')
def guest_lecture_sanskrit(request): return render(request, 'events/2023/guest_lecture_sanskrit.html')
def guest_lecture_math(request): return render(request, 'events/2023/guest_lecture_math.html')
def guest_lecture_polsc(request): return render(request, 'events/2023/guest_lecture_polsc.html')
def industry_visit(request): return render(request, 'events/2023/industry_visit.html')
def world_ozone_day(request): return render(request, 'events/2023/world_ozone_day.html')
def social_entrepreneur_course(request): return render(request, 'events/2023/social_entrepreneur_course.html')
def first_aid_yrc(request): return render(request, 'events/2023/first_aid_yrc.html')
def slogan_writing(request): return render(request, 'events/2023/slogan_writing.html')
def letter_writing(request): return render(request, 'events/2023/letter_writing.html')
def industrial_visit_bcom(request): return render(request, 'events/2023/industrial_visit_bcom.html')
def induction(request): return render(request, 'events/2023/induction.html')
def slow_cycling_competition(request): return render(request, 'events/2023/slow_cycling_competition.html')
def ek_tiranga_prog(request): return render(request, 'events/2023/ek_tiranga_prog.html')
def ncc_workshop(request): return render(request, 'events/2023/ncc_workshop.html')
def library_day(request): return render(request, 'events/2023/library_day.html')
def youth_dialogue(request): return render(request, 'events/2023/youth_dialogue.html')
def env_nss(request): return render(request, 'events/2023/env_nss.html')
def comm_skills_course(request): return render(request, 'events/2023/comm_skills_course.html')
def first_aid_training(request): return render(request, 'events/2023/first_aid_training.html')
def world_redcross(request): return render(request, 'events/2023/world_redcross.html')
def blood_donation(request): return render(request, 'events/2023/blood_donation.html')
def nss_camp(request): return render(request, 'events/2023/nss_camp.html')
def millet_year(request): return render(request, 'events/2023/millet_year.html')


def event_2022(request):
    return render(request, 'main_app/event_2022.html')




def iqac_meeting(request): return render(request, 'events/2022/iqac_meeting.html')
def health_talk_yrc(request): return render(request, 'events/2022/health_talk_yrc.html')
def uni_outreach_programme(request): return render(request, 'events/2022/uni_outreach_programme.html')
def guest_lect_history(request): return render(request, 'events/2022/guest_lect_history.html')
def imt_industries_expo(request): return render(request, 'events/2022/imt_industries_expo.html')
def talk_design_destiny(request): return render(request, 'events/2022/talk_design_destiny.html')
def archery_competition(request): return render(request, 'events/2022/archery_competition.html')
def navy_day(request): return render(request, 'events/2022/navy_day.html')
def aids_day(request): return render(request, 'events/2022/aids_day.html')
def mba_expo(request): return render(request, 'events/2022/mba_expo.html')
def fdp_wellness(request): return render(request, 'events/2022/fdp_wellness.html')
def guest_lect_hindi(request): return render(request, 'events/2022/guest_lect_hindi.html')
def env_protection(request): return render(request, 'events/2022/env_protection.html')
def world_hindu_council(request): return render(request, 'events/2022/world_hindu_council.html')
def constitution_day(request): return render(request, 'events/2022/constitution_day.html')
def guest_lect_computer(request): return render(request, 'events/2022/guest_lect_computer.html')
def career_awareness(request): return render(request, 'events/2022/career_awareness.html')
def poetry_reading(request): return render(request, 'events/2022/poetry_reading.html')
def intl_youth_day(request): return render(request, 'events/2022/intl_youth_day.html')
def motivational_speech(request): return render(request, 'events/2022/motivational_speech.html')
def children_day(request): return render(request, 'events/2022/children_day.html')
def natak_commerce(request): return render(request, 'events/2022/natak_commerce.html')
def blockchain_seminar(request): return render(request, 'events/2022/blockchain_seminar.html')
def legal_services(request): return render(request, 'events/2022/legal_services.html')
def shooting_championship(request): return render(request, 'events/2022/shooting_championship.html')
def voter_awareness(request): return render(request, 'events/2022/voter_awareness.html')
def eye_checkup(request): return render(request, 'events/2022/eye_checkup.html')
def guest_lect_english(request): return render(request, 'events/2022/guest_lect_english.html')
def guest_lect_chem(request): return render(request, 'events/2022/guest_lect_chem.html')
def induction(request): return render(request, 'events/2022/induction.html')
def env_awareness(request): return render(request, 'events/2022/env_awareness.html')
def inspiration_day(request): return render(request, 'events/2022/inspiration_day.html')
def guest_lect_maths(request): return render(request, 'events/2022/guest_lect_maths.html')
def painting_competition(request): return render(request, 'events/2022/painting_competition.html')
def guest_lect_history2(request): return render(request, 'events/2022/guest_lect_history2.html')
def career_workshop(request): return render(request, 'events/2022/career_workshop.html')
def seminar_crimes(request): return render(request, 'events/2022/seminar_crimes.html')
def elderly_day(request): return render(request, 'events/2022/elderly_day.html')
def shri_ratan_singh(request): return render(request, 'events/2022/shri_ratan_singh.html')
def career_counselling(request): return render(request, 'events/2022/career_counselling.html')
def gandhi_jayanti(request): return render(request, 'events/2022/gandhi_jayanti.html')
def physics_lab_tour(request): return render(request, 'events/2022/physics_lab_tour.html')
def parlour_certificate(request): return render(request, 'events/2022/parlour_certificate.html')
def guest_lect_polsc(request): return render(request, 'events/2022/guest_lect_polsc.html')
def bhagat_singh_jayanti(request): return render(request, 'events/2022/bhagat_singh_jayanti.html')
def nss_activities(request): return render(request, 'events/2022/nss_activities.html')
def pushpanjali_nss(request): return render(request, 'events/2022/pushpanjali_nss.html')
def rangoli_competition(request): return render(request, 'events/2022/rangoli_competition.html')
def poster_making(request): return render(request, 'events/2022/poster_making.html')
def hindi_divas(request): return render(request, 'events/2022/hindi_divas.html')
def nss_nutrition(request): return render(request, 'events/2022/nss_nutrition.html')


def event_2021(request):
    return render(request, 'main_app/event_2021.html')

    # starteventviews2021


def unnat_bharat_abhiyan(request): return render(request, 'events/2021/unnat_bharat_abhiyan.html')
def webinar_data_analytics(request): return render(request, 'events/2021/webinar_data_analytics.html')
def career_guidance(request): return render(request, 'events/2021/career_guidance.html')
def maths_webinar(request): return render(request, 'events/2021/maths_webinar.html')
def ptm(request): return render(request, 'events/2021/ptm.html')
def seminar_comp_sc(request): return render(request, 'events/2021/seminar_comp_sc.html')
def nat_web_commerce(request): return render(request, 'events/2021/nat_web_commerce.html')
def pol_sci_webinar(request): return render(request, 'events/2021/pol_sci_webinar.html')
def math_webinar(request): return render(request, 'events/2021/math_webinar.html')
def guest_mgmt(request): return render(request, 'events/2021/guest_mgmt.html')
def career_counselling(request): return render(request, 'events/2021/career_counselling.html')
def azadi_ka_amrit(request): return render(request, 'events/2021/azadi_ka_amrit.html')
def recruitment_drive(request): return render(request, 'events/2021/recruitment_drive.html')
def covid_vaccination(request): return render(request, 'events/2021/covid_vaccination.html')
def webinar_commerce(request): return render(request, 'events/2021/webinar_commerce.html')
def guest_commerce(request): return render(request, 'events/2021/guest_commerce.html')
def blood_donation(request): return render(request, 'events/2021/blood_donation.html')
def wd_comp_sc(request): return render(request, 'events/2021/wd_comp_sc.html')
def archery_comp(request): return render(request, 'events/2021/archery_comp.html')
def navy_day(request): return render(request, 'events/2021/navy_day.html')
def guest_gandhi(request): return render(request, 'events/2021/guest_gandhi.html')
def swachh_bharat(request): return render(request, 'events/2021/swachh_bharat.html')
def fla_webinar(request): return render(request, 'events/2021/fla_webinar.html')
def health_talk(request): return render(request, 'events/2021/health_talk.html')
def world_aids_day(request): return render(request, 'events/2021/world_aids_day.html')
def constitution_day(request): return render(request, 'events/2021/constitution_day.html')
def guest_comp_sc(request): return render(request, 'events/2021/guest_comp_sc.html')
def poster_comp_sc(request): return render(request, 'events/2021/poster_comp_sc.html')
def audio_project(request): return render(request, 'events/2021/audio_project.html')
def history_lecture(request): return render(request, 'events/2021/history_lecture.html')
def seminar_comm(request): return render(request, 'events/2021/seminar_comm.html')
def report_making(request): return render(request, 'events/2021/report_making.html')
def health_checkup(request): return render(request, 'events/2021/health_checkup.html')
def rangoli_comp(request): return render(request, 'events/2021/rangoli_comp.html')
def interactive_session(request): return render(request, 'events/2021/interactive_session.html')
def vigilance_week(request): return render(request, 'events/2021/vigilance_week.html')

    #endviews2021

def event_2020(request):
    return render(request, 'main_app/event_2020.html')
#start2020




def national_science_day(request):
    return render(request, 'events/2020/national_science_day.html')

def guest_lect_pol_sc(request):
    return render(request, 'events/2020/guest_lect_pol_sc.html')

def quiz_competition(request):
    return render(request, 'events/2020/quiz_competition.html')

def yrc_camp(request):
    return render(request, 'events/2020/yrc_camp.html')

def unnat_bharat_abhiyan(request):
    return render(request, 'events/2020/unnat_bharat_abhiyan.html')

def seminar_entrepreneurship(request):
    return render(request, 'events/2020/seminar_entrepreneurship.html')

def guest_lect_history_dept(request):
    return render(request, 'events/2020/guest_lect_history_dept.html')

def guest_lect_m_o_v(request):
    return render(request, 'events/2020/guest_lect_m_o_v.html')

def constitution_day(request):
    return render(request, 'events/2020/constitution_day.html')

def annual_nursing_camp(request):
    return render(request, 'events/2020/annual_nursing_camp.html')

def session_health_happiness(request):
    return render(request, 'events/2020/session_health_happiness.html')

def industrial_visit(request):
    return render(request, 'events/2020/industrial_visit.html')

def health_talk_checkup_camp(request):
    return render(request, 'events/2020/health_talk_checkup_camp.html')

def story_writing_competition(request):
    return render(request, 'events/2020/story_writing_competition.html')

def environment_protection(request):
    return render(request, 'events/2020/environment_protection.html')

def prog_company_secretary(request):
    return render(request, 'events/2020/prog_company_secretary.html')

def programme_ewaste_mgmt(request):
    return render(request, 'events/2020/programme_ewaste_mgmt.html')

def seminar_road_safety(request):
    return render(request, 'events/2020/seminar_road_safety.html')

def jagriti_hariyanvi_culture(request):
    return render(request, 'events/2020/jagriti_hariyanvi_culture.html')

def prog_swami_vivekanand(request):
    return render(request, 'events/2020/prog_swami_vivekanand.html')

def republic_day(request):
    return render(request, 'events/2020/republic_day.html')

def a_talk_on_health(request):
    return render(request, 'events/2020/a_talk_on_health.html')

def national_voters_day(request):
    return render(request, 'events/2020/national_voters_day.html')

def debate_competition(request):
    return render(request, 'events/2020/debate_competition.html')

def health_awareness_talk(request):
    return render(request, 'events/2020/health_awareness_talk.html')

def rally_and_competitions(request):
    return render(request, 'events/2020/rally_and_competitions.html')

def lecture_on_development(request):
    return render(request, 'events/2020/lecture_on_development.html')

def a_survey_in_chandawali(request):
    return render(request, 'events/2020/a_survey_in_chandawali.html')

def national_youth_day(request):
    return render(request, 'events/2020/national_youth_day.html')

def seminar_on_women(request):
    return render(request, 'events/2020/seminar_on_women.html')

#end 20020
#start2019
def event_2019(request):
    return render(request, 'main_app/event_2019.html')


# Views rendering templates from events/2019/

def nss_camp(request):
    return render(request, 'events/2019/nss_camp.html')

def national_mathematics_day(request):
    return render(request, 'events/2019/national_mathematics_day.html')

def yrc_training_camp(request):
    return render(request, 'events/2019/yrc_training_camp.html')

def world_aids_day(request):
    return render(request, 'events/2019/world_aids_day.html')

def constitution_day(request):
    return render(request, 'events/2019/constitution_day.html')

def health_talk(request):
    return render(request, 'events/2019/health_talk.html')

def archery_competition(request):
    return render(request, 'events/2019/archery_competition.html')

def one_day_seminar_on_we(request):
    return render(request, 'events/2019/one_day_seminar_on_we.html')

def interactive_session_fp(request):
    return render(request, 'events/2019/interactive_session_fp.html')

def national_education_day(request):
    return render(request, 'events/2019/national_education_day.html')

def program_shabad_kirtan(request):
    return render(request, 'events/2019/program_shabad_kirtan.html')

def blood_donation_camp(request):
    return render(request, 'events/2019/blood_donation_camp.html')

def vigilance_awareness_week(request):
    return render(request, 'events/2019/vigilance_awareness_week.html')

def inter_university_quiz(request):
    return render(request, 'events/2019/inter_university_quiz.html')

def international_child_day(request):
    return render(request, 'events/2019/international_child_day.html')

def declamation_competition(request):
    return render(request, 'events/2019/declamation_competition.html')

def educational_trip_ba(request):
    return render(request, 'events/2019/educational_trip_ba.html')

def motivational_lecture(request):
    return render(request, 'events/2019/motivational_lecture.html')

def guest_lecture_hindi_deptt(request):
    return render(request, 'events/2019/guest_lecture_hindi_deptt.html')

def tree_plantation(request):
    return render(request, 'events/2019/tree_plantation.html')

def guest_lecture_media(request):
    return render(request, 'events/2019/guest_lecture_media.html')

def voters_awareness_rally(request):
    return render(request, 'events/2019/voters_awareness_rally.html')

def swachhta_campaign(request):
    return render(request, 'events/2019/swachhta_campaign.html')

def right_way_to_humanity(request):
    return render(request, 'events/2019/right_way_to_humanity.html')

def science_quiz_competition(request):
    return render(request, 'events/2019/science_quiz_competition.html')

def awareness_to_students(request):
    return render(request, 'events/2019/awareness_to_students.html')

def counseling_session(request):
    return render(request, 'events/2019/counseling_session.html')

def postermaking_competition(request):
    return render(request, 'events/2019/postermaking_competition.html')

def guest_lect_by_history(request):
    return render(request, 'events/2019/guest_lect_by_history.html')

def nss_day(request):
    return render(request, 'events/2019/nss_day.html')

def slogan_writing_comp(request):
    return render(request, 'events/2019/slogan_writing_comp.html')
#end2019

def event_2018(request):
    return render(request, 'main_app/event_2018.html')
#atrt2018



def nss_camp(request): return render(request, 'events/2018/nss_camp.html')
def national_mathematics_day(request): return render(request, 'events/2018/national_mathematics_day.html')
def yrc_training_camp(request): return render(request, 'events/2018/yrc_training_camp.html')
def world_aids_day(request): return render(request, 'events/2018/world_aids_day.html')
def constitution_day(request): return render(request, 'events/2018/constitution_day.html')
def health_talk(request): return render(request, 'events/2018/health_talk.html')
def archery_competition(request): return render(request, 'events/2018/archery_competition.html')
def one_day_seminar_on_we(request): return render(request, 'events/2018/one_day_seminar_on_we.html')
def interactive_session_fp(request): return render(request, 'events/2018/interactive_session_fp.html')
def national_education_day(request): return render(request, 'events/2018/national_education_day.html')
def program_shabad_kirtan(request): return render(request, 'events/2018/program_shabad_kirtan.html')
def blood_donation_camp(request): return render(request, 'events/2018/blood_donation_camp.html')
def vigilance_awareness_week(request): return render(request, 'events/2018/vigilance_awareness_week.html')
def inter_university_quiz(request): return render(request, 'events/2018/inter_university_quiz.html')
def international_child_day(request): return render(request, 'events/2018/international_child_day.html')
def declamation_competition(request): return render(request, 'events/2018/declamation_competition.html')
def educational_trip_ba(request): return render(request, 'events/2018/educational_trip_ba.html')
def motivational_lecture(request): return render(request, 'events/2018/motivational_lecture.html')
def guest_lecture_hindi_deptt(request): return render(request, 'events/2018/guest_lecture_hindi_deptt.html')
def tree_plantation(request): return render(request, 'events/2018/tree_plantation.html')
def guest_lecture_media(request): return render(request, 'events/2018/guest_lecture_media.html')
def voters_awareness_rally(request): return render(request, 'events/2018/voters_awareness_rally.html')
def swachhta_campaign(request): return render(request, 'events/2018/swachhta_campaign.html')
def right_way_to_humanity(request): return render(request, 'events/2018/right_way_to_humanity.html')
def science_quiz_competition(request): return render(request, 'events/2018/science_quiz_competition.html')
def awareness_to_students(request): return render(request, 'events/2018/awareness_to_students.html')
def counseling_session(request): return render(request, 'events/2018/counseling_session.html')
def postermaking_competition(request): return render(request, 'events/2018/postermaking_competition.html')
def guest_lect_by_history(request): return render(request, 'events/2018/guest_lect_by_history.html')
def nss_day(request): return render(request, 'events/2018/nss_day.html')
def slogan_writing_comp(request): return render(request, 'events/2018/slogan_writing_comp.html')

# 2018 Events
def alumni_meet(request): return render(request, 'events/alumni_meet.html')
def girls_awareness(request): return render(request, 'events/girls_awareness.html')
def chandawali_village_visit(request): return render(request, 'events/chandawali_village_visit.html')
def guest_lecture_by_pol_sc(request): return render(request, 'events/guest_lecture_by_pol_sc.html')
def importance_awareness(request): return render(request, 'events/importance_awareness.html')
def nss_day_2018(request): return render(request, 'events/nss_day_2018.html')
def inter_university_ppt(request): return render(request, 'events/inter_university_ppt.html')
def seminar_on_human_value(request): return render(request, 'events/seminar_on_human_value.html')
def career_counselling(request): return render(request, 'events/career_counselling.html')
def guest_lecture_by_comp_sci(request): return render(request, 'events/guest_lecture_by_comp_sci.html')
def spot_painting_history(request): return render(request, 'events/spot_painting_history.html')
def guest_lecture_by_eng(request): return render(request, 'events/guest_lecture_by_eng.html')
def guest_lecture_by_eco(request): return render(request, 'events/guest_lecture_by_eco.html')
def guest_lecture_by_comp(request): return render(request, 'events/guest_lecture_by_comp.html')
def guest_lecture_on_noble(request): return render(request, 'events/guest_lecture_on_noble.html')
def tree_plantation_2018(request): return render(request, 'events/tree_plantation_2018.html')
def seminar_on_solid_waste(request): return render(request, 'events/seminar_on_solid_waste.html')
def nss_swacch_bharat(request): return render(request, 'events/nss_swacch_bharat.html')
def yrc_training_camp_2018(request): return render(request, 'events/yrc_training_camp_2018.html')
def job_fair(request): return render(request, 'events/job_fair.html')
def essay_writing(request): return render(request, 'events/essay_writing.html')
def guest_lecture_on_gs(request): return render(request, 'events/guest_lecture_on_gs.html')
def sebi_regional_seminar(request): return render(request, 'events/sebi_regional_seminar.html')



#nd2018


# ///department views




def department_computer_science(request):
    return render(request, 'departments/computer_science.html')

def department_commerce(request):
    return render(request, 'departments/commerce.html')

def department_economics(request):
    return render(request, 'departments/economics.html')

def department_hindi(request):
    return render(request, 'departments/hindi.html')

def department_management(request):
    return render(request, 'departments/management.html')

def department_mathematics(request):
    return render(request, 'departments/mathematics.html')

def department_physics(request):
    return render(request, 'departments/physics.html')

def department_physical_education(request):
    return render(request, 'departments/physical_education.html')

def department_environmental_science(request):
    return render(request, 'departments/environmental_science.html')

def department_chemistry(request):
    return render(request, 'departments/chemistry.html')

def department_sanskrit(request):
    return render(request, 'departments/sanskrit.html')

def department_history(request):
    return render(request, 'departments/history.html')

def department_vocational_studies(request):
    return render(request, 'departments/vocational_studies.html')

def department_library_science(request):
    return render(request, 'departments/library_science.html')





def placement(request):
    return render(request, 'main_app/placement.html')

    return render(request, 'main_app/placement.html')

def director_message(request):
    return render(request, 'main_app/director_message.html')

def placement_acb(request):
    return render(request, 'main_app/placement_acb.html')

def contact_director(request):
    return render(request, 'main_app/contact_director.html')

def research_sort(request):
    return render(request, 'main_app/research_sort.html')

# def index(request):
#     return render(request, 'main_app/index.html')

# def about(request):
#     return render(request, 'main_app/about.html')

# def contact(request):
#     return render(request, 'main_app/contact.html')
def newsletter(request):
    return render(request, 'main_app/newsletter.html')
def about_admission(request):
    return render(request, 'main_app/about_admission.html')
def workshops(request):
    return render(request, 'main_app/workshops.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main_app/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    return render(request, 'main_app/contact.html', {'form': form})



# app_name/views.py
from django.shortcuts import render, redirect
from .forms import ApplicationForm

def apply_now(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('application_success')
    else:
        form = ApplicationForm()
    return render(request, 'main_app/apply_now.html', {'form': form})

def application_success(request):
    return render(request, 'main_app/application_success.html')




