{

  //gROOT->ProcessLine(".exception");

  gROOT->ProcessLine(".L tools.C+g");

  // Link JEC libraries that are modified to work stand-alone
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/Utilities.cc+");
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/JetCorrectorParameters.cc+");
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/SimpleJetCorrector.cc+");
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/FactorizedJetCorrector.cc+");

  gROOT->ProcessLine(".L compareLiteHLT.C+g");
  //gROOT->ProcessLine(".L drawCompareLite.C+g");

  compareLiteHLT("2022F");
  //drawCompareLite("2022F");
}
