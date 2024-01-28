
// Function LoginAPIRequest
// id - restaurant id
// setData - use state for saving data
const IndividualRestaurantAPIRequest = (id, setData) => {

    fetch("http://192.168.1.82:8000/api/restaurant/" + id, 
    {
        method: 'GET',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    }).then(response=>response.json())
    .then(data=>{

        // set the data
        setData(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default IndividualRestaurantAPIRequest