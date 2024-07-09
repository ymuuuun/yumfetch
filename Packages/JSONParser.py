import json
import pathlib

RootFolder = pathlib.Path(__file__).parent.parent

def parseConfigFile() -> dict:
    try:
        with open(f"{RootFolder}\\Config.json") as file:
            Parsed = json.loads(file.read())
            return Parsed
    except Exception as err:
        raise Exception(err)
