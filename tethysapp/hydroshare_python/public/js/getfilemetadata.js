

let button = document.getElementById('fetchfile')
const fileSelector = document.getElementById('title_input')
button.addEventListener('click', async function () {
    console.log('Button clicked')
    const username = document.getElementById('username')
    const password = document.getElementById('password')
    const resourceid = document.getElementById('resourcein')
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')

    const formData = new FormData();
    formData.append('username', username && username.value);
    formData.append('password', password && password.value);
    formData.append('resourcein', resourceid.value);
    formData.append('csrfmiddlewaretoken', csrfToken.value);
    const filev_url = document.getElementById('filev-url').getAttribute("data-url");
    const response = await fetch(filev_url, {
        method: 'post',
        body: formData
    });
    if (response.status != 200){
        return
    }
 
    try{
        const responseData = await response.json();
        console.log(responseData)

        var child = fileSelector.lastElementChild;
        while (child) {
            fileSelector.removeChild(child);
            child = fileSelector.lastElementChild;
        }
        // Default option
        const option = document.createElement('option');
        option.textContent = "Select a file";
        fileSelector.append(option)

        // File name options
        responseData.results.forEach(result => {
            const option = document.createElement('option');
            option.value = result.file_name;
            option.textContent = result.file_name;
            fileSelector.append(option)
        })
    }
    catch(err){
        return
    }
    // const responseData = await response.json();
    // console.log(responseData)

})

fileSelector.addEventListener('change', async (event) => {
    const username = document.getElementById('username')
    const password = document.getElementById('password')
    const resourceid = document.getElementById('resourcein')
    const csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]')

    const formData = new FormData();
    formData.append('username', username && username.value);
    formData.append('password', password && password.value);
    formData.append('resourcein', resourceid.value);
    formData.append('title_input', event.target.value);
    formData.append('csrfmiddlewaretoken', csrfToken.value);

    const response = await fetch('.', {
        method: 'post',
        body: formData
    });

    const responseElement = document.querySelector('.responseData');
    responseElement.textContent = JSON.stringify(await response.json(), null, "\t");
})

