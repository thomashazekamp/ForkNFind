
// Function LoginAPIRequest
// setIsLoggedIn - use state passed in that will be updated if the login is successful
// username - the username inputted by the user
// password - the password inputted by the user
const LoginAPIRequest = ({setIsLoggedIn, username, password}) => {

    console.log(JSON.stringify({username: username, password: password}))

    // Fetch the API with this information
    fetch("http://192.168.1.82:8000/api/token/", 
    {
        method: 'POST',
        headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({username: username, password: password})
    }).then(response=>response.json())
    .then(data=>{

        // Save the information returned
        username_global = data["username"]
        access_global = data["access"]
        setIsLoggedIn(true)
        
        console.log(data)
    })
    .catch(error => {
        console.error('Network request failed:', error);
      })
    ;
}  

export default LoginAPIRequest