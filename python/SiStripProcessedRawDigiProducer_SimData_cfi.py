import FWCore.ParameterSet.Config as cms

#defaults as in SiStripZeroSuppression_cfi.py
siStripProcessedRawDigis = cms.EDProducer("SiStripProcessedRawDigiProducer",
                                          DigiProducersList = cms.VInputTag( cms.InputTag('mix', 'simSiStripDigisZeroSuppressed'),
                                                                             cms.InputTag('mix', 'simSiStripDigisVirginRaw'), 
                                                                             cms.InputTag('mix', 'simSiStripDigisProcessedRaw'),
                                                                             cms.InputTag('mix', 'simSiStripDigisScopeMode')
                                                                             ),
                                          CommonModeNoiseSubtractionMode = cms.string('Median'), 
                                          #CutToAvoidSignal = cms.double(3.0), ##This is just for CMNSub...Mode TT6
                                          )
