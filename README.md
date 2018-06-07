# EleReco

Produces flat trees used to determine efficiency for electron reconstruction chain.

Flat trees are produced using simple EDAnalyzer "LowPtEleNtuplizer" class.

## Recipe

```
cmsrel CMSSW_9_4_8
cd CMSSW_9_4_8/src
cmsenv
git cms-init
git clone git@github.com:ICBPHCMS/EleReco.git
cd EleReco
git checkout Ntuplizer_CMSSW_9_4_X
scram b
voms-proxy-init --voms cms
cd Ntuplizer/test/
cmsRun LowPtEleNtuplizer_cfg.py
```

### Studies with trackerDrivenElectronSeed.MinPt = 2.0, 1.0, and 0.5 GeV

The following requires three separate release areas.

#### Recipe for 2.0 GeV threshold

##### Set up release area

```
mkdir my_dir_2p0; cd my_dir_2p0
cmsrel CMSSW_9_4_8
cd CMSSW_9_4_8/src
cmsenv
git cms-init
git clone git@github.com:ICBPHCMS/EleReco.git
cd EleReco
git checkout Ntuplizer_CMSSW_9_4_X
cd ..
scram b
```

##### Run RERECO step interactively or via crab 

```
voms-proxy-init --voms cms
cd EleReco/Ntuplizer/scripts/crab

# produce single test file interactively
FILEIN=root://gfe02.grid.hep.ph.ic.ac.uk:1097//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1460.root
FILEOUT=EleReco_Seed2p0
. cmsDriver.sh
cmsRun ${FILEOUT}_cfg.py

# produce RERECO sample via crab (to come)
python crab.py
```

##### Run ntuplizer step

```
cd ../../test/
cmsRun LowPtEleNtuplizer_cfg.py inputFiles=file:../scripts/crab/EleReco_Seed2p0.root outputFile=output.root maxEvents=10
```

##### Run plotting script

```
cd ../scripts/uproot
# to come
```

#### Recipe for 1.0 GeV threshold

##### Set up 2nd release area

```
mkdir my_dir_1p0; cd my_dir_1p0
cmsrel CMSSW_9_4_8
cd CMSSW_9_4_8/src
cmsenv
git cms-init
git remote add ICBPHCMS git@github.com:ICBPHCMS/cmssw.git
git cms-merge-topic ICBPHCMS:from-CMSSW_9_4_8-EleReco-Seed1p0
git clone git@github.com:ICBPHCMS/EleReco.git
cd EleReco
git checkout Ntuplizer_CMSSW_9_4_X
cd ..
scram b
```

##### Run RERECO step interactively or via crab 

```
voms-proxy-init --voms cms
cd EleReco/Ntuplizer/scripts/crab

# produce single test file interactively
FILEIN=root://gfe02.grid.hep.ph.ic.ac.uk:1097//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1460.root
FILEOUT=EleReco_Seed1p0
. cmsDriver.sh
cmsRun ${FILEOUT}_cfg.py
# produce RERECO sample via crab
python crab.py --name=${FILEOUT} --instance="phys03" --dataset="/BToKee_Pythia/tstreble-BToKee_Pythia_PUMix_18_03_18-c9b9e020b5bce5ee6bee9ef5f38c415a/USER"
```

##### Run ntuplizer step

```
cd ../../test/
cmsRun LowPtEleNtuplizer_cfg.py inputFiles=file:../scripts/crab/EleReco_Seed1p0.root outputFile=output.root maxEvents=10
```

##### Run plotting script

```
cd ../scripts/uproot
# to come
```

#### Recipe for 0.5 GeV threshold

As for 1.0 GeV recipe, but just replace ```1p0``` with ```0p5```, everywhere
