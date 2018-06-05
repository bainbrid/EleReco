# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = ['-b-']
lepton = ["electron","muon"][0]

if lepton == "muon" : 
    from files_RERECO import BToKmm_0p5GeV as files
    leptonid = 13
    nfiles = 15
elif lepton == "electron" :
    from files_RERECO import BToKee_0p5GeV as files 
    leptonid = 11
    nfiles = 500
import ROOT as r
r.gROOT.SetBatch(True)
sys.argv = oldargv
nevents = 10
write_histos = True

################################################################################

import math
def deltaPhi(p1,p2):
    '''Computes delta phi, handling periodic limit conditions.'''
    res = p1 - p2
    while res > math.pi:
        res -= 2*math.pi
    while res < -math.pi:
        res += 2*math.pi
    return res
def deltaR2(e1,p1,e2=None,p2=None):
    """Take either 4 arguments (eta,phi, eta,phi) or two objects that have 'eta', 'phi' methods)"""
    if (e2 == None and p2 == None):
        return deltaR2(e1.eta(),e1.phi(), p1.eta(), p1.phi())
    de = e1 - e2
    dp = deltaPhi(p1, p2)
    return de*de + dp*dp
def deltaR(*args):
    return math.sqrt( deltaR2(*args) )

################################################################################

print "Loading FWLite C++ libraries..."
r.gSystem.Load("libFWCoreFWLite.so")
r.gSystem.Load("libDataFormatsFWLite.so")
r.FWLiteEnabler.enable()

print "Loading FWlite python libraries..."
from DataFormats.FWLite import Handle, Events

print "Loading Events into memory..."
events = Events(files[:nfiles])
#events = Events("AODSIM.root")

print "Defining collections to inspect..."
genHandle, genLabel = Handle("std::vector<reco::GenParticle>"), "genParticles"
trkHandle, trkLabel = Handle("std::vector<reco::Track>"), "generalTracks"
gsfHandle, gsfLabel = Handle("std::vector<reco::GsfTrack>"), "electronGsfTracks"
nnNNseedHandle, seedLabel = Handle("std::vector<reco::ElectronSeed>"), "electronMergedSeeds"

eleHandle, eleLabel = None, None 
if lepton == "electron" :
    eleHandle, eleLabel = Handle("std::vector<reco::GsfElectron>"), "gedGsfElectrons"
elif lepton == "muon" :
    eleHandle, eleLabel = Handle("std::vector<reco::Muons>"), "recoMuons"

print "Creating histograms..."

h_genpart_n = r.TH1F("","",10,0.,10.)
h_gentrk_n = r.TH1F("","",10,0.,10.)
h_genele_n = r.TH1F("","",10,0.,10.)
h_genkaon_n = r.TH1F("","",10,0.,10.)
h_genpion_n = r.TH1F("","",10,0.,10.)
h_trk_n = r.TH1F("","",100,0.,2000.)
h_gsf_n = r.TH1F("","",10,0.,10.)
h_ele_n = r.TH1F("","",10,0.,10.)

h_genpart_pt = r.TH1F("","",100,0.,50.)
h_gentrk_pt = r.TH1F("","",100,0.,50.)
h_genele_pt = r.TH1F("","",100,0.,50.)
h_trk_pt = r.TH1F("","",100,0.,50.)
h_gsf_pt = r.TH1F("","",100,0.,50.)
h_ele_pt = r.TH1F("","",100,0.,50.)
h_trk_vs_gsf_pt = r.TH2F("","",40,0.,20.,40,0.,20.)

h_had_dr = r.TH1F("","",50,0.,5.) 
h_trk_dr = r.TH1F("","",50,0.,5.) 
h_gsf_dr = r.TH1F("","",50,0.,5.) 
h_ele_dr = r.TH1F("","",50,0.,5.) 
h_trk_vs_gsf_dr = r.TH1F("","",50,0.,5.) 

h_had_scale_vs_dr = r.TH2F("","",50,0.,0.5,20,0.,2.) 
h_trk_scale_vs_dr = r.TH2F("","",50,0.,0.5,20,0.,2.) 
h_gsf_scale_vs_dr = r.TH2F("","",50,0.,0.5,20,0.,2.) 
h_ele_scale_vs_dr = r.TH2F("","",50,0.,0.5,20,0.,2.) 

h_trk_eff_dr0p01 = r.TEfficiency("","",40,0.,20.) 
h_gsf_eff_dr0p01 = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p01 = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p01_trk = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p01_ecal = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p01_both = r.TEfficiency("","",40,0.,20.) 

h_trk_eff_dr0p05 = r.TEfficiency("","",40,0.,20.) 
h_gsf_eff_dr0p05 = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p05 = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p05_trk = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p05_ecal = r.TEfficiency("","",40,0.,20.) 
h_ele_eff_dr0p05_both = r.TEfficiency("","",40,0.,20.) 

################################################################################

print "Starting event loop..."
for iev,event in enumerate(events) : 
    if iev > nevents and nevents >= 0 : break 

    # event debug 
    print "Event: {:.0f} run: {:.0f} lumi: {:.0f}, event: {:.0f}".format(iev,
                                                                         event.eventAuxiliary().run(), 
                                                                         event.eventAuxiliary().luminosityBlock(),
                                                                         event.eventAuxiliary().event())
    
    # recoGenParticles_genParticles__HLT
    event.getByLabel(genLabel, genHandle)
    genparticles = sorted(list(filter( lambda gen : gen.pt() > 0.1 and abs(gen.eta()) < 2.4 and \
                                           ( abs(gen.pdgId()) == leptonid or \
                                             abs(gen.pdgId()) == 211 or \
                                             abs(gen.pdgId()) == 321 ) \
                                           and gen.numberOfMothers() > 0 \
                                           and abs(gen.mother().pdgId()) == 521, 
                                       genHandle.product() )), key=lambda x : x.pt(), reverse=True)
    genelectrons = list(filter( lambda gen : abs(gen.pdgId()) == leptonid, genparticles ))
    gentracks = list(filter( lambda gen : abs(gen.pdgId()) != leptonid, genparticles ))
    genkaons = list(filter( lambda gen : abs(gen.pdgId()) == 321, genparticles ))
    genpions = list(filter( lambda gen : abs(gen.pdgId()) == 211, genparticles ))

    # recoTracks_generalTracks__RECO
    event.getByLabel(trkLabel, trkHandle)
    #generaltracks = sorted(trkHandle.product(), key=lambda x : x.pt(), reverse=True) 
    generaltracks = sorted(list(filter( lambda trk : trk.quality(trk.qualityByName("highPurity")), 
                                        trkHandle.product() )), key=lambda x : x.pt(), reverse=True) 

    # gsfTracks_electronGsfTracks__RECO
    event.getByLabel(gsfLabel, gsfHandle)
    gsftracks = sorted(gsfHandle.product(), key=lambda x : x.pt(), reverse=True) 

    # recoGsfElectrons_gedGsfElectrons__RECO
    event.getByLabel(eleLabel, eleHandle)
    electrons = sorted(eleHandle.product(), key=lambda x : x.pt(), reverse=True) 

    #print "TEST",len(genelectrons),len(electrons),len(gsftracks),len(generaltracks)

    # gen histos
    h_genpart_n.Fill(min(len(genparticles),h_genpart_n.GetXaxis().GetXmax()-1.e-6))
    h_gentrk_n.Fill(min(len(gentracks),h_gentrk_n.GetXaxis().GetXmax()-1.e-6))
    h_genkaon_n.Fill(min(len(genkaons),h_genkaon_n.GetXaxis().GetXmax()-1.e-6))
    h_genpion_n.Fill(min(len(genpions),h_genpion_n.GetXaxis().GetXmax()-1.e-6))

    h_genele_n.Fill(min(len(genelectrons),h_genele_n.GetXaxis().GetXmax()-1.e-6))
    for igen,gen in enumerate(genelectrons) :
        h_genele_pt.Fill(min(gen.pt(),h_genele_pt.GetXaxis().GetXmax()-1.e-6))

    # trk histos
    h_trk_n.Fill(min(len(generaltracks),h_trk_n.GetXaxis().GetXmax()-1.e-6))
    for itrk,trk in enumerate(generaltracks) :
        h_trk_pt.Fill(min(trk.pt(),h_trk_pt.GetXaxis().GetXmax()-1.e-6))

    # gsftracks histos
    h_gsf_n.Fill(min(len(gsftracks),h_gsf_n.GetXaxis().GetXmax()-1.e-6))
    for igsf,gsf in enumerate(gsftracks) :
        h_gsf_pt.Fill(min(gsf.pt(),h_gsf_pt.GetXaxis().GetXmax()-1.e-6))

    # ele histos
    h_ele_n.Fill(min(len(electrons),h_ele_n.GetXaxis().GetXmax()-1.e-6))
    for iele,ele in enumerate(electrons) :
        h_ele_pt.Fill(min(ele.pt(),h_ele_pt.GetXaxis().GetXmax()-1.e-6))
    
    # gsftrack pt vs ctftrack pt
    for iele,ele in enumerate(electrons) :
        trk = ele.closestTrack().get() if ele.closestTrack().isNonnull() else None
        gsf = ele.gsfTrack().get() if ele.gsfTrack().isNonnull() else None
        if trk is not None and gsf is not None : 
            h_trk_vs_gsf_dr.Fill(min(deltaR(trk,gsf),h_trk_vs_gsf_dr.GetXaxis().GetXmax()-1.e-6))
            h_trk_vs_gsf_pt.Fill(min(trk.pt(),h_trk_vs_gsf_pt.GetXaxis().GetXmax()-1.e-6),
                                 min(gsf.pt(),h_trk_vs_gsf_pt.GetYaxis().GetXmax()-1.e-6))

    # gen-had matching
    xmax = h_had_scale_vs_dr.GetXaxis().GetXmax()-1.e-6
    ymax = h_had_scale_vs_dr.GetYaxis().GetXmax()-1.e-6
    trk_matched = []
    for igen,gen in enumerate(genkaons) :
        dr_min = 1.e6
        trk_min = None
        for itrk,trk in enumerate(generaltracks) : 
            dr = deltaR(trk,gen)
            if dr < dr_min : 
                dr_min = dr
                trk_min = trk
        if trk_min is not None and itrk not in trk_matched :
            trk_matched.append(itrk)
            h_had_dr.Fill(min(dr_min,h_had_dr.GetXaxis().GetXmax()-1.e-6))
            h_had_scale_vs_dr.Fill( min(dr_min,xmax), 
                                    min(trk_min.pt()/gen.pt(),ymax) if gen.pt() > 0. else -1. )
            #h_had_eff_dr0p01.Fill(1 if dr_min < 0.01 else 0, gen.pt())
            #h_had_eff_dr0p05.Fill(1 if dr_min < 0.05 else 0, gen.pt())

    # gen-trk matching
    xmax = h_trk_scale_vs_dr.GetXaxis().GetXmax()-1.e-6
    ymax = h_trk_scale_vs_dr.GetYaxis().GetXmax()-1.e-6
    trk_matched = []
    for igen,gen in enumerate(genelectrons) :
        dr_min = 1.e6
        trk_min = None
        for itrk,trk in enumerate(generaltracks) : 
            dr = deltaR(trk,gen)
            if dr < dr_min : 
                dr_min = dr
                trk_min = trk
        if trk_min is not None and itrk not in trk_matched :
            trk_matched.append(itrk)
            h_trk_dr.Fill(min(dr_min,h_trk_dr.GetXaxis().GetXmax()-1.e-6))
            h_trk_scale_vs_dr.Fill( min(dr_min,xmax), 
                                    min(trk_min.pt()/gen.pt(),ymax) if gen.pt() > 0. else -1. )
            h_trk_eff_dr0p01.Fill(1 if dr_min < 0.01 else 0, gen.pt())
            h_trk_eff_dr0p05.Fill(1 if dr_min < 0.05 else 0, gen.pt())
            
    # gen-gsf matching
    xmax = h_gsf_scale_vs_dr.GetXaxis().GetXmax()-1.e-6
    ymax = h_gsf_scale_vs_dr.GetYaxis().GetXmax()-1.e-6
    gsf_matched = []
    for igen,gen in enumerate(genelectrons) :
        dr_min = 1.e6
        gsf_min = None
        for igsf,gsf in enumerate(gsftracks) :
            dr = deltaR(gsf,gen)
            if dr < dr_min : 
                dr_min = dr
                gsf_min = gsf
        if gsf_min is not None and igsf not in gsf_matched :
            gsf_matched.append(igsf)
            h_gsf_dr.Fill(min(dr_min,h_gsf_dr.GetXaxis().GetXmax()-1.e-6))
            h_gsf_scale_vs_dr.Fill( min(dr_min,xmax), 
                                    min(gsf_min.pt()/gen.pt(),ymax) if gen.pt() > 0. else -1. )
            h_gsf_eff_dr0p01.Fill(1 if dr_min < 0.01 else 0, gen.pt())
            h_gsf_eff_dr0p05.Fill(1 if dr_min < 0.05 else 0, gen.pt())

    # gen-ele matching
    xmax = h_ele_scale_vs_dr.GetXaxis().GetXmax()-1.e-6
    ymax = h_ele_scale_vs_dr.GetYaxis().GetXmax()-1.e-6
    ele_matched = []
    for igen,gen in enumerate(genelectrons) :
        dr_min = 1.e6
        ele_min = None
        for iele,ele in enumerate(electrons) : 
            # match according to gsfTrack eta/phi (and not the extrapolated eta/phi for the ele)
            #gsf = ele.gsfTrack(); dr = deltaR(gsf,gen)
            dr = deltaR(ele,gen)
            if dr < dr_min : 
                dr_min = dr
                ele_min = ele
        if ele_min is not None and iele not in ele_matched :
            ele_matched.append(iele)
            h_ele_dr.Fill(min(dr_min,h_ele_dr.GetXaxis().GetXmax()-1.e-6))
            h_ele_scale_vs_dr.Fill( min(dr_min,xmax), 
                                    min(ele_min.pt()/gen.pt(),ymax) if gen.pt() > 0. else -1. )
            h_ele_eff_dr0p01.Fill(1 if dr_min < 0.01 else 0, gen.pt())
            h_ele_eff_dr0p05.Fill(1 if dr_min < 0.05 else 0, gen.pt())
            if ele.trackerDrivenSeed() and not ele.ecalDrivenSeed() : 
                h_ele_eff_dr0p01_trk.Fill(1 if dr_min < 0.01 else 0, gen.pt())
                h_ele_eff_dr0p05_trk.Fill(1 if dr_min < 0.01 else 0, gen.pt())
            if ele.ecalDrivenSeed() and not ele.trackerDrivenSeed() : 
                h_ele_eff_dr0p01_ecal.Fill(1 if dr_min < 0.01 else 0, gen.pt())
                h_ele_eff_dr0p05_ecal.Fill(1 if dr_min < 0.01 else 0, gen.pt())
            if ele.ecalDrivenSeed() and ele.trackerDrivenSeed() : 
                h_ele_eff_dr0p01_both.Fill(1 if dr_min < 0.01 else 0, gen.pt())
                h_ele_eff_dr0p05_both.Fill(1 if dr_min < 0.01 else 0, gen.pt())

################################################################################

if write_histos == False : 
    print "Do not create histogram files..."
    quit()

r.gStyle.SetOptStat(1111111)
r.gStyle.SetStatX(0.85)
r.gStyle.SetStatY(0.85)

import os
if not os.path.exists("plots/pdf") : os.makedirs("plots/pdf")
if not os.path.exists("plots/C") : os.makedirs("plots/C")
if not os.path.exists("plots/root") : os.makedirs("plots/root")

################################################################################

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_genpart_n.GetXaxis().SetTitle("N_{gen part}")
h_genpart_n.Draw()
name = "n_genParticles"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_genpart_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_gentrk_n.GetXaxis().SetTitle("N_{gen trk}")
h_gentrk_n.Draw()
name = "n_genTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gentrk_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_genkaon_n.GetXaxis().SetTitle("N_{gen kaon}")
h_genkaon_n.Draw()
name = "n_genKaons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_genkaon_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_genpion_n.GetXaxis().SetTitle("N_{gen pion}")
h_genpion_n.Draw()
name = "n_genPions"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_genpion_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_genele_n.GetXaxis().SetTitle("N_{gen ele}")
h_genele_n.Draw()
name = "n_genElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_genele_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_trk_n.GetXaxis().SetTitle("N_{trk}")
h_trk_n.Draw()
name = "n_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_gsf_n.GetXaxis().SetTitle("N_{gsf}")
h_gsf_n.Draw()
name = "n_gsfTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gsf_n
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_ele_n.GetXaxis().SetTitle("N_{ele}")
h_ele_n.Draw()
name = "n_gsfElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_n
del c

################################################################################

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_genele_pt.GetXaxis().SetTitle("p^{gen ele}_{T} [GeV]")
h_genele_pt.Draw()
name = "pT_genElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_genele_pt
del c
            
c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_trk_pt.GetXaxis().SetTitle("p^{trk}_{T} [GeV]")
h_trk_pt.Draw()
name = "pT_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_pt
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_gsf_pt.GetXaxis().SetTitle("p^{gsf}_{T} [GeV]")
h_gsf_pt.Draw()
name = "pT_gsfTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gsf_pt
del c
            
c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_ele_pt.GetXaxis().SetTitle("p^{ele}_{T} [GeV]")
h_ele_pt.Draw()
name = "pT_gsfElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_pt
del c

################################################################################

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_had_dr.GetXaxis().SetTitle("#DeltaR(had,gen)")
h_had_dr.Draw()
name = "deltaR_hadronTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_had_dr
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_trk_dr.GetXaxis().SetTitle("#DeltaR(trk,gen)")
h_trk_dr.Draw()
name = "deltaR_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_dr
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_gsf_dr.GetXaxis().SetTitle("#DeltaR(gsf,gen)")
h_gsf_dr.Draw()
name = "deltaR_gsfTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gsf_dr
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_ele_dr.GetXaxis().SetTitle("#DeltaR(ele,gen)")
h_ele_dr.Draw()
name = "deltaR_gsfElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_dr
del c

################################################################################
    
c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogz(1)
h_had_scale_vs_dr.GetXaxis().SetTitle("#DeltaR(had,gen)")
h_had_scale_vs_dr.GetYaxis().SetTitle("p^{had}_{T}/p^{gen}_{T}")
h_had_scale_vs_dr.Draw("colz")
name = "scale_vs_deltaR_hadronTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_had_scale_vs_dr
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogz(1)
h_trk_scale_vs_dr.GetXaxis().SetTitle("#DeltaR(trk,gen)")
h_trk_scale_vs_dr.GetYaxis().SetTitle("p^{trk}_{T}/p^{gen}_{T}")
h_trk_scale_vs_dr.Draw("colz")
name = "scale_vs_deltaR_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_scale_vs_dr
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogz(1)
h_gsf_scale_vs_dr.GetXaxis().SetTitle("#DeltaR(gsf,gen)")
h_gsf_scale_vs_dr.GetYaxis().SetTitle("p^{gsf}_{T}/p^{gen}_{T}")
h_gsf_scale_vs_dr.Draw("colz")
name = "scale_vs_deltaR_gsfTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gsf_scale_vs_dr
del c
    
c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogz(1)
h_ele_scale_vs_dr.GetXaxis().SetTitle("#DeltaR(ele,gen)")
h_ele_scale_vs_dr.GetYaxis().SetTitle("p^{ele}_{T}/p^{gen}_{T}")
h_ele_scale_vs_dr.Draw("colz")
name = "scale_vs_deltaR_gsfElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_scale_vs_dr
del c

################################################################################

c = r.TCanvas()
h_trk_eff_dr0p01.Draw()
r.gPad.Update()
h_trk_eff_dr0p01.SetTitle(";p^{gen}_{T} [GeV];Eff(trk | gen)")
h_trk_eff_dr0p01.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_trk_eff_dr0p01.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_trk_eff_dr0p01.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_trk_eff_dr0p01.SetMarkerColor(r.kBlack)
h_trk_eff_dr0p01.SetMarkerStyle(20)
h_trk_eff_dr0p01.SetMarkerSize(1.5)
h_trk_eff_dr0p01.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p01_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_eff_dr0p01
del c

c = r.TCanvas()
h_gsf_eff_dr0p01.Draw()
r.gPad.Update()
h_gsf_eff_dr0p01.SetTitle(";p^{gen}_{T} [GeV];Eff(gsf | gen)")
h_gsf_eff_dr0p01.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_gsf_eff_dr0p01.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_gsf_eff_dr0p01.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_gsf_eff_dr0p01.SetMarkerColor(r.kBlack)
h_gsf_eff_dr0p01.SetMarkerStyle(20)
h_gsf_eff_dr0p01.SetMarkerSize(1.5)
h_gsf_eff_dr0p01.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p01_gsfTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gsf_eff_dr0p01
del c

c = r.TCanvas()
h_ele_eff_dr0p01.Draw()
r.gPad.Update()
h_ele_eff_dr0p01.SetTitle(";p^{gen}_{T} [GeV];Eff(ele | gen)")
h_ele_eff_dr0p01.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p01.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p01.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p01.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p01.SetMarkerStyle(20)
h_ele_eff_dr0p01.SetMarkerSize(1.5)
h_ele_eff_dr0p01.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p01_gsfElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p01
del c

c = r.TCanvas()
h_ele_eff_dr0p01_trk.Draw()
r.gPad.Update()
h_ele_eff_dr0p01_trk.SetTitle(";p^{gen}_{T} [GeV];Eff(ele(trk) | gen)")
h_ele_eff_dr0p01_trk.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p01_trk.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p01_trk.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p01_trk.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p01_trk.SetMarkerStyle(20)
h_ele_eff_dr0p01_trk.SetMarkerSize(1.5)
h_ele_eff_dr0p01_trk.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p01_gsfElectrons_trk"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p01_trk
del c

c = r.TCanvas()
h_ele_eff_dr0p01_ecal.Draw()
r.gPad.Update()
h_ele_eff_dr0p01_ecal.SetTitle(";p^{gen}_{T} [GeV];Eff(ele(ecal) | gen)")
h_ele_eff_dr0p01_ecal.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p01_ecal.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p01_ecal.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p01_ecal.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p01_ecal.SetMarkerStyle(20)
h_ele_eff_dr0p01_ecal.SetMarkerSize(1.5)
h_ele_eff_dr0p01_ecal.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p01_gsfElectrons_ecal"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p01_ecal
del c

c = r.TCanvas()
h_ele_eff_dr0p01_both.Draw()
r.gPad.Update()
h_ele_eff_dr0p01_both.SetTitle(";p^{gen}_{T} [GeV];Eff(ele(both) | gen)")
h_ele_eff_dr0p01_both.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p01_both.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p01_both.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p01_both.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p01_both.SetMarkerStyle(20)
h_ele_eff_dr0p01_both.SetMarkerSize(1.5)
h_ele_eff_dr0p01_both.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p01_gsfElectrons_both"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p01_both
del c

################################################################################

c = r.TCanvas()
h_trk_eff_dr0p05.Draw()
r.gPad.Update()
h_trk_eff_dr0p05.SetTitle(";p^{gen}_{T} [GeV];Eff(trk | gen)")
h_trk_eff_dr0p05.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_trk_eff_dr0p05.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_trk_eff_dr0p05.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_trk_eff_dr0p05.SetMarkerColor(r.kBlack)
h_trk_eff_dr0p05.SetMarkerStyle(20)
h_trk_eff_dr0p05.SetMarkerSize(1.5)
h_trk_eff_dr0p05.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p05_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_eff_dr0p05
del c

c = r.TCanvas()
h_gsf_eff_dr0p05.Draw()
r.gPad.Update()
h_gsf_eff_dr0p05.SetTitle(";p^{gen}_{T} [GeV];Eff(gsf | gen)")
h_gsf_eff_dr0p05.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_gsf_eff_dr0p05.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_gsf_eff_dr0p05.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_gsf_eff_dr0p05.SetMarkerColor(r.kBlack)
h_gsf_eff_dr0p05.SetMarkerStyle(20)
h_gsf_eff_dr0p05.SetMarkerSize(1.5)
h_gsf_eff_dr0p05.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p05_gsfTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_gsf_eff_dr0p05
del c

c = r.TCanvas()
h_ele_eff_dr0p05.Draw()
r.gPad.Update()
h_ele_eff_dr0p05.SetTitle(";p^{gen}_{T} [GeV];Eff(ele | gen)")
h_ele_eff_dr0p05.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p05.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p05.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p05.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p05.SetMarkerStyle(20)
h_ele_eff_dr0p05.SetMarkerSize(1.5)
h_ele_eff_dr0p05.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p05_gsfElectrons"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p05
del c

c = r.TCanvas()
h_ele_eff_dr0p05_trk.Draw()
r.gPad.Update()
h_ele_eff_dr0p05_trk.SetTitle(";p^{gen}_{T} [GeV];Eff(ele(trk) | gen)")
h_ele_eff_dr0p05_trk.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p05_trk.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p05_trk.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p05_trk.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p05_trk.SetMarkerStyle(20)
h_ele_eff_dr0p05_trk.SetMarkerSize(1.5)
h_ele_eff_dr0p05_trk.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p05_gsfElectrons_trk"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p05_trk
del c

c = r.TCanvas()
h_ele_eff_dr0p05_ecal.Draw()
r.gPad.Update()
h_ele_eff_dr0p05_ecal.SetTitle(";p^{gen}_{T} [GeV];Eff(ele(ecal) | gen)")
h_ele_eff_dr0p05_ecal.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p05_ecal.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p05_ecal.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p05_ecal.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p05_ecal.SetMarkerStyle(20)
h_ele_eff_dr0p05_ecal.SetMarkerSize(1.5)
h_ele_eff_dr0p05_ecal.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p05_gsfElectrons_ecal"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p05_ecal
del c

c = r.TCanvas()
h_ele_eff_dr0p05_both.Draw()
r.gPad.Update()
h_ele_eff_dr0p05_both.SetTitle(";p^{gen}_{T} [GeV];Eff(ele(both) | gen)")
h_ele_eff_dr0p05_both.GetPaintedGraph().GetYaxis().SetNdivisions(510)
h_ele_eff_dr0p05_both.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
h_ele_eff_dr0p05_both.GetPaintedGraph().GetXaxis().SetRangeUser(0.,400.)
h_ele_eff_dr0p05_both.SetMarkerColor(r.kBlack)
h_ele_eff_dr0p05_both.SetMarkerStyle(20)
h_ele_eff_dr0p05_both.SetMarkerSize(1.5)
h_ele_eff_dr0p05_both.SetLineColor(r.kBlack)
r.gStyle.SetOptStat(0)
c.Update()
name = "eff_dr0p05_gsfElectrons_both"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_ele_eff_dr0p05_both
del c

################################################################################

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogz(1)
h_trk_vs_gsf_pt.GetXaxis().SetTitle("p^{trk}_{T} [GeV]")
h_trk_vs_gsf_pt.GetYaxis().SetTitle("p^{gsf}_{T} [GeV]")
h_trk_vs_gsf_pt.Draw("colz")
name = "pT_gsfTracks_vs_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_vs_gsf_pt
del c

c = r.TCanvas()
r.gStyle.SetOptStat(1111111)
c.SetLogy(1)
h_trk_vs_gsf_dr.GetXaxis().SetTitle("#DeltaR(trk,gsf)")
h_trk_vs_gsf_dr.Draw()
name = "deltaR_gsfTracks_vs_generalTracks"
c.SaveAs("plots/pdf/"+name+".pdf"); c.SaveAs("plots/C/"+name+".C"); c.SaveAs("plots/root/"+name+".root")
del h_trk_vs_gsf_dr
del c
