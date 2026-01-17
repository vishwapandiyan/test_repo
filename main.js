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
    apiKey: 'sk_live_51234567890123456789012345678901234567890',
    secretKey: 'secret_key_12345'
};

