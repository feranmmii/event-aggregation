console.log('every one shuld see')
const confirm_event_delete = function(){
    deleteEvents = document.querySelectorAll('.created-event')
    console.log(deleteEvents)
    for(i = 0; i<deleteEvents.length; i++){
        console.log(i)
        deleteEvents[i].addEventListener('click', function(){
            console.log('am in confirm')
            ans = confirm('Are you sure you want to delete this event?')
            if (ans){
                eventId = this.dataset.event
                console.log('in delete funct')
                json_data_transfer(eventId, '/delete_event', action = 'delete_booking')
            }
        })
    }

}

const delete_event = function(ans){
    if (ans){
        eventId = this.dataset.event
        console.log('in delete funct')
        json_data_transfer(eventId, '/user_events', action = 'delete_booking')

    }
}


confirm_event_delete()

