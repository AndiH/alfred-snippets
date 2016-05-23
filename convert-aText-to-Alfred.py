#!/usr/bin/env python3
import click
import csv
import uuid
import json
import tempfile, os
import zipfile


def read_csv(filename):
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        mylist = list(reader)
    return mylist


def genUuid():
    return str(uuid.uuid4())


def aTextToAlfred(csvEntries):
    alfredEntries = []
    for entry in csvEntries:
        tempdict = dict()
        tempdict["snippet"] = entry[1]
        tempdict["uid"] = genUuid()
        tempdict["name"] = entry[2] if entry[2] is not "" else entry[0][1:]
        tempdict["keyword"] = entry[0]
        snippet = {"alfredsnippet": tempdict}
        alfredEntries.append(snippet)
    return alfredEntries

def saveJson(entry):
    filename = entry["alfredsnippet"]["name"] + " " + entry["alfredsnippet"]["uid"] + ".json"
    with open(filename, "w") as outfile:
        json.dump(entry, outfile)
    return outfile.name


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def main(filename):
    """Convert aText snippets to Alfred Snippets (2016 by A. Herten)

    Small tool which reads aText-exported .csv files of snippet collections and generates an Alfred (3.0) snippet collection.

    The script will work in a temporary directory and move the resulting .alfredsnippets file back to the directory it is invoked from.

    If a label for a snippet is not given in aText the keyword is taken as the Alfred snippet name (without the first character).

    """
    csvEntries = read_csv(filename)
    alfredEntries = aTextToAlfred(csvEntries)
    currentDir = os.getcwd()
    with tempfile.TemporaryDirectory() as tmpDir:
        os.chdir(tmpDir)
        fileList = []
        for entry in alfredEntries:
            fileList.append(saveJson(entry))
        outputFilename = filename[:-4] + ".alfredsnippets"
        with zipfile.ZipFile(outputFilename, "w", zipfile.ZIP_DEFLATED) as zf:
            for entry in fileList:
                zf.write(entry)
            zf.close()
        os.rename(outputFilename, os.path.join(currentDir, outputFilename))

if __name__ == '__main__':
    main()
