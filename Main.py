from Packages import DeviceSpecs
from Packages import JSONParser
import pathlib
import getpass

RootFolder = pathlib.Path(__file__).parent
ConfigFile = JSONParser.parseConfigFile()  

def getArt(ArtName) -> str: # Returns the str of a file with the exact Name
    try:
        with open(f"{RootFolder}\\AsciiArt\\{ArtName}.txt", encoding="utf-8") as file:
            return file.read()
    except Exception as err:
        raise Exception(err)

def main():
    Specs = DeviceSpecs.Specs() # Get device specs
    SpecsSettings = ConfigFile.get("visiblespecs") # Get the settings for displaying specific specs.
    AsciiArt = ConfigFile.get("ascii") # Get the art to display

    print(getArt(AsciiArt))
    print(f"~ Fetch for {getpass.getuser()}@windows")
    print(f"╭{"―"*70}")

    for Key, Value in SpecsSettings.items():
        if Value is True:
            print(f"| {Key} : {Specs.__dict__[Key]}")

    print("╰")
    input()

if __name__ == "__main__":
    main()
