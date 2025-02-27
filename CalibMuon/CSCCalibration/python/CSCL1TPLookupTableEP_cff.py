import FWCore.ParameterSet.Config as cms

CSCL1TPLookupTableEP = cms.ESSource(
    "CSCL1TPLookupTableEP",
    ## CCLUT
    positionLUTFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat0_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat1_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat2_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat3_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodePosOffsetLUT_pat4_v1.txt"
    ),
    slopeLUTFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat0_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat1_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat2_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat3_v1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/CCLUT/CSCComparatorCodeSlopeLUT_pat4_v1.txt"
    ),
    ## convert pad number to 1/2-strip in ME1a
    padToHsME1aFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1a_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1a_odd.txt",
    ),
    ## convert pad number to 1/2-strip in ME1b
    padToHsME1bFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1b_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME1b_odd.txt",
    ),
    ## convert pad number to 1/2-strip in ME21
    padToHsME21Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_hs_ME21_odd.txt",
    ),
    ## convert pad number to 1/8-strip in ME1a
    padToEsME1aFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1a_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1a_odd.txt",
    ),
    ## convert pad number to 1/8-strip in ME1b
    padToEsME1bFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1b_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME1b_odd.txt",
    ),
    ## convert pad number to 1/8-strip in ME21
    padToEsME21Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_pad_es_ME21_odd.txt",
    ),
    ## convert eta partition to minimum wiregroup in ME11
    rollToMinWgME11Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME11_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME11_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME11_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME11_odd.txt",
    ),
    ## convert eta partition to maximum wiregroup in ME11
    rollToMaxWgME11Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME11_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME11_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME11_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME11_odd.txt",
    ),
     ## convert eta partition to minimum wiregroup in ME21
    rollToMinWgME21Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_min_wg_ME21_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_min_wg_ME21_odd.txt",
    ),
    ## convert eta partition to maximum wiregroup in ME21
    rollToMaxWgME21Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l1_max_wg_ME21_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/CoordinateConversion/GEMCSCLUT_roll_l2_max_wg_ME21_odd.txt",
    ),
    # lookup tables for the GEM-CSC slope correction
    gemCscSlopeCorrectionFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_even_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_even_GE11_layer2.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_odd_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCSlopeCorr_ME11_odd_GE11_layer2.txt",
    ),
    # lookup tables for the GEM-CSC slope correction
    gemCscSlopeCosiFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_even_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_odd_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_even_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_odd_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_even_GE11_layer2.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_2to1_SlopeShift_ME11_odd_GE11_layer2.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_even_GE11_layer2.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/CSCconsistency_3to1_SlopeShift_ME11_odd_GE11_layer2.txt",
    ),
    # lookup tables for the GEM-CSC slope correction
    gemCscSlopeCosiCorrectionFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_even_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_even_GE11_layer2.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_odd_GE11_layer1.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/SlopeCorrection/FacingChambers/GEMCSCconsistentSlopeCorr_ME11_odd_GE11_layer2.txt",
    ),
    # convert differences in 1/8-strip numbers between GEM and CSC to Run-3 slopes
    esDiffToSlopeME1aFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1a_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1a_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1a_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1a_odd.txt",
    ),
    esDiffToSlopeME1bFiles = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1b_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME1b_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1b_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME1b_odd.txt",
    ),
    esDiffToSlopeME21Files = cms.vstring(
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L1_ME21_odd.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME21_even.txt",
        "L1Trigger/CSCTriggerPrimitives/data/GEMCSC/BendingAngle/GEMCSCLUT_es_diff_slope_L2_ME21_odd.txt",
    ),
   )
