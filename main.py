import os
import shutil
import instelingen_voor_siem_deleter_3000 as IVSD_3000
class CLI:
    def mainmenu():
        print("1:verwijder renderring files")
        global menu
        menu = str(input("maak een keuzen "))
    def kies_pad(auto):
        global pad
        pad = input("wat is je pad (doe niks voor auto) ")
        if pad == "":
            pad = auto
        tool.make_paths(pad)
class tool:
    def get_files(pad):
        return os.listdir(pad)
    def delete(pad):
        shutil.rmtree(pad)
    def make_paths(pad):
        global PD
        global HQM
        global TM
        PD = pad + "/Peaks Data"
        HQM = pad + "/High Quality Media"
        TM  = pad + "/Thumbnail Media"

CLI.mainmenu()
pad_naar_event = IVSD_3000.pad + IVSD_3000.folder + IVSD_3000.bundelSoort + "/" + IVSD_3000.event
print(menu)
if menu == str(1):
    CLI.kies_pad(IVSD_3000.pad + IVSD_3000.folder + IVSD_3000.bundelSoort + "/" + IVSD_3000.event +"/Render Files")
    tool.delete(PD)
    tool.delete(HQM)
    tool.delete(TM)