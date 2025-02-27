// system include files
#include <memory>
#include <sys/stat.h>
#include <map>
#include <utility>
#include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelCalibConfiguration.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelGainCalibration.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelGainCalibrationOffline.h"
#include "CondFormats/SiPixelObjects/interface/SiPixelGainCalibrationForHLT.h"
#include "CalibTracker/SiPixelESProducers/interface/SiPixelGainCalibrationService.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "CalibTracker/SiPixelESProducers/interface/SiPixelGainCalibrationOfflineService.h"
#include "CalibTracker/SiPixelESProducers/interface/SiPixelGainCalibrationForHLTService.h"
#include "CalibTracker/SiPixelESProducers/interface/SiPixelGainCalibrationServiceBase.h"
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h"
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

#include "TH2F.h"
#include "TFile.h"
#include "TDirectory.h"
#include "TKey.h"
#include "TString.h"
#include "TList.h"

class SiPixelGainCalibrationRejectNoisyAndDead : public edm::one::EDAnalyzer<> {
public:
  explicit SiPixelGainCalibrationRejectNoisyAndDead(const edm::ParameterSet &);
  ~SiPixelGainCalibrationRejectNoisyAndDead() override;

private:
  edm::ParameterSet conf_;
  edm::ESGetToken<TrackerGeometry, TrackerDigiGeometryRecord> pddToken_;
  SiPixelGainCalibrationOfflineService SiPixelGainCalibrationOfflineService_;
  //SiPixelGainCalibrationForHLTService SiPixelGainCalibrationService_;
  SiPixelGainCalibrationOffline *theGainCalibrationDbInputOffline_;

  SiPixelGainCalibrationForHLTService SiPixelGainCalibrationForHLTService_;
  SiPixelGainCalibrationForHLT *theGainCalibrationDbInputForHLT_;

  void analyze(const edm::Event &, const edm::EventSetup &) override;

  std::map<int, std::vector<std::pair<int, int> > > noisypixelkeeper;
  std::map<int, std::vector<std::pair<int, int> > > insertednoisypixel;
  int nnoisyininput;

  void fillDatabase(const edm::EventSetup &);
  void getNoisyPixels();
  void getDeadPixels();

  // ----------member data ---------------------------

  std::string noisypixellist_;
  int insertnoisypixelsindb_;
  std::string record_;
  bool DEBUG;
  float pedlow_;
  float pedhi_;
  float gainlow_;
  float gainhi_;
};
