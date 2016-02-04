import FWCore.ParameterSet.Config as cms

l1CaloScales = cms.ESProducer("L1ScalesTrivialProducer",

    L1CaloEmEtScaleLSB = cms.double(0.25),

    L1CaloRegionEtScaleLSB = cms.double(0.25),

    L1CaloEmThresholds = cms.vdouble(
      0.0, 1.0, 2.0, 3.0, 4.0, 
      5.0, 6.0, 7.0, 8.0, 9.0, 
      10.0, 11.0, 12.0, 13.0, 14.0, 
      15.0, 16.0, 17.0, 18.0, 19.0, 
      20.0, 21.0, 22.0, 23.0, 24.0, 
      25.0, 26.0, 27.0, 28.0, 29.0, 
      30.0, 31.0, 32.0, 33.0, 34.0, 
      35.0, 36.0, 37.0, 38.0, 39.0, 
      40.0, 41.0, 42.0, 43.0, 44.0, 
      45.0, 46.0, 47.0, 48.0, 49.0, 
      50.0, 51.0, 52.0, 53.0, 54.0, 
      55.0, 56.0, 57.0, 58.0, 59.0, 
      60.0, 61.0, 62.0, 63.0
    ),

    L1CaloJetThresholds = cms.vdouble(
      0.0, 10.0, 12.0, 14.0, 15.0, 
      18.0, 20.0, 22.0, 24.0, 25.0, 
      28.0, 30.0, 32.0, 35.0, 37.0, 
      40.0, 45.0, 50.0, 55.0, 60.0, 
      65.0, 70.0, 75.0, 80.0, 85.0, 
      90.0, 100.0, 110.0, 120.0, 125.0, 
      130.0, 140.0, 150.0, 160.0, 170.0, 
      175.0, 180.0, 190.0, 200.0, 215.0, 
      225.0, 235.0, 250.0, 275.0, 300.0, 
      325.0, 350.0, 375.0, 400.0, 425.0, 
      450.0, 475.0, 500.0, 525.0, 550.0, 
      575.0, 600.0, 625.0, 650.0, 675.0, 
      700.0, 725.0, 750.0, 775.0
    ),

    L1HtMissThresholds = cms.vdouble(
      0.0, 2.0, 4.0, 6.0, 8.0,
      10.0, 12.0, 14.0, 16.0, 18.0,
      20.0, 22.0, 24.0, 26.0, 28.0,
      30.0, 32.0, 34.0, 36.0, 38.0,
      40.0, 42.0, 44.0, 46.0, 48.0,
      50.0, 52.0, 54.0, 56.0, 58.0,
      60.0, 62.0, 64.0, 66.0, 68.0,
      70.0, 72.0, 74.0, 76.0, 78.0,
      80.0, 82.0, 84.0, 86.0, 88.0,
      90.0, 92.0, 94.0, 96.0, 98.0,
      100.0, 102.0, 104.0, 106.0, 108.0,
      110.0, 112.0, 114.0, 116.0, 118.0,
      120.0, 122.0, 124.0, 126.0, 128.0,
      130.0, 132.0, 134.0, 136.0, 138.0,
      140.0, 142.0, 144.0, 146.0, 148.0,
      150.0, 152.0, 154.0, 156.0, 158.0,
      160.0, 162.0, 164.0, 166.0, 168.0,
      170.0, 172.0, 174.0, 176.0, 178.0,
      180.0, 182.0, 184.0, 186.0, 188.0,
      190.0, 192.0, 194.0, 196.0, 198.0,
      200.0, 202.0, 204.0, 206.0, 208.0,
      210.0, 212.0, 214.0, 216.0, 218.0,
      220.0, 222.0, 224.0, 226.0, 228.0,
      230.0, 232.0, 234.0, 236.0, 238.0,
      240.0, 242.0, 244.0, 246.0, 248.0,
      250.0, 252.0, 254.0
    ),

    L1HfRingThresholds = cms.vdouble(
      0.0, 2.0, 3.0, 4.0, 6.0, 50., 200., 500. 
    )

)


