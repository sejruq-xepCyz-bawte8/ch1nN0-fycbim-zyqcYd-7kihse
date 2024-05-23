console.log("cheteme init.js")
if (window.crypto && window.crypto.subtle) {
    var subtle = window.crypto.subtle;
    console.log('Crypro OK')
    // You can now use the subtle object to perform cryptographic operations
} else {
    console.error('Web Crypto API is not supported in this browser.');
}
