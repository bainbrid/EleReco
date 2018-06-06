import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from EleReco.Ntuplizer.files_RERECO import *

process = cms.Process("Ntuplizer")

options = VarParsing.VarParsing('analysis')
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
options.parseArguments()

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000 # silence output

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(options.inputFiles)
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.dummy = cms.EDAnalyzer("NonAnalyzer")

process.p = cms.Path(process.dummy)

process.load("Configuration.EventContent.EventContent_cff")
process.out = cms.OutputModule("PoolOutputModule",
                               process.RECOSIMEventContent,
                               fileName = cms.untracked.string(options.outputFile)
                               )

process.ep = cms.EndPath(process.out)
