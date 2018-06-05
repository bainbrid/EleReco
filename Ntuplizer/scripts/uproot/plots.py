import uproot
import numpy as np
from setTDRStyle import setTDRStyle
import ROOT as r
from math import sqrt
import numpy as np
import numpy.ma as ma
import re

################################################################################
# 
class Tree(object) :

    def __init__(self,filename) :
        print "Creating tree",filename,"..."
        self.prefix = "branch_"
        self.filename = filename
        self.file = uproot.open(filename)
        self.tree = self.file['LowPtEleNtuplizer/tree']
        for branch in self.tree.allkeys() : self.setter(branch,self.tree.array(branch))
        self.add() 
        self.branches = [ x.replace(self.prefix,"") for x in dir(self) if x.startswith(self.prefix) ]
        
    def __str__(self) :
        string  = "Filename: {:s}\n".format(self.filename)
        string += "Branches :\n"
        for branch in self.branches : string += "  "+branch+"\n"
        return string

    def getter(self,branch) : 
        values = getattr(self,self.prefix+branch)
        if "JaggedArray" in str(type(values)) : return values.content
        else : return values 

    def setter(self,branch,values) : 
        return setattr(self,self.prefix+branch,values)

    def filter(self,branch,filter) : 
        return ma.array(self.getter(branch),mask=~self.getter(filter)).compressed()

    def add(self) :
        pass

#        # define mask to identify lead lepton based on gen pT
#        lead = [ lp>lm for lp,lm in zip(self.getter("bd_lp_pt"),self.getter("bd_lm_pt"))]
#
#        # add ll_lead and ll_sub variables 
#        for var in ["pt","eta","phi","mass","charge"] :
#            self.setter("bd_ll_lead_"+var,
#                        np.array([ lp if ok else lm for lp,lm,ok in zip(self.getter("bd_lp_"+var),
#                                                                        self.getter("bd_lm_"+var),
#                                                                        lead) ]))
#            self.setter("bd_ll_sub_"+var,
#                        np.array([ lp if ~ok else lm for lp,lm,ok in zip(self.getter("bd_lp_"+var),
#                                                                         self.getter("bd_lm_"+var),
#                                                                         lead) ]))
#            self.setter("bd_ll_lead_reco_"+var,
#                        np.array([ lp if ok else lm for lp,lm,ok in zip(self.getter("bd_lp_reco_"+var),
#                                                                        self.getter("bd_lm_reco_"+var),
#                                                                        lead) ]))
#            self.setter("bd_ll_sub_reco_"+var,
#                        np.array([ lp if ~ok else lm for lp,lm,ok in zip(self.getter("bd_lp_reco_"+var),
#                                                                         self.getter("bd_lm_reco_"+var),
#                                                                         lead) ]))
#            
#        # trigger acceptance 
#        self.setter("tag_mu_low", ( self.getter("tag_mu_pt") > 7. )  & ( abs(self.getter("tag_mu_eta")) < 2.5 ) )
#        self.setter("tag_mu_high", ( self.getter("tag_mu_pt") > 12. ) & ( abs(self.getter("tag_mu_eta")) < 2.5 ) )
#        
#        # acceptance thresholds
#        apply=["standard","open","tight","open_pt"][1]
#        pt_cut = {"standard":0.5,"open":0.,"tight":2.,"open_pt":0.}[apply]
#        eta_cut = {"standard":2.5,"open":9999.,"tight":0.8,"open_pt":2.5}[apply]
#        pt_reco_cut = {"standard":0.5,"open":0.,"tight":2.,"open_pt":0.}[apply]
#        eta_reco_cut = {"standard":2.5,"open":9999.,"tight":0.8,"open_pt":2.5}[apply]
#
#        # GEN object acceptance (ignoring trigger)
#        self.setter("bd_lp_pass", ( self.getter("bd_lp_pt") > pt_cut ) & ( abs(self.getter("bd_lp_eta")) < eta_cut ) )
#        self.setter("bd_lm_pass", ( self.getter("bd_lm_pt") > pt_cut ) & ( abs(self.getter("bd_lm_eta")) < eta_cut ) )
#        self.setter("bd_k_pass", ( self.getter("bd_k_pt") > pt_cut ) & ( abs(self.getter("bd_k_eta")) < eta_cut ) )
#        self.setter("bd_pi_pass", ( self.getter("bd_pi_pt") > pt_cut ) & ( abs(self.getter("bd_pi_eta")) < eta_cut ) )
#        self.setter("bd_all_pass", self.getter("bd_lp_pass") & self.getter("bd_lm_pass") & self.getter("bd_k_pass") & ( self.getter("bd_pi_pass") | ~self.bkstll ) )
#
#        # RECO object acceptance (ignoring trigger and GEN acceptance)
#        self.setter("bd_lp_reco_pass", ( self.getter("bd_lp_reco_pt") > pt_reco_cut ) & ( abs(self.getter("bd_lp_reco_eta")) < eta_reco_cut ) )
#        self.setter("bd_lm_reco_pass", ( self.getter("bd_lm_reco_pt") > pt_reco_cut ) & ( abs(self.getter("bd_lm_reco_eta")) < eta_reco_cut ) )
#        self.setter("bd_k_reco_pass", (  self.getter("bd_k_reco_pt") > pt_reco_cut ) & ( abs( self.getter("bd_k_reco_eta")) < eta_reco_cut ) )
#        self.setter("bd_pi_reco_pass", ( self.getter("bd_pi_reco_pt") > pt_reco_cut ) & ( abs(self.getter("bd_pi_reco_eta")) < eta_reco_cut ) )
#        self.setter("bd_all_reco_pass", self.getter("bd_lp_reco_pass") & self.getter("bd_lm_reco_pass") & self.getter("bd_k_reco_pass") & ( self.getter("bd_pi_reco_pass") | ~self.bkstll ) )
#
#        # event acceptance given trigger 
#        self.setter("evt_low", self.getter("bd_all_pass") & self.getter("tag_mu_low") )
#        self.setter("evt_high", self.getter("bd_all_pass") & self.getter("tag_mu_high") )
#        self.setter("evt_reco_low", self.getter("bd_all_reco_pass") & self.getter("tag_mu_low") )
#        self.setter("evt_reco_high", self.getter("bd_all_reco_pass") & self.getter("tag_mu_high") )

    # print summary of acceptances 
    def acceptance(self) :
        pad = 32
        print "Filename".ljust(pad),self.filename
#        print "No requirement on tag muon:"
#        print "  N(events)".ljust(pad),self.bd_lp_pt.shape[0]
#        print "  N(l+ from probe)".ljust(pad),sum(self.bd_lp_pass)
#        print "  N(l- from probe)".ljust(pad),sum(self.bd_lm_pass)
#        print "  N(k from probe)".ljust(pad),sum(self.bd_k_pass)
#        print "  N(pi from probe)".ljust(pad),sum(self.bd_pi_pass)
#        print "  N(all from probe)".ljust(pad),sum(self.bd_all_pass) 
#        print "  Acc(all from probe)".ljust(pad),"{:0.3f}".format(sum(self.bd_all_pass)*1. / self.bd_lp_pt.shape[0])
#        print "Lower threshold on tag muon:"
#        print "  N(tag muon pT > 7 GeV)".ljust(pad),sum(self.tag_mu_low)
#        print "  N(l+ from probe)".ljust(pad),sum(self.bd_lp_pass&self.tag_mu_low)
#        print "  N(l- from probe)".ljust(pad),sum(self.bd_lm_pass&self.tag_mu_low)
#        print "  N(k from probe)".ljust(pad),sum(self.bd_k_pass&self.tag_mu_low)
#        print "  N(pi from probe)".ljust(pad),sum(self.bd_pi_pass&self.tag_mu_low)
#        print "  N(all from probe)".ljust(pad),sum(self.bd_all_pass&self.tag_mu_low)
#        print "  Acc(all from probe | tag muon)".ljust(pad),"{:.3f}".format(sum(self.bd_all_pass&self.tag_mu_low)*1. / sum(self.tag_mu_low)*1.)
#        print "Higher threshold on tag muon:"
#        print "  N(tag muon pT > 12 GeV)".ljust(pad),sum(self.tag_mu_high)
#        print "  N(l+ from probe)".ljust(pad),sum(self.bd_lp_pass&self.tag_mu_high)
#        print "  N(l- from probe)".ljust(pad),sum(self.bd_lm_pass&self.tag_mu_high)
#        print "  N(k from probe)".ljust(pad),sum(self.bd_k_pass&self.tag_mu_high)
#        print "  N(pi from probe)".ljust(pad),sum(self.bd_pi_pass&self.tag_mu_high)
#        print "  N(all from probe)".ljust(pad),sum(self.bd_all_pass&self.tag_mu_high)
#        print "  Acc(all from probe | tag muon)".ljust(pad),"{:.3f}".format(sum(self.bd_all_pass&self.tag_mu_high)*1. / sum(self.tag_mu_high)*1.)

################################################################################
# 
class Analysis(object) :
    def __init__(self,filenames) :

        self.filenames = filenames 
        self.trees = []
        for filename in self.filenames :
            self.trees.append( Tree(filename) )
        # backup dirs 
        import os
        import datetime
        if os.path.isdir("plots") : 
            name = "plots_backup_"+datetime.datetime.now().strftime("%y%m%d_%H%M")
            print "'plots' directory exists! renaming to '{:s}'".format(name)
            os.rename("plots",name)
        os.makedirs("plots")

    def __str__(self) :
        string  = "Analysis of {:.0f} trees...\n\n".format(len(self.filenames))
        for tree in self.trees : string += tree.__str__()
        return string

    def eff(self,
            dir="plots",
            verbose=False,
            ) :

        # util
        
        binning = np.append(np.logspace(-3.0, 1.0, 40, endpoint=False),
                            np.logspace( 1.0, 3.0, 2))
        setTDRStyle()
        colors = [r.kBlue,r.kGreen,r.kRed,r.kOrange,r.kYellow]
        styles = [20,20,20,20,20]
        sizes = [1.7,1.6,1.5,1.4,1.3]

        effs_pt = []
        effs_eta = []
        for gen,reco in [("genMuons","genTrks"),
                         ("genKaons","genTrks"),
                         ("genEles","genTrks"),
                         ("genEles","gsfTrks"),
                         #("genEles","gsfElectrons"), #@@ ADD THIS!!! NEEDS NEW NTUPLES!!! 
                         ] :

            # just use 2GeV sample for now
            tree = filter( lambda x : "2GeV" in x[0], zip(self.filenames,self.trees) )[0][1]

            effs_pt.append(r.TEfficiency("pt_{:s}_{:s}".format(gen,reco),"",len(binning)-1,binning))
            effs_eta.append(r.TEfficiency("eta_{:s}_{:s}".format(gen,reco),"",50,-2.5,2.5))
            pts = tree.getter("{:s}_Pt".format(gen))
            etas = tree.getter("{:s}_Eta".format(gen))
            idxs = tree.getter("{:s}_{:s}_Idx".format(gen,reco))
            drs = tree.getter("{:s}_{:s}_DR".format(gen,reco))
            for pt,eta,idx,dr in zip(pts,etas,idxs,drs) :
                matched = (idx >= 0) and (dr < 0.01)
                effs_pt[-1].Fill(True if matched else False, pt)
                effs_eta[-1].Fill(True if matched else False, eta)

        # create plot that compares eff curves in pt
        c = r.TCanvas()
        c.SetLogx()
        legend = r.TLegend(0.6,0.4-0.04*len(effs_pt),0.85,0.4)
        for ieff,eff in enumerate(effs_pt) :
            eff.Draw("" if ieff == 0 else "same")
            r.gPad.Update()
            if ieff == 0 : 
                r.gStyle.SetOptStat(0)
                eff.SetTitle(";p^{gen}_{T} [GeV];Efficency")
                eff.GetPaintedGraph().GetYaxis().SetNdivisions(510)
                eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.)
                eff.GetPaintedGraph().GetXaxis().SetRangeUser(0.001,1000.)
            eff.SetMarkerColor(colors[ieff])
            eff.SetMarkerStyle(styles[ieff])
            eff.SetMarkerSize(sizes[ieff])
            eff.SetLineColor(colors[ieff])
            c.Update()
            legend.AddEntry(eff,eff.GetName(),"pl")
        legend.SetTextSize(0.025)
        legend.Draw("same")
        c.SaveAs("plots/efficiency_pt.pdf")
        for eff in effs_pt : del eff
        del c

        # create plot that compares eff curves in eta
        c = r.TCanvas()
        legend = r.TLegend(0.4,0.35-0.04*len(effs_eta),0.6,0.35)
        for ieff,eff in enumerate(effs_eta) :
            eff.Draw("" if ieff == 0 else "same")
            r.gPad.Update()
            if ieff == 0 : 
                r.gStyle.SetOptStat(0)
                eff.SetTitle(";|#eta^{gen}|;Efficency")
                eff.GetPaintedGraph().GetYaxis().SetNdivisions(510)
                eff.GetPaintedGraph().GetYaxis().SetRangeUser(0,1.)
                eff.GetPaintedGraph().GetXaxis().SetRangeUser(-2.5,2.5)
            eff.SetMarkerColor(colors[ieff])
            eff.SetMarkerStyle(styles[ieff])
            eff.SetMarkerSize(sizes[ieff])
            eff.SetLineColor(colors[ieff])
            c.Update()
            legend.AddEntry(eff,eff.GetName(),"pl")
        legend.SetTextSize(0.025)
        legend.Draw("same")
        c.SaveAs("plots/efficiency_eta.pdf")
        for eff in effs_eta : del eff
        del c

        efficiencies = {}
        for eff in effs_pt :
            keys = []
            vals = []
            numer = eff.GetCopyPassedHisto()
            denom = eff.GetCopyTotalHisto()
            for bin in range(1,numer.GetXaxis().GetNbins()+1) :
                k = numer.GetBinLowEdge(bin)
                n = numer.GetBinContent(bin)
                d = denom.GetBinContent(bin)
                v = float(n)/float(d) if d>0 else 0.
                keys.append(k)
                vals.append(v)
            #efficiencies[eff.GetName()] = zip(keys,vals) # [(k,v),(),...]
            efficiencies[eff.GetName()] = (keys,vals) #([],[])
        #print efficiencies
        import pickle 
        file = open('effs.pkl','wb')
        pickle.dump(efficiencies,file)
        file.close()

    def effs(self,
             dir="plots",
             verbose=False,
             ) :

        # util
        setTDRStyle()
        colors = [r.kBlue,r.kRed,r.kGreen,r.kOrange]
        styles = [20,20,20,20]
        sizes = [1.8,1.6,1.4,1.2]

        # find "_Idx" branches that are denominators of eff plots 
        filters=["gen(.*)_Idx"] 
        all_branches = list(set([ branch for tree in self.trees for branch in tree.branches ]))
        all_branches = [ b for b in all_branches for f in filters if len(re.findall(f,b)) > 0 ]

        # separate plot for each branch 
        for branch in all_branches : 

            # create TEff objects from different trees 
            effs = []
            for itree,tree in enumerate(self.trees) :
                effs.append(r.TEfficiency(branch,branch,20,0.,10.)) 

                # pt,idx,dr values for gen eles/muons 
                values = zip(tree.getter(branch.split("_")[0]+"_Pt"),
                             tree.getter(branch.split("_")[1]+"_Pt"),
                             tree.getter(branch),
                             tree.getter(branch.replace("_Idx","_DR")))
                for ii,(gen_pt,reco_pt,idx,dr) in enumerate(values) : 
                    matched = (idx >= 0) and (dr < 0.05)
                    #if ii < 10 : print "idx",idx,"  dr",dr,"  matched",matched,"  gen_pt",gen_pt,"  reco_pt",reco_pt
                    effs[-1].Fill(True if matched else False, gen_pt)

            # create plot that compares eff curves 
            c = r.TCanvas()
            legend = r.TLegend(0.5,0.4-0.04*len(self.trees),0.75,0.4)
            for ieff,(eff,tree) in enumerate(zip(effs,self.trees)) :
                eff.Draw("" if ieff == 0 else "same")
                r.gPad.Update()
                if ieff == 0 : 
                    r.gStyle.SetOptStat(0)
                    eff.SetTitle(";p^{gen}_{T} [GeV];Efficency")
                    eff.GetPaintedGraph().GetYaxis().SetNdivisions(510)
                    eff.GetPaintedGraph().GetYaxis().SetRangeUser(0.,1.01)
                    eff.GetPaintedGraph().GetXaxis().SetRangeUser(0.,10.)
                eff.SetMarkerColor(colors[ieff])
                eff.SetMarkerStyle(styles[ieff])
                eff.SetMarkerSize(sizes[ieff])
                eff.SetLineColor(colors[ieff])
                c.Update()
                legend.AddEntry(eff,tree.filename.replace("output_BToKee_","").replace(".root",""),"l")

            legend.SetTextSize(0.03)
            legend.Draw("same")
            name = "eff_"+branch
            c.SaveAs("plots/"+name+".pdf")
            for eff in effs : del eff
            del c

    def plot(self,
             dir="plots",
             norm=False,
             logy=True,
             verbose=False,
             filters=[],#["bd_(.*)(?!reco)(.*)_pt"]
             ) :

        # util
        setTDRStyle()
        binning = {
            "_N":{"xbin":10,"xlow":0.,"xhigh":10.},
            "genTrks_N":{"xbin":200,"xlow":0.,"xhigh":2000.},
            "gsfTrks_N":{"xbin":20,"xlow":0.,"xhigh":100.},
            "gsfEles_N":{"xbin":30,"xlow":0.,"xhigh":30.,"yhigh":5.e3},
            "_Pt":{"xbin":50,"xlow":0.,"xhigh":10.},
            "_Eta":{"xbin":50,"xlow":-5.,"xhigh":5.},
            "_Phi":{"xbin":64,"xlow":-3.2,"xhigh":3.2},
            "_DR":{"xbin":50,"xlow":0.,"xhigh":0.5},
            "_DXY":{"xbin":50,"xlow":0.,"xhigh":5.},
            "_DZ":{"xbin":50,"xlow":0.,"xhigh":5.},
            }
        colors = [r.kBlue,r.kRed,r.kGreen,r.kOrange]
        styles = [1,1,9,9]
        widths = [4,2,2,2]

        # branches 
        all_branches = list(set([ branch for tree in self.trees for branch in tree.branches ]))
        if len(filters) > 0 : all_branches = [ b for b in all_branches for f in filters if len(re.findall(f,b)) > 0 ]

        # iterate through branches 
        for ibranch,branch in enumerate(all_branches) : 
            print "Plotting branch",branch,"..."
            if "genKaons_genTrks" in branch : continue 
            if "genTrks_" in branch : continue 
            #if "_N" not in branch : continue

            # determine tree with most entries in first branch 
            #if ibranch == 0 : 
            largest = max([ (index,len(tree.getter(branch))) for index,tree in enumerate(self.trees) ])[0]

            # ignore "event" branch (causes problems)
            if branch == "EventNumber" or branch == "LumiSection" : continue 

            # determine binning, maximum, over using tree with most entries (and remove -999. entries!!!)
            values = self.trees[largest].getter(branch)
            values = np.array([ x for x in values if x > -9. ]) #@@ 
            if values.shape[0] > 0 and "bool" in str(type(values[0])) : values = [ 1. if x is True else 0. for x in values ]
            #if any( [ x in branch for x in binning.keys() ] ) :
            matches = filter( lambda x : x in branch, binning.keys() ) 
            if len(matches) > 0 :contents, low_edges = np.histogram(values,bins=np.linspace(binning[matches[-1]]["xlow"],
                                                                                            binning[matches[-1]]["xhigh"],
                                                                                            binning[matches[-1]]["xbin"]+1))
            else : 
                try :
                    _max = max(values)
                    _min = min(values)
                    _diff = np.diff(np.unique(values)).min()
                    _bins = int((_max-_min)/_diff)+1 
                    if _diff < 1. and _bins > 51 : _bins = 51 
                    contents, low_edges = np.histogram(values,bins=np.linspace(_min,_max,_bins))#bins='doane'
                except :
                    print "Error creating np.histogram object!",values[:10]
                    continue 

            underflow = len([ x for x in values if x < low_edges[0] ])
            overflow = len([ x for x in values if x > low_edges[-1] ])
            contents = np.append(contents,[overflow])
            total = sum(contents)
            if norm and total > 0. : contents = [ x*1. / total*1. for x in contents ]
            maximum = max(contents)

            # for each branch, create plot that compares distributions from different trees 
            c = r.TCanvas()
            histos = []
            legend = r.TLegend(0.7,0.9-0.04*len(self.trees),0.9,0.9)
            for itree,tree in enumerate(self.trees) :

                # determine histogram content using numpy (quicker!)
                values = tree.getter(branch)
                if values.shape[0] > 0 and "bool" in str(type(values[0])) : values = [ 1. if x is True else 0. for x in values ]
                matches = filter( lambda x : x in branch, binning.keys() )
                if len(matches) > 0 : contents,_ = np.histogram(values,bins=np.linspace(binning[matches[-1]]["xlow"],
                                                                                        binning[matches[-1]]["xhigh"],
                                                                                        binning[matches[-1]]["xbin"]+1))
                else : contents,_ = np.histogram(values,bins=low_edges)

                name = tree.filename+"_"+branch
                histos.append(r.TH1F(name,branch,len(low_edges)-1,low_edges))
                his = histos[-1]
                for low,val in zip(low_edges,contents) : 
                    his.SetBinContent(his.FindBin(low+1.e-6),val)
                    his.SetBinError(his.FindBin(low+1.e-6),sqrt(val))

                # add overflow to final bin (ignore underflow for now)
                underflow = len([ x for x in values if x < low_edges[0] ])
                overflow = len([ x for x in values if x > low_edges[-1] ])
                his.SetBinContent(his.GetNbinsX(),his.GetBinContent(his.GetNbinsX())+overflow)
                his.SetBinError(his.GetNbinsX(),sqrt(his.GetBinError(his.GetNbinsX())**2.+overflow))
                if "_N" in branch : total = sum([x*y for x,y in zip(low_edges,contents)]) #@@ bug?
                else : total = sum(contents)+overflow
                his.SetEntries(total) 

                # normalize?
                if norm and total > 0. : his.Scale(1./total*1.)

                # draw cosmetics
                his.SetTitle(";{:s};a.u.".format(branch))
                his.SetMarkerColor(colors[itree])
                his.SetLineColor(colors[itree])
                his.SetLineStyle(styles[itree])
                his.SetLineWidth(widths[itree])
                if itree == 0 : 
#                    if norm : 
#                        his.SetMaximum(maximum*1./total*1.) if total > 0. else his.SetMaximum(1.0)
#                    else : 
#                    matches = filter( lambda x : x in branch, binning.keys() ) 
                    his.SetMaximum(maximum*3.)
                    his.Draw("hist")
                else : 
                    his.Draw("histsame")
                legend.AddEntry(his,tree.filename.split("_")[2].replace(".root",""),"l")
                #legend.AddEntry(his,tree.filename.split("_")[2].replace(".root","")+" ({:.0f})".format(total),"l")

            r.gStyle.SetOptStat(0)
            legend.SetTextSize(0.03)
            legend.Draw("same")
            if logy : c.SetLogy()
            c.Update()
            c.SaveAs("{:s}/{:s}.pdf".format(dir,branch))
            del c

################################################################################
# print global variables 

if __name__ == '__main__' :

    files = [
        "output_BToKee_2GeV.root",
        # "output_BToKee_1GeV.root",
        # "output_BToKee_0p5GeV.root",
        ]
    
    a = Analysis(files)
    # print a 
    # for tree in a.trees : tree.acceptance(); print 

    # a.plot() # comparisom plots of several variables from different RERECOs (with diff threholds)
    # a.effs() # plots efficiencies for different RERECOs vs gen pT
    # a.eff() # plots efficiencies for different RECO objects vs log of gen pT (for first input file only), and creates effs.pkl file 
