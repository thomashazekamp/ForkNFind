
// Function GetAllUserReviews
// id - restaurant id
// setData - use state for saving data
// setOriginalData - backup for saving data
const GetAllRestaurantReviews = (id, setData, setOriginalData) => {

    fetch("https://lionfish-dear-roughy.ngrok-free.app/review/restaurant/" + id, 
    {
        method: 'GET',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_global,
    },
    }).then(response=>response.json())
    .then(data=>{

        // set the data
        setData(data);
        setOriginalData(data);
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default GetAllRestaurantReviews