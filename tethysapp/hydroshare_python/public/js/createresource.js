const clickevent = (event) => {
    var r = confirm("Are you sure you want to create a Resource ?")
    if (r==false){
        event.preventDefault()
    }
}

var createbutton = document.querySelector("[name=create-button]")
createbutton.addEventListener('click', clickevent);


