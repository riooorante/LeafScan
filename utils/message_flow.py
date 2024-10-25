import multiprocessing
from llm.text_generation import TextGeneration
from utils.create_message import Message

class Flow:
    def __init__(self):
        self.message = Message()
        self.lock = multiprocessing.Lock()  
    def create_content(self, disease: str, section: str):
        text_generation = TextGeneration()

        try:
            content = text_generation.generate_text(disease, section)

            with self.lock:
                if disease not in self.message.get_message()["disease"].keys():
                    self.message.add_disease(disease)
                self.message.add_section(disease, section, content)

            return True 
        except Exception as e:
            with self.lock:
                self.message.set_status_code(500)
            return False  

    def _process_prediction(self, prediction, sections):
        for section in sections:
            if not self.create_content(prediction, section):
                return False
        return True

    def result_flow(self, predictions: list):
        sections = ["Penjelasan Dasar"]

        try:
            with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
                results = pool.starmap(self._process_prediction, [(prediction, sections) for prediction in predictions])

            if all(results):
                self.message.set_status_code(200)  
            else:
                self.message.set_status_code(500) 

        except Exception as e:
            self.message.set_status_code(500)

        return self.message.get_message()
