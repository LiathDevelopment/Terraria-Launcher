from json import load

def get_versions():
    versions = []
    data = load(open("./launcher.json"))
    for version in data["versions"]:
        versions.append(version)

    return [entry for entry in reversed(versions)]

def launcher_version():
    data = load(open("./launcher.json"))
    return data["launcher_version"]