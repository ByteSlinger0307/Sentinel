from modules.llm._groq import Groq, LLAMA_31_70B_VERSATILE, LLAMA_32_11B_VISION_PREVIEW, Role
from rich import print

llm = Groq(LLAMA_32_11B_VISION_PREVIEW)


llm.addMessage(
    role=Role.user,
    content="My home name is Sonal"
)

print(f"{llm.messages = }")

print(llm.run("What is my home name?"))

print(f"{llm.messages = }")
