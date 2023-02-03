import yaml

def loadConfigDict(configName: list, basePath):
    """
    Generic function to load and open yaml config files
    :param configNames: Tuple containing names of config files to be loaded
    :return: Dictionary with opened yaml config files
    """
    configPath = basePath / 'config'
    configDict = {}
    filePath = (configPath / configName)
    with open(filePath) as ipf:
        configDict[configName] = yaml.load(ipf, Loader=yaml.SafeLoader)
    return configDict


def createFileString(fileName: str, filetypeStr: str):
    """
    Generic method used for fileString. This method does not write any files but just creates the file name including
    the filetype suffix.
    :param fileKey: Manual specification of fileKey
    :param filetypeStr: filetype to be written to hard disk
    :return: Full name of file to be written.
    """
    return f"{fileName}.{filetypeStr}"