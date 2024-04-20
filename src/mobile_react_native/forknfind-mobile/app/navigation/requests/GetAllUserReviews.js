
// Function GetAllUserReviews
// setData - use state for saving data
// setOriginalData - backup for saving data
const GetAllUserReviews = (setData, setOriginalData) => {

    fetch("https://forknfind-fd07ce2d4651.herokuapp.com/review/user/", 
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