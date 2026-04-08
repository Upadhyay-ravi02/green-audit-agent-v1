import numpy as np
from models import BrowserGymObs, ActionResult

class SustainabilityEnv:
    def __init__(self, task_id="verify_offset"):
        self.task_id = task_id
        self.max_steps = 8
        self.reset()

    def reset(self):
        self.steps = 0
        self.done = False
        
        goal_text = {
            "verify_offset": "Find and click the 'Verify' button for Carbon Project #82.",
            "cross_reference": "Extract 'Net Carbon' value and fill it in the 'Audit_Value' box.",
            "anomaly_detection": "Check if Page A and Page B values match. Flag if they don't."
        }

        metadata = {
            "browsergym_obs": {
                "extra_element_properties": {
                    "82": {"clickable": True, "bbox": ["100", "200", "50", "20"]},
                    "input_audit": {"clickable": True, "bbox": ["300", "400", "100", "30"]}
                }
            }
        }

        obs = BrowserGymObs(
            goal=goal_text.get(self.task_id, "Complete Audit"),
            url="https://audit.eco-corp.internal/dashboard",
            screenshot=list(np.zeros(100).flatten()), 
            metadata=metadata
        )
        return ActionResult(observation=obs, reward=0.0, done=False)

    def step(self, action_obj):
        self.steps += 1
        # Extracting the string from the object passed by inference.py
        action = action_obj.action_str.lower() if hasattr(action_obj, 'action_str') else str(action_obj).lower()
        reward = 0.0
        
        # Simple Grader Logic
        if self.task_id == "verify_offset" and "click('82')" in action:
            reward = 1.0
            self.done = True
        elif self.task_id == "cross_reference" and "fill('input_audit'" in action:
            reward = 0.8
            self.done = True
            
        if self.steps >= self.max_steps:
            self.done = True

        obs = self.reset().observation
        return ActionResult(observation=obs, reward=reward, done=self.done)

    def close(self):
        pass