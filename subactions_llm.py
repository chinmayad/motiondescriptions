import openai

# Define your OpenAI GPT-3 API key.
api_key = "

# List of kinetic action classes.
kinetic_actions = [
    "abseiling"
    "squat",
    "sticking tongue out",
    "stomping grapes",
    "stretching arm",
    "stretching leg",
    "strumming guitar",
    "surfing crowd",
    "surfing water",
    "sweeping floor",
    "swimming backstroke",
    "swimming breast stroke",
    "swimming butterfly stroke",
    "swing dancing",
    "swinging legs",
    "swinging on something",
    "sword fighting",
    "tai chi",
    "taking a shower",
    "tango dancing",
    # Add more actions as needed
]

def generate_subactions(action):
    prompt = f"Make the bed steps are :   put the sheet on the bed ,insert the quilt into the quilt cover ,put the quilt on the bed , insert the pillow into the pillow cover , put the pillow on the bed.   Similarly, provide the steps of {action} that are visually seen. No need of explaining each step. "
    
   # generated_response = openai.Completion.create(
   ##     engine="davinci",
   #     prompt=prompt,
   #     max_tokens=50,
   # )
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",#gpt-3.5-turbo",
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )

    steps= response.choices[0].message["content"]
    generated_steps = generated_response.choices[0].text.strip()
    return generated_steps

def main():
    openai.api_key = api_key

    for action in kinetic_actions:
        generated_steps = generate_subactions(action)
        print(f"Steps for {action}:\n{generated_steps}\n")

if __name__ == "__main__":
    main()

