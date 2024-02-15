
// Function GetUserInformationAPIRequest
// setData - use state for saving data
const GetUserInformationAPIRequest = (setData) => {

    fetch("http://192.168.1.82:8000/user/info/", 
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