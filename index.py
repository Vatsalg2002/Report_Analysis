"""

this is the main file that will be used to run the crewai
for the patient report analysis and provide the insights and recommendations to the patient

"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from crewai_tools import tool, SerperDevTool
from parse_report import extract_data_from_pdf


#getting the api keys from the environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")


# Ollama_openhermes = Ollama(model = "openhermes")


# define agents
report_reader = Agent(
    role="Report Reader",
    goal="Read the pdf of report and give the result in structured way in json format",
    backstory="You are an AI reader that take a pdf report and give the result in structured json format",
    verbose=True,
    allow_delegation=True,
    tools=[extract_data_from_pdf, SerperDevTool()],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
    # llm=Ollama_openhermes
)

# defining doctor that will provide the summary of the patient health conditions and possible diseases and health risks

doctor = Agent(
    role="doctor",
    goal="analyse the reports of the patient and provide a summary of the patient health conditions in a brief manner i.e how is his/her health and also telling the patient about the possible diseases and with possible health risks that must be understandable to patient in simple language",
    backstory="You are a expert doctor who have all over knowledge of the human body and can provide a summary of the patient health conditions and also provide possible diseases to the patients and with possible health risks",
    verbose=True,
    allow_delegation=False,
    tools=[SerperDevTool()],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
    # llm=Ollama_openhermes
)

# defining the recommendation writer that will provide the recommendations to the patient to cure the blood abnormalities and also provide the possible diseases that the patient may have and also provide the links to the articles that will help the patient to cure the disease in better way

recommendation_writer = Agent(
    role="Recommendation Writer",
    goal="tell the disease that the patient may have if any and provide brief heath recommendations to treat the blood abnormalities and  home remedies to treat it and possible reason for their abnomal values and also provide links to articles present on internet for the patient that will help them to cure the diseases in better way",
    backstory="You are a health expert who can give recommendation to the patients to cure the blood abnormalities with it possible reason and methods. remedies to cure them in a structured json format",
    verbose=True,
    allow_delegation=True,
    tools=[SerperDevTool()],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
    # llm=Ollama_openhermes
)

# creation of task for the agents

task1 = Task(
    description="Analyse the report of the patient and return result in structured json format",
    agent=report_reader,
    expected_output="json format of the report of patient",
)

task2 = Task(
    description="analyse the reports of the patient and provide thorough insights over it with possible heath diseases and health risks",
    agent=doctor,
    expected_output="a detailed insights of the patient's heath conditions and possible diseases in json format",
)

task3 = Task(
    description="write recommendations for the patient as per insights and also mention the possible disease to the patient if any and heath risks told by doctor and provide methods to cure them , some home remedies to cure them and also provide links to the artcles that will help the patient to cure the disease in better way",
    agent=recommendation_writer,
    expected_output="a detailed recommendation/overview to the patient regarding his/her disease (if any) and to cure the blood abnormalities/disease, with possible reasons for the abnormalities and relevant links to the patient that will help them to cure the disease in better way with some home remedies",
)

# instantiating the crew

crew = Crew(
    agents=[report_reader, doctor, recommendation_writer],
    tasks=[task1, task2, task3],
    # llm=Ollama_openhermes,
    version=2,
    process=Process.sequential,
)

# kickoff the crew

result = crew.kickoff()
print(result)
