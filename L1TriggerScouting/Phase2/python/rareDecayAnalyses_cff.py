import FWCore.ParameterSet.Config as cms


hjpsigammaRecMesonStruct = cms.EDProducer("ScPhase2BosonToRecMesonGamma",
    srcMeson = cms.InputTag("recMesonStruct", "jpsi"),
    srcGamma = cms.InputTag("recIsoTkEmStruct"),
    minMassBoson = cms.double(100),
    maxMassBoson = cms.double(150),
    minPtQ = cms.double(30),
    minPtGamma = cms.double(30),
    analysisName = cms.string("HJPsiGamma")
)

h2phiRecMesonStruct = cms.EDProducer("ScPhase2BosonTo2RecMeson",
    srcMeson1 = cms.InputTag("recMesonStruct", "phi"),
    srcMeson2 = cms.InputTag("recMesonStruct", "phi"),
    minMassBoson = cms.double(100),
    maxMassBoson = cms.double(150),
    minPtQ = cms.double(1),
    maxIso = cms.double(0.25),
    analysisName = cms.string("H2Phi")
)

hphigammaRecMesonStruct = cms.EDProducer("ScPhase2BosonToRecMesonGamma",
    srcMeson = cms.InputTag("recMesonStruct", "phi"),
    srcGamma = cms.InputTag("recIsoTkEmStruct"),
    minMassBoson = cms.double(100),
    maxMassBoson = cms.double(150),
    minPtQ = cms.double(30),
    minPtGamma = cms.double(30),
    analysisName = cms.string("HPhiGamma")
)

hphijpsiRecMesonStruct = cms.EDProducer("ScPhase2BosonTo2RecMeson",
    srcMeson1 = cms.InputTag("recMesonStruct", "phi"),
    srcMeson2 = cms.InputTag("recMesonStruct", "jpsi"),
    minMassBoson = cms.double(100),
    maxMassBoson = cms.double(150),
    minPtQ = cms.double(30),
    maxIso = cms.double(0.25),
    analysisName = cms.string("HPhiJPsi")
)

h2rhoRecMesonStruct = cms.EDProducer("ScPhase2BosonTo2RecMeson",
    srcMeson1 = cms.InputTag("recMesonStruct", "rho"),
    srcMeson2 = cms.InputTag("recMesonStruct", "rho"),
    minMassBoson = cms.double(100),
    maxMassBoson = cms.double(150),
    minPtQ = cms.double(3),
    maxIso = cms.double(0.25),
    analysisName = cms.string("H2Rho")
)

hrhogammaRecMesonStruct = cms.EDProducer("ScPhase2BosonToRecMesonGamma",
    srcMeson = cms.InputTag("recMesonStruct", "rho"),
    srcGamma = cms.InputTag("recIsoTkEmStruct"),
    minMassBoson = cms.double(100),
    maxMassBoson = cms.double(150),
    minPtQ = cms.double(30),
    minPtGamma = cms.double(30),
    analysisName = cms.string("HRhoGamma")
)

z2phiRecMesonStruct = cms.EDProducer("ScPhase2BosonTo2RecMeson",
    srcMeson1 = cms.InputTag("recMesonStruct", "phi"),
    srcMeson2 = cms.InputTag("recMesonStruct", "phi"),
    minMassBoson = cms.double(60),
    maxMassBoson = cms.double(120),
    minPtQ = cms.double(1),
    maxIso = cms.double(0.25),
    analysisName = cms.string("Z2Phi")
)

z2rhoRecMesonStruct = cms.EDProducer("ScPhase2BosonTo2RecMeson",
    srcMeson1 = cms.InputTag("recMesonStruct", "rho"),
    srcMeson2 = cms.InputTag("recMesonStruct", "rho"),
    minMassBoson = cms.double(60),
    maxMassBoson = cms.double(120),
    minPtQ = cms.double(3),
    maxIso = cms.double(0.25),
    analysisName = cms.string("Z2Rho")
)

w3piStruct = cms.EDProducer("ScPhase2PuppiW3PiDemo",
    src = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
)

wdsgStruct = cms.EDProducer("ScPhase2PuppiWDsGammaDemo",
    srcPuppi = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
    srcTkEm = cms.InputTag("scPhase2TkEmRawToDigiStruct"),
)

wpigStruct = cms.EDProducer("ScPhase2PuppiWPiGammaDemo",
    srcPuppi = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
    srcTkEm = cms.InputTag("scPhase2TkEmRawToDigiStruct"),
)

hrhogStruct = cms.EDProducer("ScPhase2PuppiHRhoGammaDemo",
    srcPuppi = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
    srcTkEm = cms.InputTag("scPhase2TkEmRawToDigiStruct"),
)

hphigStruct = cms.EDProducer("ScPhase2PuppiHPhiGammaDemo",
    srcPuppi = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
    srcTkEm = cms.InputTag("scPhase2TkEmRawToDigiStruct"),
)

hjpsigStruct = cms.EDProducer("ScPhase2PuppiHJPsiGammaDemo",
    srcPuppi = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
    srcTkEm = cms.InputTag("scPhase2TkEmRawToDigiStruct"),
)

h2rhoStruct = cms.EDProducer("ScPhase2PuppiH2RhoDemo",
    src = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
)

h2phiStruct = cms.EDProducer("ScPhase2PuppiH2PhiDemo",
    src = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
)

hphijpsiStruct = cms.EDProducer("ScPhase2PuppiHPhiJPsiDemo",
    src = cms.InputTag("scPhase2PuppiRawToDigiStruct"),
)