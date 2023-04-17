import yaml
import os
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# config parameters
telegram_token = os.getenv("telegram_token")
openai_api_key = os.getenv("openai_api_key")
use_chatgpt_api = os.getenv("use_chatgpt_api", True)
allowed_telegram_usernames = os.getenv("allowed_telegram_usernames")
new_dialog_timeout = os.getenv("new_dialog_timeout")
enable_message_streaming = os.getenv("enable_message_streaming", True)
mongodb_uri = os.getenv('MONGODB_URI')

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)
