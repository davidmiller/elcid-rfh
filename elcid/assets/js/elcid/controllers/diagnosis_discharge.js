//
// This is the controller for elCID episodes that have a
// presenting complaint/final diagnosis pair.
//
// We do the standard discharge, then ask some more questions.
//
controllers.controller(
    'DiagnosisDischargeCtrl',
    function(
        $scope, $rootScope, $modalInstance, $modal, $q,
        $location,
        growl,
        Flow,
        tags, schema, options, episode, DischargePatientService){

        $scope.tags = tags;
        $scope.episode = episode;

        var steps = [
          "diagnosis"
        ];

        $scope.steps_details = {
            discharge: {
                icon: "fa fa-street-view",
                title: "Discharge",
                subtitle: undefined
            },
            diagnosis: {
                icon: "fa fa-stethoscope",
                title: "Diagnosis",
                subtitle: undefined
            },
            antimicrobial: {
                icon: "fa fa-flask",
                title: "Antimicrobial",
                subtitle: "Please enter the <strong>drug name</strong> and the <strong>start and end dates</strong> or state that the patient was <strong>not on antimicrobials</strong>."
            },
            travel: {
                icon: "fa fa-plane",
                title: "Travel",
                subtitle: "Please enter a <strong>travel destination</strong> and <strong>dates</strong>, or state that the patient <strong>did not travel</strong>."
            },
            consultant_at_discharge: {
                icon: "fa fa-user-md",
                title: "Consultant At Discharge",
                subtitle: "Please record the <strong>consultant</strong> at discharge."
            }
        };

        var dischargePatientService = new DischargePatientService();

        /*
        * a multi step model that acts a bit like a form controller for travel,
        * antimicrobial and symptoms
        */
        var MultiStep = function(requiredFields, negationField, editing, episode, columnName){
            this.none = false;
            this.warning = false;

            this.remove = function(index){
              editing[columnName].splice(index, 1);
              episode[columnName].splice(index, 1);
            };

            this.getRequiredFields = function(antimicrobial){
                return _.map(requiredFields, function(r){
                    return antimicrobial[r];
                });
            };

            this.pristine = function(antimicrobial){
              return !_.some(this.getRequiredFields(antimicrobial));
            };

            this.clear = function(){
              if(this.none){
                newAntimicrobial = episode.newItem(columnName);
                episode[columnName] = [newAntimicrobial];
                editing[columnName] = [newAntimicrobial.makeCopy()];
                editing[columnName][0][negationField] = true;
              }
              this.warning = false;
            };

            this.validate = function(antimicrobial){
              var requiredAll = this.getRequiredFields(antimicrobial);
              return _.every(requiredAll) || this.none;
            };

            // validates a whole step, e.g. all of the antimicrobial
            this.validateStep = function(){
              var toReview = $scope.editing[columnName];

              // if there's just an empty form at the end, lets ignore that
              if(toReview > 1){
                  if(this.pristine(toReview)){
                      toReview = _.first(toReview, toReview.length-1);
                  }
              }

              var invalidModels = _.filter(toReview, function(a){
                  return !this.validate(a);
              }, this);

              if(invalidModels.length){
                this.warning = true;
                return false;
              }

              return true;
            };

            this.addAnother = function(model){
                if(!this.validate(model)){
                    this.warning=true;
                }
                else{
                    if(!this.none){
                        model.submitted=true;
                        var newModel = episode.newItem(columnName);
                        episode[columnName].push(newModel);
                        editing[columnName].push(newModel.makeCopy());
                    }
                }
            };

            this.reset = function(){
                this.warning = false;
            };

            this.save = function(){
              saves = [];
              _.each($scope.editing[columnName], function(a, i){
                  var to_save = episode[columnName][i];
                  var editingItem = $scope.editing[columnName][i];
                  delete editingItem.submitted;
                  if(!this.pristine(a) || editingItem[negationField]){
                    saves.push(to_save.save($scope.editing[columnName][i]));
                  }
              }, this);

              return saves;
            };
        };

        $scope.currentCategory = episode.location[0].category;

        $scope.editing = dischargePatientService.getEditing(episode);

        $scope.editing.primary_diagnosis = $scope.episode.primary_diagnosis[0].makeCopy();

        $scope.antimicrobialStep = new MultiStep(
            ["drug", "start_date", "end_date"],
            "no_antimicriobials",
            $scope.editing,
            $scope.episode,
            "antimicrobial"
        );

        $scope.travelStep = new MultiStep(
            ["dates", "destination"],
            "did_not_travel",
            $scope.editing,
            $scope.episode,
            "travel"
        );


        if($scope.is_list_view || !episode.isDischarged()){
            steps.unshift("discharge");
        }

        if($scope.episode.primary_diagnosis.length === 0){
            var primary = $scope.episode.newItem('primary_diagnosis');
            $scope.episode.primary_diagnosis[0] = primary;
        }

        if(!$scope.episode.antimicrobial.length){
            var antimicrobials = [$scope.episode.newItem('antimicrobial')];
            $scope.episode.antimicrobial = antimicrobials;

            $scope.editing.antimicrobial = _.map($scope.episode.antimicrobial, function(a){
                 var copy = a.makeCopy();
                 return copy;
            });

            steps.push("antimicrobial");
        }

        if(!$scope.episode.travel.length){
            var travel = [$scope.episode.newItem('travel')];
            $scope.episode.travel = travel;

            $scope.editing.travel = _.map($scope.episode.travel, function(a){
                 var copy = a.makeCopy();
                 return copy;
            });

            steps.push("travel");
        }

        if(!$scope.episode.consultant_at_discharge[0].consultant){
            steps.push("consultant_at_discharge");
            $scope.editing.consultant_at_discharge = $scope.episode.consultant_at_discharge[0].makeCopy();
        }

        $scope.errors = _.reduce(steps, function(mem, y){
            mem[y] = undefined;
            return mem;
        }, {});

        $scope.nextStep = function(){
            var currentIndex = _.indexOf(steps, $scope.step);

            if(currentIndex + 1 === steps.length){
                return null;
            }
            return steps[currentIndex + 1];
        };

        $scope.previousStep = function(){
            var currentIndex = _.indexOf(steps, $scope.step);

            if(!currentIndex){
                return null;
            }

            return steps[currentIndex - 1];
        };

        $scope.goToPreviousStep = function(){
            $scope.step = $scope.previousStep();
        };

        $scope.resetFormValidation = function(someForm){
            someForm.warning = false;
        };


        $scope.goToNextStep = function(form, model){
            var require_all, nextStep;
            if($scope.step === "diagnosis"){
                if(!form.editing_primary_diagnosis_condition.$valid){
                    form.editing_primary_diagnosis_condition.$setDirty();
                    return;
                }
            }
            if($scope.step === "travel"){
                if(!$scope.travelStep.validateStep()){
                    return;
                }
            }
            if($scope.step === "antimicrobial"){
                if(!$scope.antimicrobialStep.validateStep()){
                    return;
                }
            }
            if($scope.step === "consultant_at_discharge"){
                if(!form.editing_consultant_at_discharge_consultant.$valid){
                    form.editing_consultant_at_discharge_consultant.$setDirty();
                    return;
                }
            }

            nextStep = $scope.nextStep();
            if(nextStep){
                $scope.step = nextStep;
            }
            else{
                $scope.save();
            }
        };

        if(!$scope.step){
            $scope.step = _.first(steps);
        }

        if($scope.episode.secondary_diagnosis.length === 0){
            $scope.editing.secondary_diagnosis =  [{condition: null, co_primary: false, id: 1}];
        }else{
            $scope.editing.secondary_diagnosis = _.map(
                $scope.episode.secondary_diagnosis, function(sd){
                    var copy = sd.makeCopy();
                    copy.submitted = true;
                    return copy;
                });
        }

        $scope.confirming = false;
        $scope.is_list_view = $location.path().indexOf('/list/') === 0;
        //
        // This flag sets the visibility of the modal body
        //
        $scope.discharged = false;

        //
        // We should deal with the case where we're confirming discharge
        //
        if(!$scope.is_list_view){
            $scope.confirming = true;
        }

        //
        // We only really need one lookuplist.
        // TODO: put these into a nicer service.
        //
      	for (var name in options) {
      	    if (name.indexOf('micro_test') !== 0) {
            		$scope[name + '_list'] = options[name];
      	    }
      	}

        //
        // Add an extra Secondary diagnosis option to the list
        //
        var secondaryDiagnosisWarning = false;

        $scope.addSecondary = function(){
            secondaryDiagnosisWarning = !_.every($scope.editing.secondary_diagnosis, function(x){
                return x.condition;
            });

            if(secondaryDiagnosisWarning){
                _.each($scope.editing.secondary_diagnosis, function(e){
                    e.submitted = true;
                });

                var d = {
                    condition: null,
                    co_primary: false,
                    id: $scope.editing.secondary_diagnosis.length + 1
                };

                $scope.editing.secondary_diagnosis.push(d);
            }
        };

        $scope.removeSecondary = function($index){
            $scope.editing.secondary_diagnosis.splice(index, 1);
        }

        // Let's have a nice way to kill the modal.
        $scope.cancel = function() {
      	    $modalInstance.close('cancel');
        };

        //
        // We need to save both the primary diagnosis and any secondary diagnoses.
        // The PD is simple as it's a singleton model, and we ensured it existed
        // above.
        //
        // For SDs, we need to check whether we are creating or updating, and
        // hit the appropriate .save().
        //
        // Once everything has come back from the server, growl the user and kill
        // the modal.
        //
        $scope.save = function() {
            var primary = episode.primary_diagnosis[0];

            if($scope.confirming){
                $scope.editing.primary_diagnosis.confirmed = true;
            }

            var saves = [];
            saves.push(primary.save($scope.editing.primary_diagnosis));

            if(_.contains(steps, "consultant_at_discharge")){
                var to_save = $scope.episode.consultant_at_discharge[0];
                saves.push(to_save.save($scope.editing.consultant_at_discharge));
            }

            saves.concat($scope.antimicrobialStep.save());
            saves.concat($scope.travelStep.save());

            // if they've removed an already existing diagnosis, let them delete it
            _.each($scope.episode.secondary_diagnosis, function(sd){
                if(sd.consistency_token){
                    if(!_.find($scope.editing.secondary_diagnosis)){
                        sd.destroy();
                    }
                }
            });

            _.each(_.filter($scope.editing.secondary_diagnosis,
                            function(sd){ return sd.condition!== null; }),
                   function(sd, index){
                       var save;
                       var secondary;
                       delete sd.submitted;

                       if(sd.consistency_token){
                           var consistency_token = sd.consistency_token;
                           secondary = _.find(
                               $scope.episode.secondary_diagnosis,
                               function(sd){
                                   return sd.consistency_token == consistency_token;
                               }
                           );
                           save = secondary.save(sd);
                       }else{
                           secondary = $scope.episode.newItem('secondary_diagnosis');
                           delete sd.id;
                           save = secondary.save(sd);
                       }
                       saves.push(save);
                   }
              );


            dischargePatientService.discharge(episode, $scope.editing, tags).then(function(){
                $q.all(saves).then(function(){
                    if($scope.confirming){
                        growl.success('Final Diagnosis approved.');
                    }else{
                        growl.success($scope.episode.demographics[0].name + ' discharged.');
                    }
                    $scope.discharged = true;
                    $modalInstance.close('discharged');
                });
            });

        };

        window.scope = $scope;
    });
