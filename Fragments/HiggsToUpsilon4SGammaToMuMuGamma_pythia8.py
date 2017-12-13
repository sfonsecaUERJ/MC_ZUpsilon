import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                                 comEnergy = cms.double(13000.0),
                                 crossSection = cms.untracked.double(8.45E-6),
                                 filterEfficiency = cms.untracked.double(1.0),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 pythiaPylistVerbosity = cms.untracked.int32(0),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 PythiaParameters = cms.PSet(

    pythia8CommonSettingsBlock,
    pythia8CUEP8M1SettingsBlock,
    processParameters = cms.vstring(
      'Main:timesAllowErrors    = 10000',
      'HiggsSM:all=true',
      '300553:new = 300553 Upsilon(4S) 3 0 0 1.0579400e+01 0.0205 10.4769 10.6819 0.0000000e+00',
      #particle: id="200553" name="Upsilon(3S)" spinType="3" chargeType="0" colType="0" m0="10.3552" mWidth="0.00002" mMin="10.3552" mMax="10.3552"   
      '300553:addChannel = 1 0.96  0  511   -511', # BBbar
      '300553:addChannel = 1 0.514 0  521   -521', # B+B-
      '25:m0 = 125.0',
      '25:onMode = off',
      '25:addChannel = 1  1.00   103   22   300553',
      '300553:onMode = off',
      '300553:addChannel = 1 1. 0 13 -13',
      ),

    parameterSets = cms.vstring(
      'pythia8CommonSettings',
      'pythia8CUEP8M1Settings',
      'processParameters')
    )
                                 )
ProductionFilterSequence = cms.Sequence(generator)
