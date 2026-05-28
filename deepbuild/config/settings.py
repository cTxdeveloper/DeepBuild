from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / '.env')

class Settings:
    project_name: str = os.getenv('PROJECT_NAME', 'DeepBuild')
    log_level: str = os.getenv('LOG_LEVEL', 'INFO')
    sqlite_path: str = os.getenv('SQLITE_PATH', 'tasks.db')
    chroma_path: str = os.getenv('CHROMA_PATH', '.memory/chroma')
    default_model: str = os.getenv('DEFAULT_MODEL', 'gpt-4o-mini')

settings = Settings()
