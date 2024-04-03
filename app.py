import os
from PIL import Image
import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger
from dotenv import load_dotenv; load_dotenv()

# Setup your config
st.set_page_config(
    page_title="Logo Generator",
    layout="centered",   
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png"
)

# Load and display the logo
image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Logo Generator by Lyzr")
st.markdown("### Welcome to the Logo Generator!")
st.markdown("Logo Generator app crafts personalized logos tailored to users' specifications.!!!")

# Custom function to style the app
def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# Content Campaign Generator

# replace this with your openai api key or create an environment variable for storing the key.
API_KEY = os.getenv('OPENAI_API_KEY')

 

open_ai_model_image = OpenAIModel(
    api_key=API_KEY,
    parameters={
        "n": 1,
        "model": "dall-e-3",
    },
)

def logo_generator(user_specification):
    
    graphic_designer = Agent(
        prompt_persona="""As a seasoned Graphic Designer specializing in logo creation for brands, your mission is to visually communicate the essence and identity of each client through compelling and memorable designs. Leveraging your expertise in color theory, typography, and visual storytelling, you'll craft logos that resonate with target audiences and effectively represent the values and personality of each brand. Your goal is to create visually stunning and versatile logos that leave a lasting impression, elevating the presence and credibility of the brands you collaborate with.""",
        role="Graphic Designer", 
    )

    logo_generator_image = Task(
        name="Logo Generation",
        agent=graphic_designer,
        output_type=OutputType.IMAGE,
        input_type=InputType.TEXT,
        model=open_ai_model_image,
        log_output=True,
        instructions="Generate an Image which is suitable to the given description. Capture every detail. Minimalistic style. [IMPORTANT!] Avoid any text or numbers in the image.",
        default_input=user_specification
    )

    logo_generator_image_innovative = Task(
        name="Logo Generation",
        agent=graphic_designer,
        output_type=OutputType.IMAGE,
        input_type=InputType.TEXT,
        model=open_ai_model_image,
        log_output=True,
        instructions="Create a fresh logo concept to the given description. Minimalistic style. [IMPORTANT!] Avoid any text or numbers in the image.",
        default_input=user_specification
    )

    logo_generator_image_sustainable = Task(
        name="Logo Generation",
        agent=graphic_designer,
        output_type=OutputType.IMAGE,
        input_type=InputType.TEXT,
        model=open_ai_model_image,
        log_output=True,
        instructions="Create a sustainable captivating logo to the given description. Minimalistic style. [IMPORTANT!] Avoid any text or numbers in the image.",
        default_input=user_specification
    )

    logo_generator_image_dynamic = Task(
        name="Logo Generation",
        agent=graphic_designer,
        output_type=OutputType.IMAGE,
        input_type=InputType.TEXT,
        model=open_ai_model_image,
        log_output=True,
        instructions="Craft a dynamic logo to the given description. Minimalistic style. [IMPORTANT!] Avoid any text or numbers in the image.",
        default_input=user_specification
    )

    logo_generator_image_luxury = Task(
        name="Logo Generation",
        agent=graphic_designer,
        output_type=OutputType.IMAGE,
        input_type=InputType.TEXT,
        model=open_ai_model_image,
        log_output=True,
        instructions="Craft a luxury standout logo to the given description. Minimalistic style. [IMPORTANT!] Avoid any text or numbers in the image.",
        default_input=user_specification
    )


    logger = Logger()
    

    main_output = LinearSyncPipeline(
        logger=logger,
        name="Logo Generator",
        completion_message="App Generated logo's!",
        tasks=[
            logo_generator_image,
            logo_generator_image_innovative,
            logo_generator_image_sustainable,
            logo_generator_image_dynamic,
            logo_generator_image_luxury
        ],
    ).run()

    return main_output


if __name__ == "__main__":
    style_app() 
    user_input = st.text_area("What kind of Business do you have?, Write about logo!")

    button=st.button('Submit')
    if (button==True):
        generated_output = logo_generator(user_specification=user_input)
        image_file_name = generated_output[0]['task_output'].local_file_path
        st.header("Logo's for your Business")
        st.image(image_file_name, caption='Logo Generator - Lyzr')
        st.markdown('---')

        st.subheader('Innovative Logo')
        second_image_file_name = generated_output[1]['task_output'].local_file_path
        st.image(second_image_file_name, caption='Logo Generator - Lyzr')
        st.markdown('---')

        st.subheader('Sustainable Logo')
        third_image_file_name = generated_output[2]['task_output'].local_file_path
        st.image(third_image_file_name, caption='Logo Generator - Lyzr')
        st.markdown('---')

        st.subheader('Dynamic Logo')
        fourth_image_file_name = generated_output[3]['task_output'].local_file_path
        st.image(fourth_image_file_name, caption='Logo Generator - Lyzr')
        st.markdown('---')

        st.subheader('Luxury Logo')
        fifth_image_file_name = generated_output[4]['task_output'].local_file_path
        st.image(fifth_image_file_name, caption='Logo Generator - Lyzr')
        st.markdown('---')

   
    with st.expander("ℹ️ - About this App"):
        st.markdown("""
        This app uses Lyzr Automata Agent to generate logo on the basis of user sepecification. For any inquiries or issues, please contact Lyzr.
        
        """)
        st.link_button("Lyzr", url='https://www.lyzr.ai/', use_container_width = True)
        st.link_button("Book a Demo", url='https://www.lyzr.ai/book-demo/', use_container_width = True)
        st.link_button("Discord", url='https://discord.gg/nm7zSyEFA2', use_container_width = True)
        st.link_button("Slack", url='https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw', use_container_width = True)