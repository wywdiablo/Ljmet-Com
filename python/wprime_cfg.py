import FWCore.ParameterSet.Config as cms
import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes

process = cms.Process("LJMetCom")

relBase    = str('/data1/speer/tblsm/cmssw/git-transition/new-git_5_3_6/')
############################################################
#
# FWLite application options
process.load('LJMet.Com.ljmet_cfi')
process.ljmet.isMc = cms.bool(True)
process.ljmet.excluded_calculators = cms.vstring(
                                                 #'WprimeCalc',
                                                 'DileptonCalc',
                                                 'StopCalc',
                                                 'PdfCalc',
                                                 'ChargedHiggsCalc',
                                                 'TprimeCalc'
                                                 )

# common calculator options
process.load('LJMet.Com.commonCalc_cfi')

# Stop calculator options
process.load('LJMet.Com.stopCalc_cfi')

# Wprime calculator options
process.load('LJMet.Com.wprimeCalc_cfi')
process.WprimeCalc.isWJets = cms.bool(False)

# LjetsTopoCalc options
process.load('LJMet.Com.ljetsTopoCalcNew_cfi')
process.LjetsTopoCalcNew.useBestTop = cms.bool(True)


############################################################
#
# Event selector options
#
process.event_selector = cms.PSet(
                                  
                                  selection = cms.string('WprimeSelector'),
                                  
                                  # cuts
                                  debug  = cms.bool(False),
                                  
                                  isMc  = cms.bool(True),
                                  doLaserCalFilt  = cms.bool(False),
                                  
                                  trigger_cut  = cms.bool(True),
                                  dump_trigger = cms.bool(False),
                                  
                                  mctrigger_path_el = cms.string('HLT_Ele30_CaloIdVT_TrkIdT_PFNoPUJet150_PFNoPUJet25_v9'),
                                  mctrigger_path_mu = cms.string('HLT_Mu40_eta2p1_v12'),
                                  trigger_path_el = cms.vstring('HLT_Ele27_WP80_v8','HLT_Ele27_WP80_v9','HLT_Ele27_WP80_v10','HLT_Ele27_WP80_v11'),
                                  trigger_path_mu = cms.vstring('HLT_IsoMu24_eta2p1_v11','HLT_IsoMu24_eta2p1_v12','HLT_IsoMu24_eta2p1_v13','HLT_IsoMu24_eta2p1_v14','HLT_IsoMu24_eta2p1_v15'),
                                  
                                  #testing muons
                                  #mctrigger_path_el = cms.string('HLT_Mu40_v12'),
                                  #mctrigger_path_mu = cms.string('HLT_Mu40_v12'),
                                  #trigger_path_el = cms.vstring('HLT_Mu40_v12'),
                                  #trigger_path_mu = cms.vstring('HLT_Mu40_v12'),
                                  
                                  pv_cut         = cms.bool(True),
                                  hbhe_cut       = cms.bool(True),
                                  
                                  jet_cuts                 = cms.bool(True),
                                  jet_minpt                = cms.double(30.0),
                                  jet_maxeta               = cms.double(2.4),
                                  min_jet                  = cms.int32(2),
                                  max_jet                  = cms.int32(4000),
                                  leading_jet_pt           = cms.double(50.0),
                                  
                                  muon_cuts                = cms.bool(True),
                                  tight_muon_minpt         = cms.double(26.0), # 26 GeV
                                  tight_muon_maxeta        = cms.double(2.1),
                                  loose_muon_minpt         = cms.double(10.0),
                                  loose_muon_maxeta        = cms.double(2.4),
                                  min_tight_muon           = cms.int32(0),
                                  
                                  electron_cuts                = cms.bool(True),
                                  tight_electron_minpt         = cms.double(30.0), # 30 GeV
                                  tight_electron_maxeta        = cms.double(2.5),
                                  loose_electron_minpt         = cms.double(20.0),
                                  loose_electron_maxeta        = cms.double(2.5),
                                  min_tight_electron           = cms.int32(0),
                                  
                                  min_tight_lepton         = cms.int32(1),
                                  max_tight_lepton         = cms.int32(1),
                                  trigger_consistent       = cms.bool(True),
                                  second_lepton_veto       = cms.bool(True),
                                  
                                  met_cuts                 = cms.bool(True),
                                  min_met                  = cms.double(20.0),
                                  
                                  btag_cuts                = cms.bool(True),
                                  btagger                  = cms.string('slimmedSecondaryVertices'),
                                  btag_min_discr           = cms.double(0.679),
                                  btag_1                   = cms.bool(True),
                                  btag_2                   = cms.bool(False),
                                  btag_3                   = cms.bool(False),
                                  
                                  BTagUncertUp             = cms.bool(False),
                                  BTagUncertDown           = cms.bool(False),
                                  JECup                    = cms.bool(False),
                                  JECdown                  = cms.bool(False),
                                  JERup                    = cms.bool(False),
                                  JERdown                  = cms.bool(False),
                                  JEC_txtfile = cms.string('../cond/Summer12_V2_DATA_AK5PF_UncertaintySources.txt'),
                                  trigger_collection       = cms.InputTag('TriggerResults::HLT'),
                                  pv_collection            = cms.InputTag('offlineSlimmedPrimaryVertices'),
                                  removeJetLepOverlap      = cms.bool(True),
                                  jet_collection           = cms.InputTag('slimmedJets'),
                                  muon_collection          = cms.InputTag('slimmedMuons'),
                                  electron_collection      = cms.InputTag('slimmedElectrons'),
                                  met_collection           = cms.InputTag('slimmedMETs'),
                                  type1corrmet_collection  = cms.InputTag(''),
                                  
                                  MCL1JetPar               = cms.string(relBase+'/src/LJMet/Com/data/START53_V7G_L1FastJet_AK5PFchs.txt'),
                                  MCL2JetPar               = cms.string(relBase+'/src/LJMet/Com/data/START53_V7G_L2Relative_AK5PFchs.txt'),
                                  MCL3JetPar               = cms.string(relBase+'/src/LJMet/Com/data/START53_V7G_L3Absolute_AK5PFchs.txt'),
                                  
                                  DataL1JetPar             = cms.string(relBase+'/src/LJMet/Com/data/FT_53_V10_AN3_L1FastJet_AK5PFchs.txt'),
                                  DataL2JetPar             = cms.string(relBase+'/src/LJMet/Com/data/FT_53_V10_AN3_L2Relative_AK5PFchs.txt'),
                                  DataL3JetPar             = cms.string(relBase+'/src/LJMet/Com/data/FT_53_V10_AN3_L3Absolute_AK5PFchs.txt'),
                                  DataResJetPar            = cms.string(relBase+'/src/LJMet/Com/data/FT_53_V10_AN3_L2L3Residual_AK5PFchs.txt')
                                  )


#######################################################
#
# Input files
#

process.inputs = cms.PSet (
                           nEvents    = cms.int32(100),
                           skipEvents = cms.int32(0),
                           lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange()),
                           fileNames  = cms.vstring(
                                                    [
                                                     'root://cmsxrootd.fnal.gov//store/mc/Spring14miniaod/SingletopWprime_M2000GeV_right_Tune4C_13TeV-comphep/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/2C794437-DF1E-E411-9467-0025901ACB64.root',
                                                     ]
                                                    )
                           )

#process.load(input_module)


# JSON
if (not process.ljmet.isMc==cms.bool(True)):
    JsonFile = 'data/json/Cert_190456-202016_8TeV_PromptReco_Collisions12_JSON_MuonPhys.txt'
    myList   = LumiList.LumiList(filename=JsonFile).getCMSSWString().split(',')
    process.inputs.lumisToProcess.extend(myList)


#######################################################
#
# Output
#
process.outputs = cms.PSet (
                            outputName = cms.string('ljmet_tree'),
                            treeName   = cms.string('ljmet'),
                            )


#######################################################
#
# Object selector options
#

# Primary vertex
process.load('PhysicsTools.SelectorUtils.pvSelector_cfi')
process.pvSelector.pvSrc   = cms.InputTag('offlineSlimmedPrimaryVertices')
process.pvSelector.minNdof = cms.double(4.0)
process.pvSelector.maxZ    = cms.double(24.0)
process.pvSelector.maxRho  = cms.double(2.0)

# Tight muon
process.load('LJMet.Com.pfMuonSelector_cfi') 

# Loose muon
process.looseMuonSelector = process.pfMuonSelector.clone()
process.looseMuonSelector.maxPfRelIso = cms.double(0.2)
process.looseMuonSelector.cutsToIgnore = cms.vstring('TrackerMuon',
                                                     'Chi2'
                                                     )

# electron
process.load('LJMet.Com.cutbasedIDSelector_cfi')

# loose electron
process.looseElectronSelector = process.cutbasedIDSelector.clone()
process.looseElectronSelector.version = cms.string('VETO')

# jets
process.load('PhysicsTools.SelectorUtils.pfJetIDSelector_cfi') 
process.pfJetIDSelector.version = cms.string('FIRSTDATA')
process.pfJetIDSelector.quality = cms.string('LOOSE')
