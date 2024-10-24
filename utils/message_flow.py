from llm import create_text
from utils.create_message import Message

message = Message()

def message_flow(prediction: list):
    sections = [""]

    for disiase in prediction:
        message.add_disiase(disiase)
        for section in sections:

            content = create_text(disiase, section)

            message.add_section(disiase, section, content)

    message.to_json()

    return message.get_message()






