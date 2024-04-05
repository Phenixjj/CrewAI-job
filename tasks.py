from crewai import Task
from textwrap import dedent


class ScootingTask:
    def __tip_section(self):
        return dedent(
            "If you do your BEST WORK, I'll give you a $10,000 commission!"
        )

    def search_companies(self, agent, city, role, language) -> Task:
        return Task(
            title="Search for Tech Companies",
            description=dedent(
                f"""
                **Task**: Search for tech companies in {city} hiring for {role} roles.
                **Description**: I need you to find tech companies in {city} that are hiring for {role} roles.
                Who have in the past accepted interns. And provide me with a list of companies that you think would be 
                a good fit for me because they are using this tech : {language}.
                Make sure to include the company name, website, and a brief description of the company with contact 
                as possible.

                **Parameters**:
                - City : {city}
                - Role: {role}
                - Language: {language}
            
                **Note**:{self.__tip_section()}
                """
            ),
            agent=agent,
        )

    def search_jobs(self, agent, city, role, language) -> Task:
        return Task(
            title="Search for Job Opportunities",
            description=dedent(
                f"""
                **Task**: Search for job opportunities in {city} for {role} roles.
                **Description**: I need you to find job opportunities in {city} for {role} roles.
                List the different job opportunities available in {city} for {role} roles using {language}.
                Make sure to include the company name, job title, and a brief description of the job with contact

                **Parameters**:
                - City : {city}
                - Role: {role}
            
                **Note**:{self.__tip_section()}
                """
            ),
            agent=agent,
        )

    def search_internships(self, agent, city, role, language) -> Task:
        return Task(
            title="Search for Internship Opportunities",
            description=dedent(
                f"""
                **Task**: Search for internship opportunities in {city} for {role} roles.
                **Description**: You need to find how to convince companies to accept interns in {city}.
                List the different internship opportunities available in {city} for {role} roles using {language}.
                Make sure to include the company name, job title, and a brief description of the job with contact
                

                **Parameters**:
                - City : {city}
                - Role: {role}
            
                **Note**:{self.__tip_section()}
                """
            ),
            agent=agent,
        )
