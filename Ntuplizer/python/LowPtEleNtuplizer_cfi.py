import FWCore.ParameterSet.Config as cms

LowPtEleNtuplizer = cms.EDAnalyzer("LowPtEleNtuplizer",
                                   hepMCProductLabel = cms.InputTag("generatorSmeared"),
                                   genParticlesLabel = cms.InputTag("genParticles"),
                                   generalTracksLabel = cms.InputTag("generalTracks"),
                                   gsfTracksLabel = cms.InputTag("electronGsfTracks"),
                                   #seedElectronsLabel = cms.InputTag("electronMergedSeeds"),
                                   gsfElectronsLabel = cms.InputTag("gedGsfElectrons"),
                                   recoMuonsLabel = cms.InputTag("muons"),
                                   )
