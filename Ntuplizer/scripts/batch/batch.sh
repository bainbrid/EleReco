export X509_USER_PROXY=/afs/cern.ch/user/b/bainbrid/x509up_u58809
export CMSSW=/eos/user/b/bainbrid/electrons/CMSSW_9_4_1/src
export CFG="RECOSIM_cfg.py"
export OUT="RECOSIM.root"
export TOP="$PWD"

cd $CMSSW
eval `scramv1 runtime -sh`
cd $TOP

cmsRun $CMSSW/$CFG
rfcp $OUT $CMSSW/$OUT
