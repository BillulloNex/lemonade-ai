# pip install transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
class JinaReader:
    def __init__(self, checkpoint="jinaai/reader-lm-0.5b", device="cpu"):
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(checkpoint)
        self.model = AutoModelForCausalLM.from_pretrained(checkpoint).to(device)

    def process_html(self, html_content, max_new_tokens=1024, temperature=0, 
                    do_sample=False, repetition_penalty=1.08):
        messages = [{"role": "user", "content": html_content}]
        input_text = self.tokenizer.apply_chat_template(messages, tokenize=False)
        
        inputs = self.tokenizer.encode(input_text, return_tensors="pt").to(self.device)
        outputs = self.model.generate(
            inputs, 
            max_new_tokens=max_new_tokens, 
            temperature=temperature, 
            do_sample=do_sample, 
            repetition_penalty=repetition_penalty
        )
        
        return self.tokenizer.decode(outputs[0])

# Example usage:
# reader = JinaReader()
# html_content = "<html><body><h1>Hello, world!</h1></body></html>"
# result = reader.process_html(html_content)
# print(result)
