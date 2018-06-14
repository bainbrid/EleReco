import ROOT as r

def plot(tree,varexp,selection,option) :
    tree.Draw(varexp,selection,option)
    htemp = r.gDirectory.Get("htemp")
    c = r.TCanvas()
    htemp.Draw()
    c.SaveAs("draw/"+htemp.GetTitle().replace("/",".ov.")+".pdf")

filenames = ["output_BToKee_Gsf0p5.root"]

t = None
if len(filenames) == 0 : 
    t = None
if len(filenames) == 1 : 
    f = r.TFile(filenames[0])
    t = f.Get("LowPtEleNtuplizer/tree")
else :
    t = r.TChain("LowPtEleNtuplizer/tree")
    for name in filenames : t.Add(name)

t.Print()

plot(t,"gsfEles_gsfTrk_Phi:gsfEles_gsfTrk_Eta>>htemp(64,-3.2,3.2,50,-5.,5.)","gsfEles_gsfTrk_Pt<2.","")

plot(t,"genEles_Pt[0]>>htemp(50,0.,10.)","genEles_N>0","")
plot(t,"genTrks_Pt[genEleLead_genTrks_Idx]>>htemp(80,0.,20.)","genEles_N>0","")

plot(t,"genEleLead_genTrks_N>>htemp(20,0.,20.)","genEles_N>0","")
plot(t,"genEleLead_genTrks_N:genEles_Pt>>htemp(20,0.,20.,22,-0.5,10.5)","","")

plot(t,"genEleLead_genTrks_N:genEles_Pt[0]>>htemp(50,0.,10.,20,0.,20.)","genEles_N>0","")
plot(t,"genEleLead_genTrks_DR:genEles_Pt[0]>>htemp(50,0.,10.,50,0.,0.5)","genEles_N>0","")
plot(t,"genEleLead_genTrks_PtRatio:genEles_Pt[0]>>htemp(50,0.,10.,40,0.,2.)","genEles_N>0","")

# 
plot(t,"genEleLead_genTrks_PtRatio>>htemp(40,0.,2.)","genEles_N>0","")
plot(t,"genEleLead_genTrks_DR>>htemp(60,0.,0.3)","genEles_N>0","")
plot(t,"genEleLead_genTrks_PtRatio:genEleLead_genTrks_DR>>htemp(60,0.,0.3,40,0.,2.)","genEles_N>0","")

# 
plot(t,"genEleLead_genTrks_PtRatio>>htemp(40,0.,2.)","genEles_N>0","")
plot(t,"genEleLead_genTrks_DR>>htemp(60,0.,0.3)","genEles_N>0","")
plot(t,"genEleLead_genTrks_PtRatio:genEleLead_genTrks_DR>>htemp(60,0.,0.3,40,0.,2.)","genEles_N>0","")

# 
plot(t,"genEleSub_genTrks_PtRatio>>htemp(40,0.,2.)","genEles_N>1","")
plot(t,"genEleSub_genTrks_DR>>htemp(60,0.,0.3)","genEles_N>1","")
plot(t,"genEleSub_genTrks_PtRatio:genEleLead_genTrks_DR>>htemp(60,0.,0.3,40,0.,2.)","genEles_N>1","")

#
plot(t,"genTrks_Pt[genEles_genTrks_Idx]/genEles_Pt:genEles_genTrks_DR>>htemp(60,0.,0.3,40,0.,2.)","genEles_N>0 && genEles_genTrks_Idx>=0","")




