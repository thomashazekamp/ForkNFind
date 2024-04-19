
// Function GetUserInformationAPIRequest
// setData - use state for saving data
const GetUserInformationAPIRequest = (setData) => {

    fetch("https://lionfish-dear-roughy.ngrok-free.app/user/info/", 
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
        setData(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default GetUserInformationAPIRequest;