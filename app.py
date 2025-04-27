import streamlit as st
from research_agent import research_industry
from usecase_agent import generate_usecases
from resource_agent import find_resources
from utils.llm_helper import ask_llm

def generate_final_report(company, industry_info, usecases, resources, bonus_solutions):
    report = f"# Market Research & AI Use Case Report for {company}\n\n"
    report += f"## Industry Research\n{industry_info}\n\n"
    report += "## Suggested AI/ML/GenAI Use Cases\n"
    for idx, uc in enumerate(usecases, 1):
        report += f"{idx}. {uc}\n"
    report += "\n## Resource Links\n"
    for res in resources:
        report += f"- [{res['title']}]({res['link']})\n"
    report += "\n## Bonus GenAI Solutions\n"
    for sol in bonus_solutions:
        report += f"- {sol}\n"
    return report

st.set_page_config(page_title="Market Research & AI Use Case Generator", layout="wide")

st.title("🔍 Market Research & AI Use Case Generator (Google Gemini)")
st.write("This tool uses Google Gemini to generate AI/GenAI use cases based on market research.")

company = st.text_input("Enter Company Name", placeholder="Example: Tesla, Amazon, Siemens")

if st.button("Generate Research & Use Cases"):
    if company:
        with st.spinner("Researching the Industry..."):
            industry_info = research_industry(company)
        
        with st.spinner("Generating Use Cases..."):
            usecases = generate_usecases(company, industry_info)

        with st.spinner("Finding Datasets and Resources..."):
            resources = find_resources(company)

        with st.spinner("Generating Bonus GenAI Solutions..."):
            bonus_prompt = f"Suggest 3-5 internal or customer-facing GenAI solutions (like document search, report generation, AI chatbots) for {company}."
            bonus_response = ask_llm(bonus_prompt)
            bonus_solutions = bonus_response.split("\n")

        st.success("Completed!")
        
        st.subheader("📚 Industry & Company Research")
        st.write(industry_info)

        st.subheader("🚀 Suggested AI/GenAI Use Cases")
        for idx, uc in enumerate(usecases, 1):
            st.write(f"{idx}. {uc}")

        st.subheader("📊 Resource Links")
        for res in resources:
            st.markdown(f"- [{res['title']}]({res['link']})")

        st.subheader("💡 Bonus GenAI Solutions")
        for sol in bonus_solutions:
            st.write(f"- {sol}")

        # Final Report
        final_report = generate_final_report(company, industry_info, usecases, resources, bonus_solutions)
        st.download_button("📥 Download Final Report", data=final_report, file_name=f"{company}_report.md", mime="text/markdown")

    else:
        st.warning("Please enter a company name.")
