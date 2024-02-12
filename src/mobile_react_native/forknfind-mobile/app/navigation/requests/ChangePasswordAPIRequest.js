
// Function ChangePasswordAPIRequest
// currentPassword - user's current password
// newPassword - user's new password
// setResponseData - saving response if it is a success
const ChangePasswordAPIRequest = (currentPassword, newPassword, setResponseData) => {

    console.log("does this work?")
    console.log(currentPassword, newPassword)

    fetch("http://192.168.1.82:8000/user/password/update/", 
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

        console.log(data)
        setResponseData(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default ChangePasswordAPIRequest;