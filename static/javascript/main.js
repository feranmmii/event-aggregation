// Home page
const events_list = document.querySelectorAll('.attend-btn')
for (i = 0; i < events_list.length; i++){
    events_list[i].addEventListener('click', function(){
        eventId = this.dataset.event

        if (isAuthenticated == 'True'){
            console.log('user is logged in')
            json_data_transfer(eventId, '/book_event_view', action = 'make_booking')
            //this.classList.add('deactivate-button')
            //deactivateButtonByClass('.deactivate-button')
        }
        else{
            console.log(isAuthenticated)
            alert('You must be signed in')

        }
    })
}


// Json data transfer for booking events
function json_data_transfer(eventId, url, action = ''){
    console.log('loading details page')
    console.log(url)
    console.log(eventId)

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'id': eventId, 'action':action})
    })
    .then((res) =>{
        if (res.ok){
            console.log('added to ', action)
            location.reload()
            return res.json()
        }
        else{
            console.log('Error with response')
        }
    })
    
}

function deactivateButtonByClass(class_name){
    const events_name = document.querySelectorAll(class_name)
        for (i = 0; i < events_name.length; i++){
            events_name[i].disabled = true
        }
    }


// my events page
section_title = document.querySelector('#section-title')

booked_event = document.querySelector('#book_event_menue')
created_event = document.querySelector('#created_event_menue')
create_event_btn = document.querySelector('#create_event_menue')

booked_event_content = document.querySelector('#booked-events')
created_event_content = document.querySelector('#created-events')
create_event_content = document.querySelector('#create-events')

/*booked_event.addEventListener('click', function(){
    if (created_event.classList.contains('active')){
        created_event.classList.remove('active')
        created_event_content.classList.add('hidden')
    }

    if (create_event_btn.classList.contains('active')){
        create_event_btn.classList.remove('active')
        create_event_content.classList.add('hidden')
    }

    if (booked_event.classList.contains('active') != true){
        booked_event.classList.add('active')
        booked_event_content.classList.remove('hidden')
        section_title.innerHTML = 'My Booked Events'
    }


})


created_event.addEventListener('click', function(){
    if (created_event.classList.contains('active') != true){
        created_event.classList.add('active')
        created_event_content.classList.remove('hidden')
        section_title.innerHTML = 'My Created Events'
    }

    if (create_event_btn.classList.contains('active')){
        create_event_btn.classList.remove('active')
        create_event_content.classList.add('hidden')
    }

    if (booked_event.classList.contains('active')){
        booked_event.classList.remove('active')
        booked_event_content.classList.add('hidden')
    }
})


create_event_btn.addEventListener('click', function(){
    if (created_event.classList.contains('active')){
        created_event.classList.remove('active')
        created_event_content.classList.add('hidden')
    }

    if (create_event_btn.classList.contains('active') != true){
        create_event_btn.classList.add('active')
        create_event_content.classList.remove('hidden')
        section_title.innerHTML = 'Create an Event'
    }

    if (booked_event.classList.contains('active')){
        booked_event.classList.remove('active')
        booked_event_content.classList.add('hidden')
    }
})*/


// add event listeners to button
const booked_events = document.querySelectorAll('.cancel-btn')

for (i = 0; i < booked_events.length; i++){
    booked_events[i].addEventListener('click', function(){
        eventId = this.dataset.event

        if (isAuthenticated == 'True'){
            console.log('user is logged in')
            json_data_transfer(eventId, '/book_event_view', action = 'cancel_booking')
            console.log(this)
        }
        else{
            console.log(isAuthenticated)
            alert('You must be signed in')

        }
    })
}