from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
# You can replace this embedding with your own as well.

speech = synthesiser(" I'm excited to see how AI will change the way we learn. AI can help personalize learning, automate grading, and even provide real-time feedback. But what about the human touch? Will we lose the joy of learning from a teacher, or the camaraderie of a classroom? I think AI can augment, not replace, the human element. By providing personalized learning experiences, AI can help teachers focus on what matters most – building relationships, fostering creativity, and inspiring students to reach their full potential.  I'm excited to see how AI will change the way we work. AI can help automate routine tasks, improve productivity, and even enable remote work. But what about the human side of work? Will we lose the sense of purpose and fulfillment that comes from working with others", forward_params={"speaker_embeddings": speaker_embedding})

sf.write("speech.wav", speech["audio"], samplerate=speech["sampling_rate"])
