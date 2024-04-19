
// Function LoginAPIRequest
// id - restaurant id
// setData - use state for saving data
const IndividualRestaurantAPIRequest = (id, setData) => {

    fetch("https://lionfish-dear-roughy.ngrok-free.app/api/restaurant/" + id, 
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