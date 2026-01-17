// JavaScript file with security issues

// SECURITY ISSUE: Hardcoded API key
const API_KEY = 'AIzaSyDummyGoogleAPIKeyForTestingPurposesOnly12345';

// SECURITY ISSUE: Hardcoded password
const dbPassword = 'mypassword123';

// SECURITY ISSUE: XSS vulnerability - no input sanitization
function displayUserInput(userInput) {
    document.getElementById('output').innerHTML = userInput; // Dangerous!
}

// SECURITY ISSUE: Weak encryption
function hashPassword(password) {
    return btoa(password); // Base64 is not encryption, just encoding!
}

// SECURITY ISSUE: Exposed credentials in client-side code
const config = {
    apiKey: process.env.STRIPE_API_KEY || 'your_stripe_api_key_here',
    secretKey: process.env.SECRET_KEY || 'your_secret_key_here'
};

