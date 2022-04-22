
// ///////////////////Record input of audio//////////////////////////////////////////////
function recordInput()
{
    navigator.mediaDevices.getUserMedia({ audio: true })
.then(stream => {
  const mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();
});


//////////////////////////////////store chunks of data inout recorded/////////////////////////////
navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    const audioChunks = [];

    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });
  });


  ////////////////////////////////////stop record after 3 sec//////////////////////////////////////
navigator.mediaDevices.getUserMedia({ audio: true })
.then(stream => {
  const mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();

  const audioChunks = [];

  mediaRecorder.addEventListener("dataavailable", event => {
    audioChunks.push(event.data);
  });

  setTimeout(() => {
    mediaRecorder.stop();
  }, 3000);
});

///////////////////////////////////// convert chunks to blob URL/////////////////////////////////////////
navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks);
    });

    setTimeout(() => {
      mediaRecorder.stop();
    }, 3000);
  });
  ///////////////////////////////////create url for audio//////////////////////////////////////
  navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });
    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks);
      const audioUrl = URL.createObjectURL(audioBlob);
      console.log(audioUrl)
    });
    setTimeout(() => {
      mediaRecorder.stop();
    }, 3000);
  });
}
  ///////////////////////////////////play input recorded//////////////////////////////////////////////////////
  function playInput()
  {
  navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();

    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });

    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks);
      const audioUrl = URL.createObjectURL(audioBlob);
      const audio = new Audio(audioUrl);
      console.log(audioUrl)
      document.getElementById("audioinput").setAttribute("src",`${audioUrl}`)
      console.log(document.getElementById("audioinput"))
      audio.play();
    });

    setTimeout(() => {
      mediaRecorder.stop();
    }, 3000);
  });

  }
  document.getElementById("recordInput").addEventListener("click",recordInput)  
  document.getElementById("playInput").addEventListener("click",playInput)

/////////////////////////////////////////////play audiotag of record input//////////////////////////////////////////////
const audioContext = new AudioContext();
    // Select the Audio Element from the DOM
const htmlAudioElement = document.getElementById("audioinput");
// Create an "Audio Node" from the Audio Element
const source = audioContext.createMediaElementSource(htmlAudioElement);
// Connect the Audio Node to your speakers. Now that the audio lives in the
// Audio Context, you have to explicitly connect it to the speakers in order to
// hear it
source.connect(audioContext.destination);
//////////////////////////////play db///////////////////////////////////////////////////////////////////////

const audioContext2 = new AudioContext();
const audioElement = document.getElementById("audiodb");

async function playdb() {

  if(audioContext2.state != "running") {
    audioContext2.resume().then(function() {
      console.log('audioContext resumed.')
    });
  }
  audioElement.play();}

//////////////////////////////////////////////////////////////////////////////////////////

// features realtime for input recorded//////////////////////////////////////////////
if (typeof Meyda === "undefined") {
  console.log("Meyda could not be found! Have you included it?");
} else {

// Create the Meyda Analyzer
  const analyzer = Meyda.createMeydaAnalyzer({
    
// Pass in the AudioContext so that Meyda knows which AudioContext Box to work with
    audioContext: audioContext,
    source: source,
  // Buffer Size tells Meyda how often to check the audio feature, and is
  // measured in Audio Samples. Usually there are 44100 Audio Samples in 1
  // second, which means in this case Meyda will calculate the level about 86
  // (44100/512) times per second.
    bufferSize: 512,
    // Here we're telling Meyda which audio features to calculate. While Meyda can
  // calculate a variety of audio features, in this case we only want to know
  // the "rms" (root mean square) "HERE I USE MFCC" of the audio signal, which corresponds to its
  // level
    featureExtractors: ["mfcc"],
  // Finally, we provide a function which Meyda will call every time it
  // calculates a new level. This function will be called around 86 times per
  // second.
    callback: (features) => {
      console.log(features);

    },
  });
  analyzer.start();
}



































//   var ser1 = [ 9, 93, 15, 19, 24 ];
//   var ser2 = [ 31, 97, 81, 82, 39 ];
//   var distFunc = function( a, b ) {
//       return Math.abs( a - b );
//   };
  
//   var dtw = new DynamicTimeWarping(ser1, ser2, distFunc);
// console.log(dtw)


//   var dist1 = dtw.getDistance();
// console.log(dist1)

//   var dist2 = dtw.getPath();
// console.log(dist2)