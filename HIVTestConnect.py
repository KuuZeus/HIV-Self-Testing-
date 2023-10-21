import streamlit as st
from streamlit_option_menu import option_menu
import os

## App general customization
st.set_page_config(page_title='HIVTestConnect', page_icon= '👋')

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



def main():
    with st.sidebar:

        choice =option_menu(menu_title =None,
                    options =["Home", "About", "What to Know","Why Test" ,"Before you Test" ,"How to Test" ,"What your results mean" ,"After the Test", "Living with HIV" ,"Resources" ],
                    # orientation='horizontal',
                    default_index= 0)
        # choice= st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.header("Empower yourself: HIV Testing Made Easy!")
        st.write("--------------------------------")
        st.video("https://youtu.be/oHKEE0WidMU?si=oUilzmMSrisJYLpR", format = 'video/mp4', start_time = 0)
        st.write('________________________________________________________________')

        # st.write("Select from the menu to learn more")


    elif choice == 'About':
        st.title('ABOUT')
        st.write('________________________________________________________________')
        st.subheader('Introduction')
        # st.subheader('About HIV Self-Testing and the 95-95-95 Targets')
        st.write("HIV self-testing empowers individuals to take control of their health by offering an accessible and private method for knowing their HIV status. This initiative is a critical component in achieving the UNAIDS 2030 targets, which are a global commitment to end the HIV/AIDS epidemic by 2030.")
        st.subheader('Our Mission')
        # st.subheader('Our Mission: Empowering You to Know Your Status')
        st.write("Our mission is to provide accessible and accurate information about HIV self-testing, HIV treatment, and living with HIV. We are dedicated to enabling individuals to make informed decisions about their health, contributing to the achievement of the 95-95-95 targets set by UNAIDS.")
        st.subheader("Why HIV Self-Testing Matters")
        # st.subheader("Why HIV Self-Testing is Essential")
        st.write("HIV self-testing is essential because it offers privacy, convenience, and reduces the stigma associated with HIV testing. By giving individuals the power to test themselves, we aim to increase the number of people who know their HIV status, leading to earlier diagnosis and improved access to treatment.")
        st.subheader("Our Commitment")
        # st.subheader('Our Commitment to Reliable Information')
        st.write("We are committed to providing accurate and up-to-date information on HIV self-testing, including guidance on how to perform self-tests, interpret results, and live positively with HIV. Our content is rooted in evidence-based practices and guidelines from global health organizations.")
        st.subheader("How We Can Achieve the Targets Together")
        # st.subheader('Working Together to Achieve the 95-95-95 Targets')
        st.write("Achieving the 95-95-95 targets is a collective effort. We believe that together, we can make a significant impact in the fight against HIV/AIDS. To contribute, explore our website to understand more about HIV, learn how to self-test, interpret results, and find valuable resources for living with HIV.")

    elif choice == "What to Know":
        st.title("What You Need to Know About HIV")
        st.write('--------------------------------')
        # st.subheader("Understanding HIV")
        st.video("https://youtu.be/12vTnXekJu8", format="video/mp4", start_time=0)
        st.write("--------------------------------")
        st.subheader("How it Spreads")
        st.markdown("""
        - Unprotected sexual intercourse with an infected person. 
        - Sharing needles or syringes with someone who has HIV. 
        - Receiving contaminated blood products or organ transplants. 
        - From mother to child during childbirth or breastfeeding.""")
        st.subheader('Early Detection is Important')
        st.write("Getting tested for HIV is crucial because early diagnosis can lead to better health. Regular testing is especially important if you engage in risky behaviors.")
        st.subheader("It is Treatable")
        st.write("Having HIV doesn't mean you can't live a long and healthy life. Medications called antiretroviral therapy (ART) can control the virus.")
        st.subheader("Prevention Matters")

        st.write("Use condoms for safe sex, avoid sharing needles if you use drugs, and consider PrEP if you're at high risk.")

    elif choice == "Why Test":
        st.title("Why Test for HIV?")
        st.write("--------------------------------")
        # st.subheader("Understanding HIV")
        st.video("https://youtu.be/uScEAA9LlZw", format="video/mp4", start_time=0)
        st.write("--------------------------------")
        st.subheader("Early Detection and Treatment")
        st.write("Early detection of HIV is crucial because it allows for early medical intervention. Starting treatment as soon as possible can slow down the progression of the virus and prevent health complications.")
        st.subheader("Protecting Your Health")
        st.write("Knowing your HIV status is key to protecting your health. It helps you make informed decisions about your lifestyle and sexual activity.")
        st.subheader("Reducing the Spread of HIV")
        st.write("By getting tested and knowing your status, you play a part in reducing the spread of HIV in your community and globally. Those who are aware of their positive status can take steps to prevent transmission.")
        st.subheader("Access to Treatment and Support")
        st.write("Testing positive for HIV provides access to treatment, including antiretroviral therapy (ART), which can significantly improve your health and quality of life. It also opens doors to support and resources for those living with HIV.")
        st.subheader("Empowerment")
        st.write("Knowing your HIV status is empowering. It allows you to take control of your health and make informed choices regarding your well-being.")


    elif choice == "Before you Test":
        st.title("Pre-testing Counseling")
        st.write("--------------------------------")
        # st.subheader("Understanding HIV")
        st.video("https://youtu.be/kwHdheVwFkI", format="video/mp4", start_time=0)
        st.write("--------------------------------")
        st.subheader("Emotional Preparedness")
        st.write(
            "Testing for HIV can be an emotional experience. It's natural to feel anxiety, fear, or uncertainty. If you have any concerns, doubts, or questions, now is the time to share them. This is a safe space, and we're here to provide guidance and support.")
        st.subheader("Remember: You Are Not Alone")
        st.write(
            "Regardless of the test result, remember that you are not alone. Support is available, whether it's through medical care, counseling, or support groups. Reach out if you need assistance, and remember that living a healthy and fulfilling life with HIV is possible.")
        st.subheader("In Closing")
        st.write(
            "This pretesting counseling session is designed to ensure that you are informed, emotionally prepared, and ready to take your HIV self-test. If you have any questions or concerns, please don't hesitate to ask. Your health is important, and you're taking a positive step toward knowing your status and taking control of your well-being. We're here to support you every step of the way.")

    elif choice == "How to Test":
        st.header("How to Test: Conducting an HIV Self-Test")
        st.write("--------------------------------")
        # st.subheader("Understanding HIV")
        st.write("Welcome to the step-by-step guide on conducting an HIV self-test. This page will walk you through the process, ensuring you have the information you need to perform the test accurately and confidently")
        st.write("--------------------------------")
        st.video("https://youtu.be/78CjkrSFM2E", format="video/mp4", start_time=0)
        st.write("--------------------------------")
        st.subheader("Record Your Result")
        st.write(
            "It's essential to document your result as instructed in your test kit. This record can be important for future reference or medical consultations.")

        #Data for the database
        st.radio('What is your sex?',['Male', 'Female'])
        st.number_input('How old are you?', min_value=8, step=1)
        st.radio("What is your results?", ['Negative', 'Positive'])


        st.button("Submit Results")

    elif choice == "What your results mean":
        st.title("Understanding Your HIV Test Result")
        st.write("--------------------------------")
        st.subheader("Positive Results")

        st.write(""" A reactive result with this test does not mean you are infected with HIV, however an additional test should be carried out in a clinic to confirm your result. We can help you find a clinic suitable for your needs.

If you test positive for HIV at the clinic, you’ll be given a prescription for antiretroviral medication. You can read more about this medication here.

If you test positive for HIV after confirmation, you should consider telling your current partners and anyone else that you have had sex with in the last 3 months to get tested too. We can support you with that.

It is important to note that people who have self tested should not be forced or coerced to disclose the results of their test to anyone. They should only do so on a voluntary basis.""")
        st.write("--------------------------------")
        st.subheader("Negative Results")
        st.write(""" A non-reactive result means the test did not detect a response by your immune system to the HIV infection. If you think you’ve been exposed to HIV in the last 3 months you should test again in 3 months time to confirm that you are not infected with HIV. Exposure can happen through unprotected sex. Not everyone who is HIV positive knows their status.

We recommend that you test regularly for HIV. You can speak to our friendly clinical team to find out how often, and to set up reminders to test.

Some people who are at risk of catching HIV choose to take a medication called PrEP (pre-exposure prophylaxis). This is a tablet which has few side effects and is highly effective at preventing HIV infection. We can help you find a clinic suitable for your needs."""
            )

    elif choice == "After the Test":
        st.header("After the Test: Your Next Steps")
        st.write("--------------------------------")
        # st.subheader("Understanding HIV")
        st.write("Once you have completed your HIV self-test and received your result, it's important to understand what to do next. This page will provide guidance on the steps you should take based on your test result.")
        st.write("--------------------------------")
        st.video("https://youtu.be/XDmGcFIIH-Q", format="video/mp4", start_time=0)
        st.write("--------------------------------")

    elif choice == "Living with HIV":
        st.header("Living with HIV: A Healthy and Fulfilling Life")
        st.write("--------------------------------")
        # st.subheader("Understanding HIV")
        st.write("Receiving an HIV-positive diagnosis can be challenging, but it's important to understand that living with HIV is manageable, and many individuals lead healthy and fulfilling lives. This page is dedicated to providing you with information, resources, and guidance to help you navigate life with HIV.")
        st.write("--------------------------------")
        st.video("https://youtu.be/604tb9pehxE", format="video/mp4", start_time=0)
        st.write("--------------------------------")
        st.subheader("Starting Treatment")
        st.write("If you have tested positive for HIV, starting antiretroviral therapy (ART) is a crucial step. ART helps control the virus, reduce its impact on your immune system, and keep you healthy.")
        st.write("--------------------------------")
        st.subheader("Medical Care")
        st.write("Regular medical check-ups are essential for managing HIV. Your healthcare provider will monitor your health, adjust your treatment as needed, and help you navigate any side effects or concerns.")

        st.write("--------------------------------")
        st.subheader("Living Healthy")
        st.write("A healthy lifestyle can significantly impact your well-being. Eat a balanced diet, get regular exercise, and avoid smoking and excessive alcohol use.")
        st.write("--------------------------------")
        st.subheader("Medication Adherence")
        st.write("Taking your HIV medication as prescribed is crucial for maintaining viral suppression. Set reminders and establish a routine to ensure you don't miss a dose.")

        st.write("--------------------------------")
        st.subheader("Preventing Transmission")
        st.write("While living with HIV, it's essential to take precautions to prevent transmission to others. Practicing safe sex and using condoms is important.")

    elif choice == "Resources":
        st.header("Resources: Additional Support and Information")
        st.write("--------------------------------")
        # st.subheader("Understanding HIV")
        st.write("This  page is a valuable directory of external sources, organizations, and materials dedicated to HIV awareness, education, support, and advocacy. We've curated a list of resources to help you find additional information, connect with support networks, and stay informed about HIV-related topics.")
        st.write("--------------------------------")
        st.markdown("Visit the Ghana AIDS Commission for Self Test for information: https://ghanaids.gov.gh/")
        st.markdown("You can visit Self Test for information: https://self-test.hiv/")


        st.write("--------------------------------")

        ### This will also be fed into a seperate database
        st.header('Feedback')
        st.radio("How was your overall experience with the self-testing kit?",['Positive', 'Negative'])
        st.radio("Did you encounter any issues with the test kit?", ['No', 'Yes'])
        st.text_input('If yes, tell us about it')
        st.text_input('How can the HIV self-testing process be improved for users like you?')
        if st.button('Submit'):
            st.success('Your results have been submitted successfully')



if __name__ == '__main__':
    main()
