import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         #crossSection = cms.untracked.double(1256000.0),
                         comEnergy = cms.double(13000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
      'HiggsSM:ffbar2H =true',
      '300553:new = 300553 Upsilon(4S) 3 0 0 1.0579400e+01 0.0000205 10.4769 10.6819 0.0000000e+00',
      '300553:addChannel = 1 0.96  0  511   -511', # BBbar
      '300553:addChannel = 1 0.514 0  521   -521', # B+B-
      '25:m0 = 91.187600000001', #don't know why, but the Higgs mass can't be the same of Z0
      '25:mWidth = 2.49520',
      '25:mMin = 10.00000',
      '25:mMax = 0.00000',
      '25:spinType = 3', #(4S+1)
      '25:onMode = off',
      '25:addChannel = 1  1.00   103   22   300553',
      '25:onIfMatch = 22 300553',
      '300553:onMode = off',    # ignore cross-section re-weighting (CSAMODE=6) since selecting wanted decay mode 
      '300553:addChannel = 1 1.0 0 13 -13',
      '300553:onIfAny = 13',
            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )

oniafilter = cms.EDFilter("PythiaFilter",
    Status = cms.untracked.int32(2),
    MaxEta = cms.untracked.double(1000.0),
    MinEta = cms.untracked.double(-1000.0),
    MinPt = cms.untracked.double(0.0),
    ParticleID = cms.untracked.int32(300553)
)

mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(2.7, 2.7),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

mugenfilter = cms.EDFilter("MCSingleParticleFilter",
    Status = cms.untracked.vint32(1,1),
    MinPt = cms.untracked.vdouble(10.0,10.0),
    ParticleID = cms.untracked.vint32(13,-13),
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter*mugenfilter)

