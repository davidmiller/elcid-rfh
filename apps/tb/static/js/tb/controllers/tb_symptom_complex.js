angular.module('opal.controllers').controller('TbSymptomComplexCrtl',
  function(step, scope, episode, recordLoader, $window) {
    if(!scope.editing.symptom_complex){
      scope.editing.symptom_complex = {};
    }

     if(_.isArray(scope.editing.symptom_complex)){
       scope.editing.symptom_complex = _.first(scope.editing.symptom_complex);
     }

     if(!scope.editing.symptom_complex.symptoms){
       scope.editing.symptom_complex.symptoms = [];
     }

    scope.tbSymptomFields = {
      "chills": "Chills",
      "cough (dry)": "Cough (Dry)",
      "cough (productive)": "Cough (Productive)",
      "dysponea": "Dysponea",
      "fatigue": "Fatigue",
      "fever": "Fever",
      "haemoptysis": "Haemoptysis",
      "loss_of_appetite": "Loss of Appetite",
      "night_sweats": "Night Sweats",
      "weight_loss": "Weight Loss"
    };
    scope.tbSymptom = {};

    var tbValues = _.keys(scope.tbSymptomFields);

    column1 = tbValues.slice(0, tbValues.length/2);
    column2 = tbValues.slice(tbValues.length/2);
    scope.columns = [column1, column2];

    scope.updateTbSymptoms = function(){
      var symptoms = scope.editing.symptom_complex.symptoms;

      var relevent = _.intersection(_.values(scope.tbSymptomFields), symptoms);

      _.each(scope.tbSymptomFields, function(v, k){
        var toAdd = _.contains(relevent, v);

        if(scope.tbSymptom[k]){
          scope.tbSymptom[k] = toAdd;
        }
        else if(!scope.tbSymptom[k] && toAdd){
          scope.tbSymptom[k] = toAdd;
        }
      });
    };

    scope.updateTbSymptoms();

    scope.updateSymptoms = function(symptomField){
      var symptoms = scope.editing.symptom_complex.symptoms || [];

      var symptomValue = scope.tbSymptomFields[symptomField]
      var inSymptoms = _.find(symptoms, function(x){
         return x === symptomValue;
      });
      var toAdd = scope.tbSymptom[symptomField];

      if(!inSymptoms && toAdd){
        symptoms.push(symptomValue);
      }
      else if(inSymptoms && !toAdd){
        symptoms = _.filter(symptoms, function(x){
            return x !== symptomValue;
        });

        scope.editing.symptom_complex.symptoms = symptoms;
      }
    };

    scope.preSave = function(editing){
      if(!editing.symptom_complex.symptoms.length){
         delete editing.symptom_complex;
      }
    }
});
