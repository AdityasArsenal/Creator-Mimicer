from huggingface_hub import InferenceClient
from huggingface_hub import login
from huggingface_hub import InferenceClient
import json
from _aud_to_text import get_raw_discription_text

login(token="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")

row_dis = get_raw_discription_text()
print(type(row_dis))
prompt = "mimic his style and write a description about ai revolution"
