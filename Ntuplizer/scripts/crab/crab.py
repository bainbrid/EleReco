from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName     = 'LowPtEle_2GeV'
config.General.workArea        = 'LowPtEle_2GeV'
config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.pluginName = 'ANALYSIS'
config.JobType.psetName   = 'RECOSIM_cfg.py'
config.JobType.outputFiles = ['RECOSIM.root']

config.Data.inputDataset         = '/BToKee_Pythia/tstreble-BToKee_Pythia_PUMix_18_03_18-c9b9e020b5bce5ee6bee9ef5f38c415a/USER'
config.Data.inputDBS             = 'phys03'
config.Data.splitting            = 'FileBased'#Automatic,EventAwareLumiBased
config.Data.unitsPerJob          = 1
config.Data.totalUnits           = -1
config.Data.outLFNDirBase        = '/store/user/%s/'%(getUsernameFromSiteDB())
config.Data.publication          = False
config.Data.outputDatasetTag     = 'LowPtEle_2GeV'

config.Site.whitelist   = ["T2_UK_London_IC"]
config.Site.storageSite = 'T2_UK_London_IC'
