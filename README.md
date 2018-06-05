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
