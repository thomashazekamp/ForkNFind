
// Function LoginAPIRequest
// setData - use state for saving data
// id - restaurant id
// location - location information for user
const ContentRecommendationsAPIRequest = (setData, id, location) => {

    fetch("https://lionfish-dear-roughy.ngrok-free.app/recommend/content/" + id + "/" + location.latitude + "/" + location.longitude, 
    {
        method: 'GET',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    }).then(response=>response.json())
    .then(data=>{

        // set the data
        setData(data);
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default ContentRecommendationsAPIRequest;