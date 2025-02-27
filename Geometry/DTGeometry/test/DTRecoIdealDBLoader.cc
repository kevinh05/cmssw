#include "FWCore/Framework/interface/one/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "CondCore/DBOutputService/interface/PoolDBOutputService.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESTransientHandle.h"
#include "CondFormats/RecoGeometryObjects/interface/RecoIdealGeometry.h"
#include "Geometry/DTGeometryBuilderinterface/DTGeometryParsFromDD.h"
#include "Geometry/Records/interface/RecoIdealGeometryRcd.h"
#include "Geometry/Records/interface/MuonGeometryRecord.h"
#include "DetectorDescription/Core/interface/DDCompactView.h"
#include "Geometry/Records/interface/MuonNumberingRecord.h"
#include "Geometry/MuonNumbering/interface/MuonDDDConstants.h"

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>

class DTRecoIdealDBLoader : public edm::one::EDAnalyzer<> {
public:
  explicit DTRecoIdealDBLoader(const edm::ParameterSet& iConfig);
  ~DTRecoIdealDBLoader();

  void beginJob() override;
  void analyze(edm::Event const& iEvent, edm::EventSetup const&) override;
  void endJob() override;

private:
  const std::string label_;
  const edm::ESGetToken<DTGeometry, MuonGeometryRecord> tokDT_;
  const edm::ESGetToken<DDCompactView, IdealGeometryRecord> tokDDD_;
  int rotNumSeed_;
};

using namespace std;

DTRecoIdealDBLoader::DTRecoIdealDBLoader(const edm::ParameterSet& iConfig)
    : label_(),
      tokDT_{esConsumes<DTGeometry, MuonGeometryRecord>(edm::ESInputTag{})},
      tokDDD_{esConsumes<DDCompactView, IdealGeometryRecord>(edm::ESInputTag{"", label_})} {
  std::cout << "DTRecoIdealDBLoader::DTRecoIdealDBLoader" << std::endl;
}

DTRecoIdealDBLoader::~DTRecoIdealDBLoader() { std::cout << "DTRecoIdealDBLoader::~DTRecoIdealDBLoader" << std::endl; }

void DTRecoIdealDBLoader::analyze(const edm::Event& evt, const edm::EventSetup& es) {
  std::cout << "DTRecoIdealDBLoader::beginJob" << std::endl;
  RecoIdealGeometry* rig = new RecoIdealGeometry;

  edm::Service<cond::service::PoolDBOutputService> mydbservice;
  if (!mydbservice.isAvailable()) {
    std::cout << "PoolDBOutputService unavailable" << std::endl;
    return;
  }

  const DDCompactView& cpv = es.getData(tokDDD_);
  const auto& pMNDC = &es.getData(tokDT_);
  DTGeometryParsFromDD dtgp;

  dtgp.build(&cpv, *pMNDC, *rig);
  std::cout << "RecoIdealGeometry " << rig->size() << std::endl;

  if (mydbservice->isNewTagRequest("RecoIdealGeometryRcd")) {
    cout << "mydbservice " << mydbservice->beginOfTime() << " to " << mydbservice->endOfTime() << endl;
    mydbservice->createNewIOV<RecoIdealGeometry>(
        rig, mydbservice->beginOfTime(), mydbservice->endOfTime(), "RecoIdealGeometryRcd");
  } else {
    std::cout << "RecoIdealGeometryRcd Tag is already present." << std::endl;
  }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DTRecoIdealDBLoader);
