const fs = require('fs');
const fetch = require('node-fetch');

// Read the audio file
const audioFile = fs.readFileSync('path/to/audio/file.wav');

// Convert the audio file to base64
const base64Audio = audioFile.toString('base64');

// Make a POST request to the Whisper API
fetch('https://api.openai.com/v1/engines/whisper/betas/0.2/completions', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY'
    },
    body: JSON.stringify({
        prompt: 'Your prompt goes here',
        max_tokens: 100
    })
})
    .then(response => response.json())
    .then(data => {
        // Handle the response from the API
        const generatedText = data.choices[0].text;
        console.log(generatedText);
        // Do something with the generated text
    })
    .catch(error => {
        console.error('Error:', error);
    });

    //rhuoghriuhgiefwefiohwih;fgrtjeguykftrhgiriguuehgrjkbjewirgghiugkrlgrweahwfejkiufguhewrsguhfdhgfdhgkj