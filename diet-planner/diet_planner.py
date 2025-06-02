import openai
import os
from utils import *

def create_meals(ingredients, kcal=2000):
    prompt = f''' Create a healthy meal plan for breakfast, lunch and dinner based on following ingredients {ingredients}.
    Explain each recepie.
    The total should be below {kcal}.
    Assign a suggestive and concise title to each meal.
    The meal should be in points.
    '''

    messages = [
        {'role':'system', 'content':'You are a talented cook.'},
        {'role':'user', 'content':prompt}
    ]
    response = openai.chat.completions.create(
        model ='gpt-4.1-nano',
        messages=messages,
        temperature =1,
        max_tokens=1000,
        n=1
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    openai.api_key = load_key()
    ingredients = 'Brocolli, Eggs, Milk, Vegetables'
    output = create_meals(ingredients)
    print(output)