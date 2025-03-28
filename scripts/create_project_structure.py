import os

folders = [
    "src",
    "src/api",
    "src/api/v1",
    "src/database",
    "src/database/postgres",
    "src/models",
    "src/schemas",
    "src/utils",
    "config",
    "tests",
    "tests/api",
    "tests/api/v1",
    "tests/database",
    "tests/database/postgres",
    "tests/models",
    "tests/schemas",
    "tests/utils",
]

files = [
    "src/__init__.py",
    "src/main.py",
    "src/api/__init__.py",
    "src/api/dependencies.py",
    "src/api/v1/__init__.py",
    "src/api/v1/quiz_router.py",
    
    "src/database/__init__.py",
    "src/database/dependencies.py",
    "src/database/postgres/__init__.py",
    "src/database/postgres/core.py",
    "src/database/postgres/handler.py",
    "src/models/__init__.py",
    "src/models/quiz_models.py",
    "src/schemas/__init__.py",
    "src/schemas/quiz_schemas.py",
    "src/utils/__init__.py",
    "src/utils/exceptions.py",
    "config/__init__.py",
    "config/base.py",
    "tests/__init__.py",
    "tests/conftest.py",
    "tests/api/__init__.py",
    "tests/api/v1/__init__.py",
    "tests/api/v1/test_quiz_router.py",
    "tests/database/__init__.py",
    "tests/database/postgres/__init__.py",
    "tests/database/postgres/test_core.py",
    "tests/database/postgres/test_handler.py",
    "tests/models/__init__.py",
    "tests/models/test_quiz_models.py",
    "tests/schemas/__init__.py",
    "tests/schemas/test_quiz_schemas.py",
    "tests/utils/__init__.py",
    "tests/utils/test_exceptions.py",
    
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, 'w') as f:
        pass  # Create empty files