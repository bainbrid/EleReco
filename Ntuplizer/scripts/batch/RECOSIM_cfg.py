# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --filein file:BToKee_PUMix.root --fileout file:RECOSIM.root --python_filename RECOSIM_cfg.py --nThreads 1 --mc --geometry DB:Extended --era Run2_2017 --conditions 94X_mc2017_realistic_v12 --eventcontent RECOSIM --datatier RECOSIM --step RAW2DIGI,RECO,RECOSIM,EI --customise Configuration/DataProcessing/Utils.addMonitoring -n -1 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('CommonTools.ParticleFlow.EITopPAG_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1460.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1462.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1443.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1419.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1491.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1493.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1490.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1489.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1485.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1470.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1478.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1469.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1452.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1481.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1468.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1463.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1457.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1435.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1465.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1456.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5313.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2048.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2327.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2353.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1593.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1984.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1750.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5260.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5342.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5310.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2672.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2214.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1180.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5269.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2125.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5365.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1101.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1977.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2635.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2651.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2352.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2670.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1292.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5345.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1450.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1448.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1298.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1031.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1332.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5355.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5352.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2183.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1758.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1310.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1260.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5333.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5364.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5324.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_495.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_479.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_491.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_481.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_485.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_497.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1455.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1428.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1401.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1397.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1432.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1449.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1451.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1446.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1447.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1409.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1439.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1417.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1407.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1405.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1445.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1440.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1391.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1394.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1399.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1408.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1364.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1438.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1434.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1422.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1379.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1376.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1358.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1386.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1423.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1425.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1416.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1350.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1403.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1413.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1410.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1415.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1406.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1412.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1420.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5935.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5910.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1381.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5916.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5917.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0003/BToKee_PUMix_3009.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1079.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_496.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5921.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5908.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5893.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5931.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5922.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5918.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5936.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_790.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5863.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5919.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5920.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_969.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_563.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0002/BToKee_PUMix_2768.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_811.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5876.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1075.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_17.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_19.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0000/BToKee_PUMix_18.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1466.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5337.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5256.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1288.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5351.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5277.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1444.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1437.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1181.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1731.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5315.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1442.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5327.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5251.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1429.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1411.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0001/BToKee_PUMix_1030.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5317.root',
'root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_PUMix_18_03_18/180318_112206/0005/BToKee_PUMix_5320.root',
),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--filein nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECOSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:RECOSIM.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v12', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.eventinterpretaion_step = cms.Path(process.EIsequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.recosim_step,process.eventinterpretaion_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
