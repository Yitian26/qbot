from openai import OpenAI

class gptApi:
    def __init__(self,api_key:str,base_url:str,model:str,stream:bool=False):
        self.client = OpenAI(api_key=api_key,base_url=base_url)
        self.model = model
        self.stream = stream

    def send_request(self,prompt:str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt},
            ],
            stream=self.stream
        )
        if self.stream:
            resp = ""
            for chunk in response:
                resp += chunk.choices[0].delta.content
            return resp
        else:
            return response.choices[0].message.content
