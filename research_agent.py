from utils.llm_helper import ask_llm

def research_industry(company_name):
    prompt = f"""
    Conduct deep market research about the company "{company_name}".
    Find:
    - Industry and sector
    - Key offerings (products/services)
    - Strategic focus areas (supply chain, operations, customer experience)
    - Vision, mission, and goals (if available)
    Give a detailed but concise overview.
    """
    return ask_llm(prompt)
