async function app() {
   const model = await tf.loadLayersModel('/tfjs/model.json')

   navigator.getUserMedia(
      { video: true },
      stream => {
         var video = document.getElementById('v')
         var canvas = document.getElementById('c')
         var button = document.getElementById('b')

         video.src = stream
         video.srcObject = stream
         video.play()

         button.disabled = false

         button.onclick = () => {
            canvas.getContext('2d').drawImage(video, 0, 0, 300, 300, 0, 0, 300, 300)
            var img = canvas.toDataURL('image/png')
            console.log(img)
         }
      },
      err => {
         alert('there was an error ' + err)
      }
   )
}

app()
