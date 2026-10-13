from app.schema.device import Device 
from openai import OpenAI 
import json 
import os 
from dotenv import load_dotenv
from app.prompts.templates import system_prompt , user_prompt
from pydantic import ValidationError
from fastapi import HTTPException



load_dotenv('/Volumes/Secondary/Generative-AI/mobile-device-assistant/.env')


OPEN_AI_KEY = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('MODEL_NAME')

client = OpenAI(api_key = OPEN_AI_KEY )

rejected_phrases = [
    "ignore previous",
    "system prompt",
    "you are "
]


def extract_device(text: str) -> Device: 
    user_input = user_prompt(text) 

    text_lower = text.lower() 

    for phrase in rejected_phrases:  
        if phrase in text_lower :
            raise HTTPException(status_code = 400 , detail = " Rejected input detected  ")

        


    messages = [
            {
                "role" : 'system', 
                "content" : system_prompt 
            },
            {
                "role" : 'user' , 
                "content" : user_input
            }
        ]

    

    for attempt in range(3) : 



        response = client.chat.completions.create(
        model = MODEL , 

        messages = messages , 
        response_format={"type": "json_object"}

        )

        data = response.choices[0].message.content
        data = json.loads(data)

        print("ATTEMPT:", attempt + 1)
        print("DATA:", data)

        try : 
            device = Device.model_validate(data)
            return device 

        except ValidationError as v : 

            print(f"---------------------------------ERROR AS {v}")
            if attempt == 2 : 
                
                raise HTTPException(status_code = 400 , detail = " Missing INFORMATION ")

                
            messages.append(
                {
                "role" : "assistant" , 
                "content" : json.dumps(data)
                })

            messages.append(
                {
                    "role" : "user" , 
                    "content" : f""" 
                    your previous response failed validation 
                    validation error {v}
                    correct the previous response to match the required schema 
                    """
                }
            )

        


    

  


