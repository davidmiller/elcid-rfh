angular.module('opal.services').factory('DemographicsSearch', function($q, $http, $window, Patient) {
  "use strict";
  /*
  * The demographics search used by the find patient
  * pathway.
  */

  var url = '/elcid/v0.1/demographics_search/';

  // we have four call backs that we are expecting

  // patient is found in elcid (Yay!)
  var PATIENT_FOUND_IN_ELCID = "patient_found_in_elcid";

  // patient is not found in elcid but is found
  // in the hospital (Yay!)
  var PATIENT_FOUND_IN_HOSPITAL = "patient_found_in_hospital";

  // patient is not found
  var PATIENT_NOT_FOUND = "patient_not_found";

  // fail (Boo!)
  var error = "error"

  var expectedCallbacks = [
    PATIENT_FOUND_IN_ELCID,
    PATIENT_FOUND_IN_HOSPITAL,
    PATIENT_NOT_FOUND,
  ]

  var find = function(hospitalNumber, findPatientOptions){
    _.keys(findPatientOptions, function(key){
      if(expectedCallbacks.indexOf(key) === -1){
        throw "unknown call back";
      }
    });
    var patientUrl = url + hospitalNumber + "/"
    $http.get(patientUrl).then(function(response) {
      if(response.data.status == PATIENT_FOUND_IN_ELCID){
        findPatientOptions[PATIENT_FOUND_IN_ELCID](response.data.patient);
      }
      else if(response.data.status == PATIENT_FOUND_IN_HOSPITAL){
        findPatientOptions[PATIENT_FOUND_IN_HOSPITAL](response.data.patient);
      }
      else if(response.data.status == PATIENT_NOT_FOUND){
        findPatientOptions[PATIENT_NOT_FOUND](response.data.patient);
      }
      else{
        $window.alert('DemographicsSearch could not be loaded');
      }
    }, function(){
      $window.alert('DemographicsSearch could not be loaded');
    });
  }

  return {
    find: find
  };
});