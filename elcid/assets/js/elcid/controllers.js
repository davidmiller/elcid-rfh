//
// This is the eLCID custom implementation of a discharge episode controller.
// It is included from the eLCID extra aplication template as defined in
// settings.py
//
controllers.controller('DischargeEpisodeCtrl', function($scope, $timeout,
                                                        $modalInstance, episode,
                                                        currentTag, currentSubTag) {
    // TODO: Reimplement this.
    //
    // $timeout(function() {
    //     dialog.modalEl.find('input,textarea').first().focus();
    // });

    $scope.currentCategory = episode.location[0].category;
    var newCategory;

    if ($scope.currentCategory == 'Inpatient') {
	newCategory = 'Discharged';
    } else if ($scope.currentCategory == 'Review' ||
               $scope.currentCategory == 'Followup') {
	newCategory = 'Unfollow';
    } else {
	newCategory = $scope.currentCategory;
    }

    $scope.editing = {
	category: newCategory,
        discharge_date: null
    };

    $scope.episode = episode.makeCopy();
    if(!$scope.episode.discharge_date){
        $scope.episode.discharge_date = moment().format('DD/MM/YYYY');
    }

    // 
    // Discharging an episode requires updating three server-side entities:
    //
    // * Location
    // * Tagging
    // * Episode
    // 
    // Make these requests then kill our modal.
    // 
    $scope.discharge = function() {

	var tagging = episode.getItem('tagging', 0);
        var location = episode.getItem('location', 0);
        
	var taggingAttrs = tagging.makeCopy();
        var locationAttrs = location.makeCopy();
        var episodeAttrs = episode.makeCopy();

	if ($scope.editing.category != 'Unfollow') {
	    locationAttrs.category = $scope.editing.category;
	}

        if($scope.editing.category == 'Unfollow') {
            // No longer under active review does not set a discharge date
            episodeAttrs.discharge_date = null;
        }else{
            episodeAttrs.discharge_date = $scope.editing.discharge_date;
        }

	if ($scope.editing.category != 'Followup') {
	    taggingAttrs[currentTag] = false;
            if(currentSubTag != 'all'){
                taggingAttrs[currentSubTag] = false;
            }
	}

	tagging.save(taggingAttrs).then(function(){
                location.save(locationAttrs).then(function(){
                        episode.save(episodeAttrs).then(function(){
                                $modalInstance.close('discharged');            
                            })
                    })

	});
    };

    $scope.cancel = function() {
	$modalInstance.close('cancel');
    };
});
