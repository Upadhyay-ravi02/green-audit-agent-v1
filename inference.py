import os
from openai import OpenAI
from env import SustainabilityEnv

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("HF_TOKEN")
MODEL_NAME = os.getenv("MODEL_NAME")

def main():
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    env = SustainabilityEnv(task_id="verify_offset")
    
    result = env.reset()
    print(f"Goal: {result.observation.goal}")

    for step in range(1, 6):
        prompt = f"Goal: {result.observation.goal}. Choose action: click('82') or fill('input_audit', 'value'). Reply with ONLY action."
        
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20
        )
        
        action_str = completion.choices[0].message.content.strip()
        print(f"Step {step}: AI Decision -> {action_str}")
        
        # Create a simple object to match the env.step requirement
        class ActionObj: pass
        action_obj = ActionObj()
        action_obj.action_str = action_str
        
        result = env.step(action_obj)
        print(f"Reward: {result.reward} | Done: {result.done}")
        
        if result.done:
            break

if __name__ == "__main__":
    main()