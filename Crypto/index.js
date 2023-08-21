const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-={}[]|:;"<>,.?/~`';

// Encryption function
function encrypt_Link(link, key){
    let encryptedLink = "";

    for(let i = 0; i < link.length; i++){
        const linkChar = link[i];
        const keyChar = key[i%key.length];

        const linkIndex = alphabet.indexOf(linkChar);
        const keyIndex = alphabet.indexOf(keyChar);

        if(linkIndex === -1){
            encryptedLink += linkChar;
        }
        else{
            const newIndex = (linkIndex + keyIndex) % alphabet.length;
            encryptedLink += alphabet[newIndex];
        }
    }

    return encryptedLink;
}

// Decrypt function
function decrypt_Link(encryptedLink, key){
    let decryptLink = "";

    for(let i = 0; i < encryptedLink.length; i++){
        const encryptedChar = encryptedLink[i];
        const keyChar = key[i % key.length];

        const encryptedIndex = alphabet.indexOf(encryptedChar);
        const keyIndex = alphabet.indexOf(keyChar);

        if(encryptedIndex === -1){
            decryptLink += encryptedChar;
        }
        else{
            let newIndex = encryptedIndex - keyIndex;
            if(newIndex < 0) newIndex += alphabet.length;
            decryptLink += alphabet[newIndex];
        }
    }

    return decryptLink;
}

// Update result based on selected operation (enc or dec)
function updateResult(isEncrypting){
    const link = document.getElementById("link").value;
    const key = document.getElementById("key").value;

    let result = "";

    if(isEncrypting){
        result = encrypt_Link(link, key);
    }
    else{
        result = decrypt_Link(link, key);
    }

    document.getElementById("result").textContent = result;
}

// Add event listeners to buttons
document.getElementById("enc-btn").addEventListener('click',
function(){
    updateResult(true);
});

document.getElementById("dec-btn").addEventListener('click',
function(){
    updateResult(false);
});

// Initialize the result with encrypted text when page loads
document.addEventListener('DOMContentLoaded', () => {
    updateResult(true);
});