console.log('hello')


var filename = ''

function enableUploadButton() {
    var fileInput = document.getElementById('image-input');
    var uploadButton = document.getElementById('upload-button');
    if (fileInput.value) {
        uploadButton.disabled = false;
        uploadButton.addEventListener('click', function(event) {
            event.preventDefault();
            var formData = new FormData();
            formData.append('image', fileInput.files[0]);

            // Get the CSRF token from the cookie
            var csrfToken = getCookie('csrftoken');
            formData.append('csrfmiddlewaretoken', csrfToken);

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/upload_selfie/');
            xhr.onload = function() {
                if (xhr.status === 200) {
                    // Parse the response text into a JSON object
                    var responseJson = JSON.parse(xhr.responseText);
                    // Compare the response JSON object
                    if (responseJson.message === 'Face found') {
                        // Update the webpage content here
                        document.getElementById('response-container').innerHTML = 'Fetching your images';

                        handleWebSockets()
                    } else if (responseJson.message === 'No face') {

                        // Clear the file selected in the image-input
                        document.getElementById('image-input').value = '';



                        // Create a container div         
                        var container = document.createElement('div');
                        container.setAttribute('id', 'error-container');
                        container.setAttribute('name', 'error container');

                        // Create the first paragraph
                        var paragraph1 = document.createElement('p');
                        paragraph1.style.color = 'red';
                        paragraph1.textContent = 'No face found in the image';

                        // Create the second paragraph
                        var paragraph2 = document.createElement('p');
                        paragraph2.style.color = 'red';
                        paragraph2.textContent = 'Please upload a clear image with face clearly visible';

                        // Add the paragraphs to the container
                        container.appendChild(paragraph1);
                        container.appendChild(paragraph2);

                         // Center the container from left and right
                         container.style.margin = '0 auto';


                        // Insert the container above the form-container
                        var formContainer = document.querySelector('.form-container');
                        formContainer.parentNode.insertBefore(container, formContainer);
                                          
                            
                         
   
                         
                    } else {

   
                        // Handle the error response here
                        console.error('Invalid response: ' + xhr.responseText);
                    }
                } else {
                    // Handle the error response here
                    console.error('Request failed: ' + xhr.status);
                }
                
            };
            xhr.send(formData);

            // Save the filename in a variable
            filename = fileInput.files[0].name;
           //console.log(' name:', filename);
        });
    } else {
        uploadButton.disabled = true;
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



function handleWebSockets() {
    // Generate a UUID for the room name
    const roomName = 'id' + Math.random().toString(16).slice(2);

   // console.log(roomName);

    // Create a WebSocket connection
    var socket = new WebSocket('ws://127.0.0.1:8000/ws/upload_selfie/' + roomName + '/');

    // Connection opened
    socket.addEventListener('open', function(event) {
        let message = {
            'message' : 'Hello Server!'
        }
        socket.send(JSON.stringify(message));
        console.log('connection established');
    });

    // Listen for messages
    socket.addEventListener('message', function(event) {
       // console.log('Message from server ', event.data);

        // Parse the message data
        const message = JSON.parse(event.data);

        console.log('Parsed message data', message);

        // Update the webpage content based on the message data
        if (message.message === 'connection success') {
              // Create a JSON object
              let message = {
                 'message': 'filename',
                 'filename': filename
                 };

             socket.send(JSON.stringify(message))
        } else if (message.message === 'result') {
           
             let imageName = message.image_names

             var imageNames =  imageName  // Assuming python_image_list is the variable containing the Python list

             // Construct the base URL using window.location.host
             var baseUrl = window.location.protocol + '//' + window.location.host;
     
            // Calculate the number of pages and the start index for the current page
var totalImages = imageNames.length;
var pageSize = 5;
var totalPages = Math.ceil(totalImages / pageSize);

// Function to display the images for the current page
function displayImages(pageNumber) {
    var startIndex = (pageNumber - 1) * pageSize;
    var endIndex = startIndex + pageSize;
    var imagesContainer = document.getElementById('imageContainer');
    imagesContainer.innerHTML = ''; // Clear the container
    for (var i = startIndex; i < endIndex && i < totalImages; i++) {
        var img = document.createElement('img');
        img.src = baseUrl + '/media/selfies/' + imageNames[i];  // Replace with the actual path to your images
        img.alt = imageNames[i];
        imagesContainer.appendChild(img);
    }
}

// Display the images for the first page
displayImages(1);

// Create pagination buttons
var paginationContainer = document.createElement('div');
paginationContainer.classList.add('pagination');
for (var i = 1; i <= totalPages; i++) {
    var button = document.createElement('button');
    button.classList.add('pagination-button')
    button.textContent = i;
    button.addEventListener('click', function() {
         // Change the background color of the clicked button to gray
        this.style.backgroundColor = 'gray';
         // Change the background color of all other buttons to blue
         var buttons = paginationContainer.getElementsByTagName('button');
         for (var j = 0; j < buttons.length; j++) {
             if (buttons[j] !== this) {
                 buttons[j].style.backgroundColor = '#007bff';
             }
         }


        displayImages(parseInt(this.textContent));
    });
    paginationContainer.appendChild(button);
}

document.body.appendChild(paginationContainer);

// Create a function to handle the click event of the "Download All Images" button
function downloadAllImages() {
    // Loop through the imageNames array and initiate the download for each image
    imageNames.forEach(function(imageName) {
      var link = document.createElement('a');
      link.href = baseUrl + '/media/selfies/' + imageName;
      link.download = imageName;
      link.click();
    });
  }
  
  // Create the "Download All Images" button
  var downloadButton = document.createElement('button');
  downloadButton.textContent = 'Download All Images';
  downloadButton.classList.add('download-button')
  /*
  downloadButton.style.marginTop = "10px";
  downloadButton.style.backgroundColor = "#007bff";
  downloadButton.style.color = 'white';
  downloadButton.style.cursor = "pointer";
  */
  downloadButton.addEventListener('click', downloadAllImages);
  document.body.appendChild(downloadButton);
  

            
                    
            
            // Display lion image
        } else {
            // Display a default image or provide a fallback
        }
    });

    // Handle connection close
    socket.addEventListener('close', function(event) {
        // Update the webpage to show an error message
        // For example, you can display an error message in a specific element
        document.getElementById('error-message').innerText = 'Connection closed. Please refresh the page to reconnect.';
    });
}
