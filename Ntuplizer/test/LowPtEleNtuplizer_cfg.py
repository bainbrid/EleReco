import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from files_RERECO import *

process = cms.Process("Ntuplizer")

sample = 0 #@@ choose here

files = [
    ['root://cms-xrd-global.cern.ch//store/user/tstreble/BToKee_Pythia/BToKee_Pythia_AODSIM_18_03_22/180321_162718/0000/BToKee_AODSIM_246.root'],
    BToKee_2GeV,
    BToKee_1GeV,
    BToKee_0p5GeV,
    BToKmm_0p5GeV,
    ][sample]
output = ['output.root',
          'output_BToKee_2GeV.root',
          'output_BToKee_1GeV.root',
          'output_BToKee_0p5GeV.root',
          'output_BToKmm_0p5GeV.root'
          ][sample]

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(*files)
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

options = VarParsing.VarParsing('analysis')
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
options.parseArguments()

#process.dummy = cms.EDAnalyzer("NonAnalyzer")
process.load('EleReco.Ntuplizer.LowPtEleNtuplizer_cfi')
process.p = cms.Path(process.LowPtEleNtuplizer)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000 # silence output

process.TFileService=cms.Service('TFileService',
                                 fileName=cms.string(output)
                                 )
