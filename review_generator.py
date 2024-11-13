from huggingface_hub import InferenceClient
from huggingface_hub import login
from huggingface_hub import InferenceClient
import json

login(token="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")

def generate_costum_review(review,prompt):
    given_review = review
    given_prompt = f'{prompt}{given_review}'

    generator = InferenceClient(model='meta-llama/Llama-3.2-1B', timeout=120)

    generated_respo = generator.post(
        json={
            'inputs' : given_prompt,
            'parameters':{'max_new_tokens' : 100},
            'task' : 'text-generation'
        }
    )

    res = json.loads(generated_respo.decode())[0]["generated_text"]
    res = res[len(prompt):]
    res = res[len(review):]

    print("🟢🟢🟢🟢🟢🟢🟢")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print(f"{res}🟣🟣🟣🟣🟣")
    print("🔴🔴🔴🔴🔴🔴🔴")
    print("🔴🔴🔴🔴🔴🔴🔴")

    return res