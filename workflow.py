# Python
# Libraries (NumPy, Pandas)
# AI Frameworks (LangChain)
# LLM APIs
# Vector Database


# User → FastAPI → Embeddings → Vector DB → LLM → Response

# ---------------------------------------------------

# Create the environment folder
# python -m venv .venv

# # Activate it (Windows)
# .venv\Scripts\activate


# Install packages (like npm install <name>)
# pip install requests python-dotenv

# Save to list (like updating package.json)
# pip freeze > requirements.txt

# Install from existing list (like npm install)
# pip install -r requirements.txt


# my_project/
# ├── .venv/              # Ignored by Git
# ├── .env                # Ignored by Git (Secrets)
# ├── .env.example        # Committed (Templates)
# ├── requirements.txt    # Committed (Dependency List)
# └── main.py             # Your code


# Pro-tip: If you use VS Code, make sure you select the interpreter located at ./.venv/bin/python (Mac) or ./.venv/Scripts/python.exe (Windows) so your IntelliSense works correctly.