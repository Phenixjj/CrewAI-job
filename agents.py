from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from tools.search_tools import SearchTools

load_dotenv()

llm = ChatOpenAI(
    model="crewai-llama2",
    base_url="http://localhost:11434/v1"
)


class HumanResourcesAgents:

    def expert_scooting_agent(self) -> Agent:
        return Agent(
            role="Expert Human Resources Scooting Agent",
            # backstory for the agent specialist in tech companies
            backstory=dedent(
                """
                I am an expert in human resources for tech companies. I have been working in the tech industry for over 10 years.
                I have experience in recruiting, onboarding, and managing employees in tech companies. I have worked with companies of all sizes, from startups to large corporations.
                I have a deep understanding of the tech industry and the unique challenges that tech companies face when it comes to human resources.
                """
            ),
            # goal of the agent
            goal=dedent(
                """
                My goal is to help tech companies recruit and retain top talent. I can provide advice on recruiting strategies, onboarding processes, and employee management.
                I can help tech companies create a positive work environment that attracts and retains top talent.
                """
            ),
            # list of tools the agent has
            tools=[
                SearchTools.search_internet
            ],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

    def compagnies_selection_agent(self) -> Agent:
        return Agent(
            role="Compagnies Selection Agent",
            backstory=dedent(
                """
                I am an expert in selecting tech companies. I have been working in the tech industry for over 10 years.
                I have experience in evaluating tech companies based on various criteria, such as company culture, growth potential, and employee satisfaction.
                I have worked with companies of all sizes, from startups to large corporations.
                I have a deep understanding of the tech industry and the unique challenges that tech companies face.
                """
            ),
            goal=dedent(
                """
                My goal is to help job seekers find the best tech companies to work for. I can provide advice on how to evaluate tech companies based on various criteria, such as company culture, growth potential, and employee satisfaction.
                I can help job seekers make informed decisions about which tech companies to apply to and work for.
                """
            ),
            tools=[
                SearchTools.search_internet
            ],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )

    def job_search_agent(self) -> Agent:
        return Agent(
            role="Job Search Agent",
            backstory=dedent(
                """
                I am an expert in job search. I have been working in the tech industry for over 10 years.
                I have experience in helping job seekers find the best job opportunities in the tech industry.
                I have worked with job seekers of all levels, from entry-level to senior executives.
                I have a deep understanding of the tech industry and the unique challenges that job seekers face.
                """
            ),
            goal=dedent(
                """
                My goal is to help job seekers find the best job opportunities in the tech industry. I can provide advice on how to search for job opportunities, prepare for interviews, and negotiate job offers.
                I can help job seekers land their dream job in the tech industry.
                I am specialized in tech companies who accept internships roles.
                """
            ),
            tools=[
                SearchTools.search_internet
            ],
            allow_delegation=False,
            verbose=True,
            llm=llm,
        )