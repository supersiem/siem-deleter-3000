import os
import shutil
import instelingen_voor_siem_deleter_3000 as IVSD_3000
class CLI:
    def mainmenu():

        global menu
        menu = str(1)
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

tool.make_paths(IVSD_3000.auto.PAD)
try:
    tool.get_files(IVSD_3000.auto.PAD)
except:
    print("404")
    print("kon event niet vinden")
    exit()

try:
    if IVSD_3000.Peaks_Data:
        tool.delete(PD)
    if IVSD_3000.High_Quality_Media:
        tool.delete(HQM)
    if IVSD_3000.Thumbnail_Media:
        tool.delete(TM)
except:
    print("404")
    print("niks om weg te haalen")
    exit()


exit()