{

  //gROOT->ProcessLine(".exception");

  gROOT->ProcessLine(".L tools.C+g");

  // Link JEC libraries that are modified to work stand-alone
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/Utilities.cc+");
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/JetCorrectorParameters.cc+");
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/SimpleJetCorrector.cc+");
  gROOT->ProcessLine(".L CondFormats/JetMETObjects/src/FactorizedJetCorrector.cc+");

  gROOT->ProcessLine(".L compareLite.C+g");
  gROOT->ProcessLine(".L drawCompareLite.C+g");

  //compareLite("TEST");
  
  //compareLite("2022C");
  //compareLite("2022D");
  //compareLite("2022E");
  //compareLite("2022F");
  //compareLite("2022G");
  //compareLite("2023Cv123");
  //compareLite("2023Cv4");
  //compareLite("2023D");
  //compareLite("2024B");

  /*
  drawCompareLite("2022CD_v2");
  drawCompareLite("2022E_v2");
  drawCompareLite("2022FG_v2");
  drawCompareLite("2022F_v2");
  drawCompareLite("2022G_v2");
  drawCompareLite("2023Cv123_v2");
  drawCompareLite("2023Cv4_v2");
  drawCompareLite("2023D_v2");
  drawCompareLite("Run3_v2");
  */
  drawCompareLite("2024B");
  
  // hadd compareLite_Run3.root compareLite_2022CD.root compareLite_2022E.root compareLite_2022FG.root compareLite_2023Cv123.root compareLite_2023Cv4.root compareLite_2023D.root

  /*
  drawCompareLiteIOVs();
  */
}
