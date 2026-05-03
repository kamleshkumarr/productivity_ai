import os
import requests
from huggingface_hub import InferenceClient
from openai import OpenAI

API_URL = "https://api-inference.huggingface.co/models/MoritzLaurer/deberta-v3-large-zeroshot-v2.0"

headers = {
    "Authorization": f"Bearer {os.environ.get('HF_TOKEN')}"
}


def get_ai_priority(task_title, description=""):
    """
    AI-powered task priority using DeBERTa zero-shot model.
    Returns: High / Medium  / Low 
    """

    # 🧠 Strong prompt (important for accuracy)
    text = f"""
You are an expert productivity assistant.

Your job is to classify task urgency based on:
- deadline
- importance
- real-world impact

Task: {task_title}
Details: {description}

Decide urgency level carefully.
"""

    # 🏷️ Better semantic labels (VERY IMPORTANT)
    labels = [
        "extremely urgent task that must be done immediately",
        "important task that should be done soon",
        "low priority task that can be done later"
    ]

    payload = {
        "inputs": text,
        "parameters": {
            "candidate_labels": labels
        }
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=20)
        result = response.json()

        # 🔴 Debug (keep during testing)
        print("HF RESPONSE:", result)

        # Handle API errors
        if isinstance(result, dict) and "error" in result:
            print("HF Error:", result["error"])
            return "Medium "

        if "labels" not in result or "scores" not in result:
            return "Medium "

        # 🧠 Get best prediction
        best_index = result["scores"].index(max(result["scores"]))
        best_label = result["labels"][best_index]

        # 🔄 Map to your app format
        mapping = {
            "extremely urgent task that must be done immediately": "High ",
            "important task that should be done soon": "Medium ",
            "low priority task that can be done later": "Low "
        }

        return mapping.get(best_label, "Medium")

    except Exception as e:
        print("AI Exception:", e)
        return "Medium "