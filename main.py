import os
from crewai import Crew

from textwrap import dedent
from agents import HumanResourcesAgents
from tasks import ScootingTask

class ScootingCrew:
    def __init__(self, city, role, language):
        self.city = city
        self.role = role
        self.language = language

    def run(self):
        agents = HumanResourcesAgents()
        tasks = ScootingTask()

        # Create a Crew
        crew = Crew(
            agents=[
                agents.expert_scooting_agent(),
                agents.compagnies_selection_agent(),
                agents.job_search_agent()
            ],
            tasks=[
                tasks.search_companies(agents.expert_scooting_agent(), self.city, self.role, self.language),
                tasks.search_jobs(agents.compagnies_selection_agent(), self.city, self.role, self.language),
                tasks.search_internships(agents.job_search_agent(), self.city, self.role, self.language)
            ],
            verbose=True
        )
        result = crew.kickoff()
        return result


if __name__ == '__main__':
    print("Welcome to the Scooting Crew!")
    city = input("Enter the city you are looking for a job in: ")
    role = input("Enter the role you are looking for: ")
    language = input("Enter the language you are looking for: ")

    crew = ScootingCrew(city, role, language)
    result = crew.run()
