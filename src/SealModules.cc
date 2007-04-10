
#include "FWCore/PluginManager/interface/ModuleDef.h"

#include "FWCore/Framework/interface/MakerMacros.h"

#include "AnalysisAlgos/SiStripClusterInfoProducer/interface/SiStripClusterInfoProducer.h"
#include "AnalysisAlgos/SiStripClusterInfoProducer/interface/SiStripFakeRawDigiModule.h"

using cms::SiStripClusterInfoProducer;

DEFINE_SEAL_MODULE();
DEFINE_ANOTHER_FWK_MODULE(SiStripClusterInfoProducer);
DEFINE_ANOTHER_FWK_MODULE(SiStripFakeRawDigiModule);
