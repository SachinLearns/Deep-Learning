import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv() # To load the environment variables (here, GROQ_API_KEY) from the .env file

os.getenv('GROQ_API_KEY')

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, 
                            groq_api_key=os.getenv('GROQ_API_KEY'), 
                            model_name='llama-3.1-70b-versatile')
    
    def extract_job(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### WEBSITE CAREER PAGE TEXT:
            {page_data}

            ### INSTRUCTION:
            Extract all job postings from the provided text. Each job should have the following keys: 
            - 'role'
            - 'experience level'
            - 'skills'
            - 'description'

            Return the output as valid JSON without any additional text or preamble.

            ### REQUIRED JSON OUTPUT (NO EXTRAS):
            """ )
        chain_extract = prompt_extract | self.llm # This is the LangChain chain - you have a prompt and you are passing it to LLM
        response = chain_extract.invoke(input = {"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            response = json_parser.parse(response.content)
        except OutputParserException:
            raise OutputParserException("Content too big. Unable to parse the jobs.")
        return response if isinstance(response, list) else {response}
    
    def generate_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DETAILS:
            {job_description}

            ### INSTRUCTION:
            Write a professional cold email as Mohan, a business development executive at AtliQ, an AI & Software Consulting company. 
            AtliQ specializes in AI-driven solutions that optimize business processes, enhance scalability, reduce costs, and improve efficiency.

            Describe AtliQ’s expertise in fulfilling the client's requirements based on the job description. 
            Incorporate the most relevant links from the following portfolio to highlight AtliQ's success in similar projects: {link_list}.

            Keep the tone persuasive but professional. Do not include any preamble.

            ### EMAIL (NO EXTRAS):
        """
        )
        chain_email = prompt_email | self.llm
        response = chain_email.invoke(input = {"job_description": str(job), "link_list": links})
        return response.content
    

if __name__ == '__main__':
    print(os.getenv('GROQ_API_KEY'))
    
