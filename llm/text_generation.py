# app/llm/gpt-recommendation.py
import logging
from . import client

class TextGeneration:

    prompt_user = """
    Daun jagung terdeteksi memiliki disease {}. Tugas anda adalah membuat {} untuk konteks disease ini. 
    Maksimal teks yang anda buat adalah 2 paragraf dan setiap paragraf berisi maksimal 5 kalimat.
    """

    prompt_system = "Kamu adalah seorang ahli dalam botani, khususnya tanaman jagung."


    def generate_text(self, disease, section):
        try:

            # prompt = self.prompt_user.format(disease, section)
            #
            # completion = client.chat.completions.create(
            #     model="gpt-3.5-turbo",
            #     messages=[
            #         {"role": "system", "content": self.prompt_system},
            #         {"role": "user", "content": prompt}
            #     ],
            #     max_tokens=154,
            # )

            # response_text = completion['choices'][0]['message']['content']
            return f"Testing Text Generation module {disease}, {section}"
        except Exception as e:
            logging.info(e)
