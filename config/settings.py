"""
Cyber AI - Global Settings
"""

from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
KNOWLEDGE_DIR = BASE_DIR / "knowledge"
DATA_DIR = BASE_DIR / "data"
MEMORY_DIR = BASE_DIR / "memory"
MODEL_DIR = BASE_DIR / "model"
PROMPTS_DIR = BASE_DIR / "prompts"

# Permissions file
PERMISSIONS_FILE = BASE_DIR / "config" / "permissions.json"

# LLM settings (change according to your provider)
LLM_PROVIDER = "openai"          # openai | local | groq | anthropic
LLM_MODEL = "gpt-4o-mini"
LLM_TEMPERATURE = 0.2
MAX_TOKENS = 4096

# Agent settings
MAX_STEPS = 20                   # Maximum reasoning/execution steps per task
ASK_BEFORE_DANGEROUS = True

# RAG settings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
TOP_K_RESULTS = 5
CHUNK_SIZE = 512
CHUNK_OVERLAP = 50
