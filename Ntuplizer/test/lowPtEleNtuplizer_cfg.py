import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
from EleReco.Ntuplizer.files_RERECO import *
>
process = cms.Process("Ntuplizer")

options = VarParsing.VarParsing('analysis')
process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True))
options.parseArguments()

sample = 0 #@@ choose preexisting samples here

files = [
    options.inputFiles,
    BToKee_2GeV,
    BToKee_1GeV,
    BToKee_0p5GeV,
    BToKmm_0p5GeV,
    ][sample]
output = [options.outputFile,
          'output_BToKee_2GeV.root',
          'output_BToKee_1GeV.root',
          'output_BToKee_0p5GeV.root',
          'output_BToKmm_0p5GeV.root'
          ][sample]

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(*files)
                            )

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.load('EleReco.Ntuplizer.lowPtEleNtuplizer_cfi')
process.p = cms.Path(process.lowPtEleNtuplizer)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000 # silence output

process.TFileService=cms.Service('TFileService',
                                 fileName=cms.string(output)
                                 )
