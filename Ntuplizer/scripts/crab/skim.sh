# essentially copies 10 events of FILEIN to local disk
# PUMix data tier does not have RECO by default, only RAW, SIM, HLT (correct?)
cmsRun skim_cfg.py inputFiles=${FILEIN} outputFile=EleReco_Seed2p0.root maxEvents=10
