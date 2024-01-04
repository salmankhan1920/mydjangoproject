console.log('hello')

const imageInput = document.getElementById('imageInput');
const uploadButton = document.getElementById('uploadButton');
const progressBar = document.getElementById('progressBar');




imageInput.addEventListener('change', () => {
  if (imageInput.files.length > 0) {
    uploadButton.disabled = false;
   // progressBar.style.display = 'block';
  } else {
    uploadButton.disabled = true;
  }
});


uploadButton.addEventListener('click', (event) => {
    event.preventDefault(); 
    progressBar.style.display = 'block';
    const files = imageInput.files;
    const filesLength = files.length;
    const formData = new FormData();
  
    for (let i = 0; i < files.length; i++) {
      formData.append('file', files[i]);
    }


    const csrfToken = getCSRFToken();
    formData.append('csrfmiddlewaretoken', csrfToken);

  
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/site-admin/', true);
  
    xhr.upload.onprogress = function(e) {
      if (e.lengthComputable) {
        const percentComplete = (e.loaded / e.total) * 100;
        // Update the progress bar with the percentage
        progressBar.value = percentComplete;
      }
    };
  
    xhr.onload = function() {
      if (xhr.status === 200) {
         console.log('upload successfull')
         const data = JSON.parse(xhr.responseText);
         if (data.message === 'images successfully saved') {
          const h2 = document.createElement('h2');
          h2.textContent = `Images successfully uploaded. Total images: ${filesLength}`;
          h2.style.color = 'lightgreen';
          h2.style.textAlign = 'center'; 
          document.body.insertBefore(h2, document.body.firstChild);

          imageInput.value = '';
        }
        // Handle the successful upload, e.g., show success message
      } else {
        // Handle the upload error
        const h2 = document.createElement('h2');
        h2.textContent = `Some Error Occured, Images Could Not Be Uploaded`;
        h2.style.color = 'red';
        h2.style.textAlign = 'center'; 
        document.body.insertBefore(h2, document.body.firstChild);
      }
    };
  
    xhr.onerror = function() {
      // Handle any network errors
    };
  
    xhr.send(formData);
  });
  

  function getCSRFToken() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.startsWith('csrftoken=')) {
        return cookie.split('=')[1];
      }
    }
    return '';
  }