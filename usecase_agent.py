from utils.llm_helper import ask_llm

def generate_usecases(company_name, industry_info):
    prompt = f"""
    Based on the following industry and company information:
    
    {industry_info}
    
    Generate 5-7 relevant and innovative use cases where "{company_name}" can apply AI, ML, or GenAI.
    Focus on:
    - Operational efficiency
    - Supply chain optimization
    - Enhancing customer experience
    - Internal process automation
    Present use cases as a list.
    """
    response = ask_llm(prompt)
    return response.split("\n")
