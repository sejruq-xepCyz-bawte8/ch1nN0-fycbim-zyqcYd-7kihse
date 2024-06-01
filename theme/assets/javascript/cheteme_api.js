async function chetemeAPIjson(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST', // or 'GET', 'PUT', 'DELETE', etc.
            headers: {
                'Content-Type': 'application/json'
            },
            //body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.status}`);
        }

        const jsonResponse = await response.json();
        return jsonResponse;
    } catch (error) {
        console.error('Error sending JSON to API:', error);
        return { error: error.message };
    }
}

// Example usage:
//const apiURL = 'https://api.example.com/endpoint';
//const jsonData = { key: 'value' };

//sendJsonToApi(apiURL, jsonData)
//    .then(responseData => console.log(responseData))
//    .catch(error => console.error('Error:', error));
