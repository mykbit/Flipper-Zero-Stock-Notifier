import os;

# Define a list of required libraries
required_libraries = ['requests', 'plyer', 'pyobjus']

# Check if the required libraries are installed
missing_libraries = []
for lib in required_libraries:
    try:
        __import__(lib)
    except ImportError:
        missing_libraries.append(lib)

# Install missing libraries
if missing_libraries:
    print("The following libraries are missing:", missing_libraries)
    print("Installing missing libraries...")
    command = 'pip install ' + ' '.join(missing_libraries)
    os.system(command)
    print("Missing libraries installed.")
