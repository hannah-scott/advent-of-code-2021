import os

to_change = []

for file in os.listdir():
    if file[:3] == "day":
        to_change.append(file)

for file in to_change:
    splits = file.split(".")

    date = int(splits[0].split("-")[1])

    if date < 10:
        fname = "2021-12-0{}".format(date)
    else:
        fname = "2021-12-{}".format(date)
    
    if len(splits[0].split("-")) > 2:
        fname += "-" + splits[0].split("-")[-1]
    
    fname += "." + splits[-1]

    print(fname)

    with open(file, "r") as f:
        contents = f.read()

    if splits[-1] in ["py", "rkt"]:
        # Need to change .txt file name
        print(splits[0] + ".txt")
        print(contents.index(splits[0] + ".txt"))
        contents = contents.replace(splits[0] + ".txt", fname.split(".")[0] + ".txt")
    
    with open(fname, "w") as f:
        f.write(contents)