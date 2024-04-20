
// Function ChangePasswordAPIRequest
// currentPassword - user's current password
// newPassword - user's new password
// setResponseData - saving response if it is a success
const ChangePasswordAPIRequest = (currentPassword, newPassword, setResponseData) => {

    fetch("https://forknfind-fd07ce2d4651.herokuapp.com/user/password/update/", 
    {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_global,
    },
    body: JSON.stringify({current_password: currentPassword, new_password: newPassword})
    }).then(response=>response.json())
    .then(data=>{

        setResponseData(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default ChangePasswordAPIRequest;