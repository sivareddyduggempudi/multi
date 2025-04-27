from utils.llm_helper import ask_llm

def find_resources(company_name):
    prompt = f"""
    Find public datasets, GitHub projects, or Kaggle datasets relevant to the industry in which "{company_name}" operates.
    List at least 3-5 links with short titles.
    """
    response = ask_llm(prompt)
    resources = []
    lines = response.split("\n")
    for line in lines:
        if "-" in line and "http" in line:
            parts = line.split("http")
            title = parts[0].replace("-", "").strip()
            link = "http" + parts[1].strip()
            resources.append({"title": title, "link": link})
    return resources
