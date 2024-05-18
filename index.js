const fs = require('fs');
const fetch = require('node-fetch');

const audioFile = fs.readFileSync('path/to/audio/file.wav');

const base64Audio = audioFile.toString('base64');

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
        const generatedText = data.choices[0].text;
        console.log(generatedText);
    })
    .catch(error => {
        console.error('Error:', error);
    });