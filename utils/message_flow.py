import logging
import multiprocessing
from llm.text_generation import TextGeneration
from utils.create_message import Message

class Flow:
    def __init__(self):
        self.message = Message()
        self.text_generation = TextGeneration()

    def create_content(self, disease: str, section: str, lock: multiprocessing.Lock):
        try:
            # Menghasilkan teks menggunakan model LLM
            content = self.text_generation.generate_text(disease, section)

            with lock:
                # Menambahkan penyakit dan konten yang dihasilkan
                if disease not in self.message.get_message()["disease"].keys():
                    self.message.add_disease(disease)
                self.message.add_section(disease, section, content)

            return True
        except Exception as e:
            logging.error(f"Error while creating content for disease '{disease}': {e}", exc_info=True)
            with lock:
                self.message.set_status_code(500)
            return False

    def _process_prediction(self, prediction, sections):
        lock = multiprocessing.Lock()  # Create a new lock for each process
        for section in sections:
            if not self.create_content(prediction, section, lock):
                return False
        return True

    def result_flow(self, predictions: list):
        sections = ["Diagnosa"]

        try:
            with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
                # Menjalankan proses secara paralel
                results = pool.map(self._process_prediction, predictions)

            logging.info("Results from predictions: %s", results)

            if all(results):
                logging.info("All predictions processed successfully.")
                self.message.set_status_code(200)
            else:
                logging.warning("Some predictions failed.")
                self.message.set_status_code(500, "flow else")

        except Exception as e:
            logging.error("An error occurred in result_flow: %s", e, exc_info=True)
            self.message.set_status_code(500, "An error occurred in result_flow")

        return self.message.get_message()
