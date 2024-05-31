#! /usr/bin/python
import os

# Purpose: hadd files together automatically, either JetMET+ZB and/or
#           IOVs-in-parts. Update the list_of_lists below and set version.

version = 'v36_Summer23MG_L2L3Res_v1'
includeZB = True
doMC = False

# Merge files into a bigger one. First one is the target
IOV_list_of_lists = [
#    ['2022C_JME', '2022C_ZB', '2022C'],
#    ['2022D_JME', '2022D_ZB', '2022D'],
#    ['2022CD_JME', '2022C_JME','2022D_JME'],    
#    ['2022E_JME', '2022E_ZB', '2022E'], 
#    ['2022F_JME', '2022F_ZB', '2022F'],
#    ['2022G_JME', '2022G_ZB', '2022G'],
#    ['2022FG_JME', '2022F_JME','2022G_JME'],    
#    ['2023BCv123_JME', '2023BCv123_ZB', '2023BCv123'], 
    ['2023Cv123_JME', '2023Cv123_ZB', '2023Cv123'],
    ['2023Cv4_JME', '2023Cv4_ZB', '2023Cv4'],
    ['2023D_JME', '2023D_ZB', '2023D'],
#    ['Run3_JME', '2022C_JME','2022D_JME', '2022E_JME', '2022F_JME', '2022G_JME',
#     '2023BCv123_JME', '2023Cv4_JME','2023D_JME']
    ]

MC_list_of_lists = [
#    ['Run2P8','2016P8','2016APVP8','2017P8','2018P8'],
#    ['Run2QCD','2016QCD','2016QCDAPV','2017QCD','2018QCD'],
#    ['Summer22MG','Summer22MG1', 'Summer22MG2'],
#    ['Summer22EEMG','Summer22EEMG1', 'Summer22EEMG2','Summer22EEMG3', 'Summer22EEMG4'],
    ['Summer23MG', 'Summer23MG_1', 'Summer23MG_2', 'Summer23MG_3', 'Summer23MG_4'],
    ['Summer23MGBPix', 'Summer23MGBPix_1', 'Summer23MGBPix_2', 'Summer23MGBPix_3', 'Summer23MGBPix_4'],
    ]

if not includeZB:
    # Drop _ZB from the list
    for IOV_list in IOV_list_of_lists:
        for i in range(len(IOV_list)):
            if '_ZB' in IOV_list[i]:
                IOV_list.remove(IOV_list[i])
                break
            
# os.system("ls rootfiles/"+version+"/jmenano_data_out_*_"+version+".root")
for IOV_list in IOV_list_of_lists:
    command = "hadd -f "
    for iov in IOV_list:
        command = command + "rootfiles/"+version+"/jmenano_data_out_"+iov+"_"+version+".root "
    print("\""+command+"\"...")
    os.system(command)

if doMC:
    os.system("ls rootfiles/"+version+"/jmenano_mc_out_*_"+version+".root")
    for MC_list in MC_list_of_lists:
        command = "hadd "
        for mc in MC_list:
            command = command + "rootfiles/"+version+"/jmenano_mc_out_"+mc+"_v36_Summer23DT_NoL2L3Res.root "
        print("\""+command+"\"...")
        os.system(command)

#for iov in IOV_list:
#    print "Process GamHistFill.C for IOV "+iov
#    os.system("ls -ltrh files/GamHistosFill_mc_"+iov+".root")
#    os.system("ls -ltrh files/GamHistosFill_data_"+iov+".root")
#    os.system("ls -ltrh log_"+iov+"_"+version+".txt")
#    os.system("root -l -b -q 'mk_GamHistosFill.C(\""+iov+"\")' > log_"+iov+"_"+version+".txt &")
#    os.system("fs flush")
#    wait()
#    time.sleep(sleep_time)
