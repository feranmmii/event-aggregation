// Home page
const events_list = document.querySelectorAll('.attend-btn')
for (i = 0; i < events_list.length; i++){
    events_list[i].addEventListener('click', function(){
        eventId = this.dataset.event

        if (isAuthenticated == true){
            console.log('user is logged in')
            bookEvent(eventId)
            events_list[i].classList.add('deactivate-button')
            deactivateButtonByClass('.deactivate-button')
        }
        else{
            alert('You must be signed in')

        }
    })


}

// Json data transfer for booking events
function bookEvent(eventId){
    console.log('loading details page')
    const url = '/book_event_view'
    console.log(url)
    console.log(eventId)

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({'productId': eventId})
    })
    .then((res) =>{
        if (res.ok){
            return res.json()
        }
    })
    .then((data) =>{

        alert(data)

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

booked_event.addEventListener('click', function(){
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
})