def key(api):
    with open("Api.txt", "r") as file:
        lines = file.readlines()
    value = ""
    for line in lines:
        if line.startswith(api):
            value = line.split("=")[1].strip().strip('"')
    return value
