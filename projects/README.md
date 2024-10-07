# Python/Pytest sub-projects

To organize your project into smaller sub-projects each with its own set of Python scripts and pytest configurations<br> you have to ensure that pytest works correctly for each sub-project without cross-contamination.<br>

Follow these guidelines:
- **Directory Structure**: Organize your project with a clear directory structure where each sub-project has its own directory.
- **Separate `pytest.ini` or `conftest.py`**: Each sub-project can have its own pytest.ini or conftest.py file to configure pytest independently.

```
projects/
│
├── sub_project_1/
│   ├── src/
│   │   └── script1.py
│   ├── tests/
│   │   ├── test_script1.py
│   │   └── conftest.py
│   └── pytest.ini
│
├── sub_project_2/
│   ├── src/
│   │   └── script2.py
│   ├── tests/
│   │   ├── test_script2.py
│   │   └── conftest.py
│   └── pytest.ini
│
└── README.md 
```

## Imports

The line `sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))` is used to modify the Python module search path (`sys.path`) to include the parent directory of the current script's directory.<br> 
This allows Python to find and import modules that are located in the parent directory or its subdirectories.<br>

Here's a breakdown of what each part of the line does:

1. `os.path.abspath(__file__)`:
    - `__file__` is a special variable that holds the path of the current script.
    - `os.path.abspath(__file__)` returns the absolute path of the current script.

2. `os.path.dirname(os.path.abspath(__file__))`:
    - `os.path.dirname(path)` returns the directory name of the given path.
    - `os.path.dirname(os.path.abspath(__file__))` returns the directory containing the current script.

3. `os.path.dirname(os.path.dirname(os.path.abspath(__file__))`):
    - This applies `os.path.dirname` again to get the parent directory of the directory containing the current script.

4. `sys.path.append(...)`:
    - `sys.path` is a list of strings that specifies the search path for modules.
    - `sys.path.append(path)` adds the specified path to the end of the module search path.

```
python-projects/
└── projects/
    └── project-template/
        ├── loggingSetup.py
        ├── src/
        │   ├── script1.py
        │   └── script2.py
```

`script2.py`
```Python
import sys
import os
import logging

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loggingSetup import setup_logging
from src import script1 as function
```
---
### There is one `project-template/` keep this empty so it is possible to copy and past it for new projects.
1. Check/change the logging paths.
2. Change the script run paths.