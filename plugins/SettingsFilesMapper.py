# This is super heavily based off https://github.com/LostDragonist/MO2-Plugins/blob/master/src/GameRedirector/GameRedirector.py by LostDragonist.
# Just like that, this is MIT Licensed.

from pathlib import Path
import mobase

class SettingsFilesMapper(mobase.IPluginFileMapper):
  def __init__(self):
    super().__init__()
    self.__organizer = None

  def __tr(self, str_):
    return str_

  def init(self, organizer):
    self.__organizer = organizer
    return True

  def name(self):
    return "Settings Files Mapper"

  def author(self):
    return "OsmosisWrench"

  def description(self):
    return self.__tr("Redirects files from a mod folder called SettingsFilesMapper, to the users \"\\Documents\\My Games\\Skyrim Special Edition\" folder via the VFS.")

  def version(self):
    return mobase.VersionInfo(1, 0, 0, 0)
  
  def settings(self):
    return []

  def enabledByDefault(self):
    return True

  def mappings(self):
    modsPath = Path(self.__organizer.modsPath())
    m = mobase.Mapping()
    m.source = modsPath.joinpath("SettingsFilesMapper").as_posix()
    m.destination = Path(self.__organizer.managedGame().documentsDirectory().absolutePath()).as_posix()
    m.isDirectory = True
    m.createTarget = True
    return [m]

def createPlugin():
  return SettingsFilesMapper()