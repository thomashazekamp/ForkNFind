
// Function NearbyRestaurantsAPIRequest
// setData - use state passed in that will be updated based on the data
// location - the device location
const NearbyRestaurantsAPIRequest = (setData, location, setOriginalData) => {

    fetch("http://192.168.1.85:8000/find/restaurants/", 
    {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }, body: JSON.stringify({"longitude": location["coords"]["longitude"].toString(), "latitude": location["coords"]["latitude"].toString()}),
    }).then(response=>response.json())
    .then(data=>{

        // set the data
        setData(data);
        setOriginalData(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default NearbyRestaurantsAPIRequest;