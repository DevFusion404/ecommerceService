"""
Config Loader - Loads application runtime settings from filesystem.
"""

def read_config_file(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except:
        return ""

if __name__ == "__main__":
    print("Config length:", len(read_config_file("settings.json")))
