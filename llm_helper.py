import google.generativeai as genai
import os
import os
os.environ["GEMINI_API_KEY"] = "AIzaSyCEiu-m_wMRwP8eiFigrbx7oCeIp6f9lJ0"



genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_llm(prompt, model_name="models/gemini-2.0-pro-exp-02-05", temperature=0.3):
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            temperature=temperature,
            top_p=1.0,
            top_k=40,
            max_output_tokens=2048,
        ),
    )
    return response.text
