
// Function GetAllUserReviews
// setData - use state for saving data
// setOriginalData - backup for saving data
const GetAllUserReviews = (setData, setOriginalData) => {

    fetch("https://lionfish-dear-roughy.ngrok-free.app/review/user/", 
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

export default GetAllUserReviews