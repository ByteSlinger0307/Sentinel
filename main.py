from modules.llm._groq import Groq, LLAMA_31_70B_VERSATILE, LLAMA_32_11B_VISION_PREVIEW, Role
from rich import print

llm = Groq(LLAMA_32_11B_VISION_PREVIEW)

print(llm.run("hello"))